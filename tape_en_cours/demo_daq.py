#!/usr/bin/python3

from ni_cts3 import *  # pylint: disable=unused-wildcard-import
from ni_cts3.Nfc import *  # pylint: disable=unused-wildcard-import
from ni_cts3.Daq import *  # pylint: disable=unused-wildcard-import
from ni_cts3.MPException import CTS3Exception
from time import time, sleep
from pathlib import Path
from tkinter import Tk, TOP, BOTH
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # type: ignore
from matplotlib.figure import Figure  # type: ignore
from numpy import float64, linspace, array
from typing import Optional, cast, Any

try:
    from numpy.typing import NDArray

    np_array = NDArray[float64]
except ModuleNotFoundError:
    np_array = Any  # type: ignore[misc, assignment]
try:
    from scipy import signal  # type: ignore

    RESAMPLING = 3  # Resampling factor
    DISCARD_COUNT = 50  # Number of points to discard after resampling
except ModuleNotFoundError:
    RESAMPLING = 0
    DISCARD_COUNT = 0

__author__ = "NI"
__license__ = "unlicense.org"

FILE_NAME = Path(__file__).with_suffix(".mpat")
DURATION = 10e-6  # 10 µs
SAMPLING_RATE = 150e6  # 150 MHz
ACQ_CHANNEL = DaqChannel.CH  # CH2 SMA

# Trigger configuration
TRIGGER = DaqTrigSource.TRIG_CH2
THRESHOLD = 0  # 0 V
TIMEOUT = 2  # 2 s


def analyze_file() -> np_array:
    """Analyzes downloaded file

    Returns
    -------
    NDArray[float64]
        Resampled and interpolated values in mV
    """
    values = array([pt.y * 1e3 for pt in load_signals(FILE_NAME)[0]])
    if RESAMPLING:
        resampled = signal.resample(values, values.size * RESAMPLING)
        return cast(np_array, resampled[DISCARD_COUNT:-DISCARD_COUNT])
    else:
        return values


def launch_acquisition(canvas: FigureCanvasTkAgg) -> Optional[np_array]:  # type: ignore
    """Launch acquisition

    Parameters
    ----------
    canvas : FigureCanvasTkAgg
        Canvas the figure renders into

    Returns
    -------
    NDArray[float64]
        Voltages in mV, or None if fatal error occurred
    """
    global stop
    result = None
    try:
        Daq_StartStopAcq(DaqAcqMode.MODE_SINGLE, file_name=FILE_NAME)

        # Poll status
        status = Daq_GetStatus()
        start = time()
        while status < DaqStatus.STATUS_FILE_AVAILABLE:
            if time() - start > TIMEOUT:
                print("Timeout")
                break
            sleep(0.01)
            if not stop:
                canvas.flush_events()
            status = Daq_GetStatus()

        # Check status
        if status == DaqStatus.STATUS_OVERFLOW:
            result = None
            print("Overflow")

        elif status == DaqStatus.STATUS_OVERRANGE:
            print("Out of range")
            result = analyze_file()

        elif status == DaqStatus.STATUS_OVERVOLTAGE:
            result = None
            print("Overvoltage")

        elif status == DaqStatus.STATUS_FILE_AVAILABLE:
            result = analyze_file()

    except (CTS3Exception, Exception) as e:
        print(e)
        result = None
    finally:
        Daq_StartStopAcq(DaqAcqMode.MODE_STOP)
        return result


def on_closing() -> None:
    """Close window event"""
    global root, stop
    stop = True
    if root is not None:
        root.destroy()


root = None
# host = input("CTS3 hostname: ")
try:
    OpenCommunication("192.168.142.1")

    # Open resource
    MPOS_OpenResource()

    # Configure acquisition channel
    points_number = int(DURATION * SAMPLING_RATE)
    if points_number % 4:
        # Ensure points number is a multiple of 4
        points_number += 4 - (points_number % 4)
    Daq_SetChannel(ACQ_CHANNEL, True, DaqRange.RANGE_2000)
    Daq_SetTimeBase(DaqSamplingClk.SCLK_150MHZ, points_number)
    Daq_SetTrigger(TRIGGER, THRESHOLD, DaqTrigDir.DIR_RISING_EDGE, 0)

    # Adjust points number to reflect resampling operation
    if RESAMPLING:
        points_number *= RESAMPLING
        points_number -= 2 * DISCARD_COUNT

    # Apply a field of 1.5 Vpp (750 mVp) at 13.66 MHz
    MPC_SelectCarrier(13.66e6)
    MPC_SelectFieldStrength(FieldUnit.UNIT_MV_RANGE_2V5, 1500)

    root = Tk()
    root.wm_title("CTS3 acquisition")
    root.protocol("WM_DELETE_WINDOW", on_closing)

    fig = Figure()
    ax = fig.add_subplot()
    x = linspace(1e6 / SAMPLING_RATE, DURATION * 1e6, points_number)
    line = None
    ax.set_xlabel("time (µs)")
    ax.set_ylabel("voltage (mV)")
    ax.set_ybound(-DaqRange.RANGE_2000 / 2, DaqRange.RANGE_2000 / 2)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    stop = False
    while not stop:
        points = launch_acquisition(fig.canvas)
        if points is None:
            # Fatal error occurred
            break
        if len(points) == points_number:
            if not line:
                (line,) = ax.plot(x, points, "g", scaley=False)
                fig.tight_layout()
                root.lift()
            line.set_ydata(points)
            fig.canvas.draw()
            fig.canvas.flush_events()

    # Switch RF field off
    MPC_SelectFieldStrength(FieldUnit.UNIT_MV_RANGE_2V5, 0)

except (CTS3Exception, Exception) as e:
    print(e)
finally:
    if root:
        root.quit()
    try:
        # Stop the acquisition
        Daq_StartStopAcq(DaqAcqMode.MODE_STOP)

        # Close resource
        MPOS_CloseResource()
    except CTS3Exception:
        pass

    CloseCommunication()
    if FILE_NAME.is_file():
        FILE_NAME.unlink()

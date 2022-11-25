import ni_cts3
from ni_cts3 import Nfc, Daq
import time
from pathlib import Path


class CTS3:
    def __init__(self, ip: str, log: bool):
        self.ip = ip
        self.log_file = Path(__file__).with_suffix(".log")
        print(self.log_file)
        ni_cts3.OpenCommunication(ip, log=log)
        self.set_NFC()
        self.set_dac()
        ni_cts3.SetDLLDebugMode(self.log_file)
        # ni_cts3.MPS_Beep(0.1)
        self.__puissance = None

    def set_NFC(self):
        ni_cts3.MPOS_OpenResource(
            ni_cts3.ResourceType.CTS3_NFC_RESOURCE_ID,
            blocking_mode=ni_cts3.ResourceBlockingMode.OVERRIDE,
        )

    def set_dac(self):
        ni_cts3.MPOS_OpenResource(
            ni_cts3.ResourceType.CTS3_DAQ_RESOURCE_ID,
            blocking_mode=ni_cts3.ResourceBlockingMode.OVERRIDE,
        )
        Daq.Daq_SetChannel(Daq.ACQ_CHANNEL, True, Daq.DaqRange.RANGE_2000)
        ni_cts3.Daq.Daq_SetTimeBase(
            ni_cts3.Daq.DaqSamplingClk.SCLK_150MHZ, ni_cts3.Daq.points_number
        )
        ni_cts3.Daq.Daq_SetTrigger(
            ni_cts3.Daq.TRIGGER,
            ni_cts3.Daq.THRESHOLD,
            ni_cts3.Daq.DaqTrigDir.DIR_RISING_EDGE,
            0,
        )

    @property
    def champ(self):
        return self.__puissance

    @champ.setter
    def champ(self, puissance):
        self.__puissance = puissance
        Nfc.MPC_SelectFieldStrength(Nfc.FieldUnit.UNIT_MV_RANGE_25V, puissance)

    def close(self):
        ni_cts3.CloseCommunication()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


# ni_cts3.OpenCommunication("192.168.142.1", log=True)
# ni_cts3.MPOS_OpenResource(
#     ni_cts3.ResourceType.CTS3_NFC_RESOURCE_ID,
#     blocking_mode=ni_cts3.ResourceBlockingMode.OVERRIDE,
# )
# Nfc.MPC_SelectFieldStrength(Nfc.FieldUnit.UNIT_MV_RANGE_25V, 10_000)
# time.sleep(5)
# ni_cts3.CloseCommunication()

andouillette = CTS3("192.168.142.1", log=True)
andouillette.champ = 10_000
time.sleep(2)
andouillette.close()

with CTS3("192.168.142.1", log=True) as andouillette:
    andouillette.champ = 10_000
    time.sleep(5)

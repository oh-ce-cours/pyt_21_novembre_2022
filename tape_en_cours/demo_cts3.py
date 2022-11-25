import ni_cts3
from ni_cts3 import Nfc, Daq
import time
from pathlib import Path


class CTS3Exception(ValueError):
    pass


class CTS3:
    def __init_(self, ip: str, log: bool):
        self.ip = ip
        self.log_file = Path(__file__).with_suffix(".log")
        # print(self.log_file)
        ni_cts3.OpenCommunication(ip, log=log)
        ni_cts3.SetDLLDebugMode("/tmp/toto.log")
        self.set_NFC()
        self.set_dac()
        # ni_cts3.MPS_Beep(0.1)
        self.__puissance = None

    def set_NFC(self):
        ni_cts3.MPOS_OpenResource(
            ni_cts3.ResourceType.CTS3_NFC_RESOURCE_ID,
            blocking_mode=ni_cts3.ResourceBlockingMode.OVERRIDE,
        )

    def set_dac(self, channel: int = 1):
        if channel not in [1, 2]:
            raise CTS3Exception(f"Les channels sont 1 ou 2, pas {channel}")

        daq_channel = getattr(Daq.DaqChannel, f"CH_{channel}_SMA")
        trigger_source = getattr(Daq.DaqTrigSource, f"TRIG_CH{channel}")
        ni_cts3.MPOS_OpenResource(
            ni_cts3.ResourceType.CTS3_DAQ_RESOURCE_ID,
            blocking_mode=ni_cts3.ResourceBlockingMode.OVERRIDE,
        )
        Daq.Daq_SetChannel(daq_channel, True, Daq.DaqRange.RANGE_2000)
        Daq.Daq_SetTimeBase(Daq.DaqSamplingClk.SCLK_150MHZ, 100_000)
        Daq.Daq_SetTrigger(
            trigger_source,
            0,
            Daq.DaqTrigDir.DIR_RISING_EDGE,
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

# andouillette = CTS3("192.168.142.1", log=True)
# andouillette.champ = 10_000
# time.sleep(2)
# andouillette.close()

with CTS3("192.168.142.1", log=True) as andouillette:
    andouillette.champ = 10_000
    time.sleep(5)

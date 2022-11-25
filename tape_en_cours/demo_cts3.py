import ni_cts3
from ni_cts3 import Nfc
import time

class CTS3:
    def __init__(self, ip:str, log:bool)

ni_cts3.OpenCommunication("192.168.142.1", log=True)
ni_cts3.MPOS_OpenResource(
    ni_cts3.ResourceType.CTS3_NFC_RESOURCE_ID,
    blocking_mode=ni_cts3.ResourceBlockingMode.OVERRIDE,
)
Nfc.MPC_SelectFieldStrength(Nfc.FieldUnit.UNIT_MV_RANGE_25V, 10_000)
time.sleep(5)
ni_cts3.CloseCommunication()

import ni_cts3
from ni_cts3 import Nfc

ni_cts3.OpenCommunication("192.168.142.1", log=True)
ni_cts3.MPOS_OpenResource(ni_cts3.ResourceType.CTS3_NFC_RESOURCE_ID)
Nfc.MPC_SelectFieldStrength(Nfc.FieldUnit.UNIT_MV_RANGE_25V, 10_000)
ni_cts3.CloseCommunication()

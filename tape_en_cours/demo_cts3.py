import ni_cts3
from ni_cts3 import Nfc

ni_cts3.OpenCommunication("192.168.142.1", log=True)
Nfc.MPC_SelectFieldStrength(
    Nfc.FieldUnit.UNIT_MV_RANGE_25V,
    10_000,
)

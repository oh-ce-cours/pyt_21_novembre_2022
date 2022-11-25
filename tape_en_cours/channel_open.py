from time import perf_counter

# import apis
from ni_cts3 import (
    SetDLLMode,
    SetDLLDebugMode,
    OpenCommunication,
    MPOS_GetResourceID,
    MPOS_OpenResource,
    MPS_ResetHard,
    MPOS_CloseResource,
    CloseCommunication,
)
from ni_cts3.Nfc import (
    MPC_NfcConfiguration,
    BeginDownloadTo,
    MPS_OpenLog,
    MPS_CloseLog,
    MPS_EndDownload,
)
from ni_cts3.CardEmu import MPC_ChannelOpen, MPC_ChannelClose

# import structs
from ni_cts3 import LibraryMode, ResourceBlockingMode
from ni_cts3.Nfc import NfcMode, NfcDataRate

cts_ip = "192.168.142.1"
resource_id = MPOS_GetResourceID()

############
# HELPERS
###########
def init():
    SetDLLMode(LibraryMode.MONOTHREADED)
    SetDLLDebugMode(".\\dll_debug.log")
    OpenCommunication(cts_ip)

    MPOS_OpenResource(
        resource_id=resource_id, blocking_mode=ResourceBlockingMode.OVERRIDE
    )

    MPS_ResetHard()


def init_spy():
    MPC_NfcConfiguration(
        mode=NfcMode.NFC_PASSIVE_MODE, initiator=True, data_rate=NfcDataRate.NFC_106
    )
    # Needed for FC Detect / FC Detect Ex to be displayed properly

    BeginDownloadTo("./logs.mplog")
    MPS_OpenLog()


def close_spy():
    MPS_CloseLog()
    MPS_EndDownload()


def close():
    MPOS_CloseResource(resource_id=resource_id)
    CloseCommunication()


############
# MAIN
###########


def main():
    init()
    init_spy()
    ##################

    MPC_NfcConfiguration(
        mode=NfcMode.NFC_PASSIVE_MODE, initiator=False, data_rate=NfcDataRate.NFC_106
    )
    print(perf_counter())
    MPC_ChannelOpen()
    print(perf_counter())
    MPC_ChannelClose()

    ##################
    close_spy()
    close()


if __name__ == "__main__":
    main()

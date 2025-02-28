#!python3

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import sys

def set_volume(volume: float):

    devices= AudioUtilities.GetSpeakers()
    interface= devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_control= cast(interface, POINTER(IAudioEndpointVolume))

    channels= volume_control.GetChannelCount()
    if channels < 2:
        print("Stereo output not detected")
        return None

    left= volume_control.GetChannelVolumeLevelScalar(0)
    right= volume_control.GetChannelVolumeLevelScalar(1)

    if left == right:
        volume_control.SetMasterVolumeLevelScalar(volume, None)
    else:
        volume_control.SetChannelVolumeLevelScalar(0, volume, None)
        volume_control.SetChannelVolumeLevelScalar(1, 0.0, None)

# volume is provided in integer where 0 is mute and 100 is full sound
# eg: 50 will change volume to 50
if __name__ == "__main__":
    vol= sys.argv[1].lower()
    if len(vol) == 1:
        set_volume(float(f"0.0{vol}"))
    elif len(vol) == 2:
        set_volume(float(f"0.{vol}"))
    else:
        set_volume(1.0)

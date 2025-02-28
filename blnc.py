#!python3

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import sys


def set_balance(left: float, right: float):
    devices= AudioUtilities.GetSpeakers()
    interface= devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_control= cast(interface, POINTER(IAudioEndpointVolume))

    channels = volume_control.GetChannelCount()
    if channels < 2:
        print("Stereo output not detected")
        return

    volume_control.SetChannelVolumeLevelScalar(0, left, None)
    volume_control.SetChannelVolumeLevelScalar(1, right, None)

# use s to change it to speaker and e to change it to earphone
# i have some problem on my right side speaker that's why it is on mute
if __name__ == "__main__":
    choice= sys.argv[1].lower()
    if choice == "s":
        set_balance(0.7, 0.0)
    elif choice == "e":
        set_balance(0.09, 0.09)
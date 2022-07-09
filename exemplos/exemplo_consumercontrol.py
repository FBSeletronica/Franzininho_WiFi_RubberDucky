import time
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

cc = ConsumerControl(usb_hid.devices)

# Raise volume.
cc.send(ConsumerControlCode.VOLUME_INCREMENT)
time.sleep(5)
# Decrease volume.
cc.send(ConsumerControlCode.VOLUME_DECREMENT )
time.sleep(5)
# Pause or resume playback.
cc.send(ConsumerControlCode.PLAY_PAUSE)
time.sleep(2)
# send brightness up button press
cc.send(ConsumerControlCode.BRIGHTNESS_INCREMENT)
time.sleep(2)
# send brightness down button press
cc.send(ConsumerControlCode.BRIGHTNESS_DECREMENT)

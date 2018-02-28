# This file is executed on every boot (including wake-boot from deepsleep)

#import esp
#esp.osdebug(None)
import gc
#import webrepl
#webrepl.start()
gc.collect()

# Set up WLAN access
try:
    with open('wlan_credentials.txt') as f:
        ssid, password = f.read().strip().split('=')
        import network
        sta_if = network.WLAN(network.STA_IF)
        sta_if.active(True)
        sta_if.connect(ssid, password)
except OSError:
    print('Could not open wlan_credentials.txt.')

# Apparently NodeMCUs have a weird PIN wiring
# https://github.com/esp8266/Arduino/blob/esp8266/hardware/esp8266com/esp8266/variants/nodemcu/pins_arduino.h#L49
import machine
D0 = const(16)
D1 = const(5)
D2 = const(4)
D3 = const(0)
D4 = const(2)
D5 = const(14)
D6 = const(12)
D7 = const(13)
D8 = const(15)
D9 = const(3)
D10 = const(1)

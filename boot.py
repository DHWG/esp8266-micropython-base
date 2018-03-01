# This file is executed on every boot (including wake-boot from deepsleep)

#import esp
#esp.osdebug(None)
import gc
#import webrepl
#webrepl.start()
gc.collect()

# get the configuration
import config

# Set up WLAN access
import time
import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(config.WLAN_SSID, config.WLAN_PASSWORD)
while not sta_if.isconnected():
    print('Connecting to WIFI...')
    time.sleep_ms(50)

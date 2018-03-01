# ESP8266 MicroPython Base

This is the base project for NodeMCUs to speed up IoT projects in DHWG.

## Hardware

* NodeMCU V3 Arduino ESP8266 ESP-12 E Lua CH340 WiFI WLan IoT Lolin Mini Micro (~5€ on eBay)

## Installation

* [Official documentation](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html)
* [MacOS driver for serial interface](http://www.wch.cn/download/CH341SER_MAC_ZIP.html)

Following commands flash the MicroPython firmware:

```sh
esptool.py --port /dev/cu.wchusbserial1410 erase_flash
esptool.py --port /dev/cu.wchusbserial1410 --baud 115200 write_flash --flash_size=detect -fm dio 0 esp8266-20171101-v1.9.3.bin
```

## Configuration

The [AMPY tool](https://github.com/adafruit/ampy) can be used to transfer files
to the chip.

```sh
ampy -p /dev/cu.wchusbserial1410 -b 115200 put boot.py /boot.py
```

Make sure to create an instance of `config.py` put it on the chip.

## REPL Access

Access to the MicroPython REPL is possible with the _screen_ tool:

```sh
screen /dev/cu.wchusbserial1410 115200
```

## MQTT Access

Good tools:
* http://www.jensd.de/apps/mqttfx/
* http://kamilfb.github.io/mqtt-spy/

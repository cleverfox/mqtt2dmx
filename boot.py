# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import os, machine
#os.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
import network
from machine import RTC
import ntptime
from umqttsimple import MQTTClient
import ubinascii
from array import array
from machine import Pin

sta_if = network.WLAN(network.STA_IF)
sta_if.connect('my_home_wifi_network_name','home_wifi_password')
mqtt_server = '192.168.1.2'

webrepl.start()
tz=7
gc.collect()
ntpsync=0
client_ready=0
rtc = RTC()
ntptime.host='ntp0.rfei.ru'

client_id = ubinascii.hexlify(machine.unique_id())
topic_dmx = b'dmx/+'

dmx_message=array('B',[0]*513);
dmx_message[1]=0;
dmx_message[2]=0;
dmx_message[3]=0;
dmx_message[4]=0;

Pin(4, Pin.OUT).value(0)

from machine import UART
def senddmx(data):
    time.sleep_us(180)
    dmx=Pin(2, Pin.OUT).value(0)
    time.sleep_us(180)
    dmx=UART(1)
    dmx.init(250000,bits=8,parity=None,stop=2)
    dmx.write(data)





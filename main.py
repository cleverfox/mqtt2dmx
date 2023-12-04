# Complete project details at https://RandomNerdTutorials.com

import time
import json
import re
from machine import Timer

def sub_cb(topic, msg):
  print((topic, msg))
  if(topic==b'dmx/data'):
      dm=json.loads(msg)
      for a in dm.keys():
          if(a>0 and a<=512):
              dmx_message[a]=dm[a];
      print('dmx data %', dm)
      Pin(4, Pin.OUT).value(1)
  else:
      x=re.match('dmx/([01-9]+)',topic)
      if(x):
          print('dmx sch % = %', x.group(1),int(float(msg)))
          dmx_message[int(x.group(1))]=int(float(msg))
          Pin(4, Pin.OUT).value(1)

def connect_and_subscribe():
  global client_id, mqtt_server, topic_dmx, client
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_dmx)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_dmx))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Restarting...')
  Pin(4, Pin.OUT).value(0)
  time.sleep(10)
  machine.reset()

def run_dmx(n):
    global dmx_message,client;
    senddmx(dmx_message)
    if('client' in globals()):
        try:
            client.check_msg()
        except OSError as e:
          print ("error %",e)
          reconnect()



dmxt = Timer(-1)
dmxt.init(period=100, mode=Timer.PERIODIC, callback=run_dmx)

while sta_if.isconnected() == False:
  time.sleep(1)
  pass

def reconnect():
    try:
      client = connect_and_subscribe()
      client_ready=1
    except OSError as e:
      restart_and_reconnect()

reconnect()


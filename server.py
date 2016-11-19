import Adafruit_DHT
import time
import paho.mqtt.client as mqtt

mqttc=mqtt.Client()
mqttc.connect("iot.eclipse.org",1883,60)
mqttc.loop_start()

#read temperature
def read_temperature():
    humidity, temperature = Adafruit_DHT.read_retry(11,4)
    print humidity
    print temperature
    return temperature

#publish temperature
while 1:
    t=read_temperature()
    (result,mid)=mqttc.publish("topic/GeneralizedIoT",t,2)
    time.sleep(1)

mqttc.loop_stop()
mqttc.disconnect()


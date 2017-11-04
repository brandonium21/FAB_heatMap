import serial
import paho.mqtt.client as broker
from time import sleep


# connect to broker
host = '192.17.189.184'
port = '1885'
nodeName = '3d_printers'
topic = "heatMap/{}".format(nodeName)
ser = serial.Serial('/dev/tty.usbserial', 9600)

broker.connect(host, port)
broker.loop_start()

while True:
    payload = ser.readline()
    broker.publish(topic, payload)
    sleep(0.5)
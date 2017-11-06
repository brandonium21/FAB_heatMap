import paho.mqtt.client as broker
import paho.mqtt.subscribe as subscribe
from time import sleep


# connect to broker
host = '192.17.189.184'
port = '1883'
filterTopic = '#'
topic = "heatMap/{}".format(filterTopic)
topics = ["heatMap/stickers", "heatMap/3d_printers"]

while True:
	msg = subscribe.simple(topics, hostname=host)
	print("%s %s" % (msg.topic, msg.payload))

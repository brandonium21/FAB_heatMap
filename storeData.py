from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import paho.mqtt.client as broker
import paho.mqtt.subscribe as subscribe
from time import sleep
from store import Node, Base, database_uri

# connect to broker
host = '192.17.189.184'
port = '1883'
filterTopic = '#'
topic = "heatMap/{}".format(filterTopic)
topics = ["heatMap/stickers", "heatMap/3d_printers", "heatMap/Uni_laser", "heatMap/epilog_laser"]

engine = create_engine(database_uri)

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)

session = DBSession()

while True:
	msg = subscribe.simple(topics, hostname=host)
	print("%s %s" % (msg.topic, msg.payload))
	new_Node = Node(node_name=msg.topic, dist_val= msg.payload)
	session.add(new_Node)
	session.commit()

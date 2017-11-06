import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime
database_uri = 'postgres://hlnvnpjufoiijp:df18e7911b9aea598f5405ee0045f87a6ab8dded19781a67f8c307af48cd884b@ec2-54-163-246-154.compute-1.amazonaws.com:5432/d3g34bk2bn1v3u'

Base = declarative_base()
 
class Node(Base):
    __tablename__ = 'node'
    id = Column(Integer, primary_key=True)
    node_name = Column(String(50))
    time = Column(DateTime, default=datetime.datetime.utcnow)
    dist_val = Column(Integer, nullable=False)


engine = create_engine(database_uri)

Base.metadata.create_all(engine)
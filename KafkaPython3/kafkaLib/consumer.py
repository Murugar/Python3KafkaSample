#!/usr/bin/env python
from kafka import KafkaConsumer

class Consumer():
    def __init__(self):
        consumer = KafkaConsumer('messages',
                                 group_id='my_group',
                                 bootstrap_servers=['192.168.99.100:9092'])


        print ("Consumed Start") 
        for message in consumer:
            print ("Consumed Msg -> '%s' on Topic -> '%s' with Offset -> %d" %
                    (message.value.decode('utf-8'), message.topic, message.offset))
       
        print ("Consumer Close") 
        consumer.close()

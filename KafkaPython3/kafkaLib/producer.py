#!/usr/bin/env python
from kafka import SimpleProducer, KafkaClient

class Producer():
    def __init__(self):
        kafka = KafkaClient('192.168.99.100:9092')
        producer = SimpleProducer(kafka)
       
        producer.send_messages('messages', b'super-duper-message')
        print("Published msg -> 'super-duper-message' on Topic -> 'messages'")
       

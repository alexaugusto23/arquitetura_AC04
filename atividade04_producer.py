#!/usr/bin/env python
import pika
from pika import connection
from pika import channel
from get_time import data_atual, tempo_atual

#pip install pika

url = 'amqps://kyiirjzl:Ttd_gMalcqGWy92iOk8_dEe6PvEdWr4V@fish.rmq.cloudamqp.com/kyiirjzl'
parametros = pika.URLParameters(url)
connection = pika.BlockingConnection(parametros)
channel = connection.channel()
channel.queue_declare(queue='Queue_Data')

messagem = "Data e Hora:\n" + data_atual + "\n" + tempo_atual

channel.basic_publish(exchange='',
                      routing_key='Queue_Data',
                      body=messagem)
print("Data Enviada!'")


connection.close()
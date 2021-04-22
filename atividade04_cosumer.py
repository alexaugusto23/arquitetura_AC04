#!/usr/bin/env python
import pika, sys, os
from pika import connection
from pika import channel
#pip install pika

def main():

    url = 'amqps://kyiirjzl:Ttd_gMalcqGWy92iOk8_dEe6PvEdWr4V@fish.rmq.cloudamqp.com/kyiirjzl'
    parametros = pika.URLParameters(url)
    connection = pika.BlockingConnection(parametros)
    channel = connection.channel()
    channel.queue_declare(queue='Semaforo_Queue')


    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='Semaforo_Queue',
                        auto_ack=True,
                        on_message_callback=callback)

    channel.basic_consume(queue='Semaforo_Queue', 
                        on_message_callback=callback, 
                        auto_ack=True)


    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrompido')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
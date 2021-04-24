#!/usr/bin/env python
import pika, sys, os
from pika import connection
from pika import channel

#pip install pika
#Usar um terminal no cmd para enviar as mensagem pelo programa producer
# e deixar o programa consumer rodando em outro terminal a parte para 
# ver as mensagens recebidas.

def main():

    url = 'amqps://kyiirjzl:Ttd_gMalcqGWy92iOk8_dEe6PvEdWr4V@fish.rmq.cloudamqp.com/kyiirjzl'
    parametros = pika.URLParameters(url)
    connection = pika.BlockingConnection(parametros)
    channel = connection.channel()
    channel.queue_declare(queue='Queue_Data')


    def callback(ch, method, properties, body):
        print(body.decode())

    channel.basic_consume(queue='Queue_Data',
                        auto_ack=True,
                        on_message_callback=callback)

    channel.start_consuming()
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrompido pelo Usuário Crtl+C')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
import pika
from pika import connection
from pika import channel
#pip install pika

url = 'amqps://kyiirjzl:Ttd_gMalcqGWy92iOk8_dEe6PvEdWr4V@fish.rmq.cloudamqp.com/kyiirjzl'
parametros = pika.URLParameters(url)
connection = pika.BlockingConnection(parametros)
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print("[x] Recebido %r" %(body))

channel.basic_consume(callback,)
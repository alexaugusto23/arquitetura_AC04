import pika
from pika import connection
from pika import channel
#pip install pika

url = 'amqps://kyiirjzl:Ttd_gMalcqGWy92iOk8_dEe6PvEdWr4V@fish.rmq.cloudamqp.com/kyiirjzl'
parametros = pika.URLParameters(url)
connection = pika.BlockingConnection(parametros)
channel = connection.channel()
channel.queue_declare(queue='Semaforo_Queue')

channel.basic_publish(exchange='',
                      routing_key='Semaforo_Queue',
                      body='Hello World!')
print(" [x] Enviado 'Hello World!'")

connection.close()
# Pesquise sobre middleware de comunicação 
# orientada a mensageria, também conhecido 
# como Broker. Descreva o funcionamento do 
# broker RabbitMQ.


# Oque são middleware de mensagens ou Brokers:
'''
è um sistema que promove serviços e 
recursos entre aplicações, por isso o 
nome de middleware, pois ele faz o intermédio 
entre os sistemas.
'''

#Protocolo de Comunicação:
'''
Tem como objetivo promover um padrão 
de comunicação entre as aplicações 
promovendo a integração entre as diversas
tecnologias. 
Um dos protocolos utilizados é o AMQP: 
Advanced Message Queuing Protocol, é um 
protocolo especifico para comunicação baseada 
em mensagens.
'''

#Como funciona o Message broker RabbitMQ:
'''
O Message broker funciona no padrão Publish e Subscriber (Publicador e Subscritor), 
Producer e Consumer (Produtor e Consumidor). Entre esse
dois personagens temos o broker RabbitMQ que faz o 
exchange (troca) paras as routes(rotas) das queue (Filas).
Ou seja Produto -> Envia Mensagem -> Broker Seleciona rota
-> coloca na fila -> Consumidor recebe a mensagem.
Ele garante que uma mensagem (evento) seja recebido, enfileirado
e armazenado para que seja consumido pelo seu consumidor.

Estrutura do Message Brokers:
Exchange
Queues
Producers
Consumers
Bindings
AMQP 
'''
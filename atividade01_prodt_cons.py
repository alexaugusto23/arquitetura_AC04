# Escreva uma versão produtor consumidor multiprocessos. 

from threading import Thread, Condition
import time
import random

fila = []
condicao = Condition()

class Produtor(Thread):
    def run(self):
        nums = range(5)
        global fila
        while True:
            num = random.choice(nums)
            condicao.acquire()
            fila.append(num)
            print("Produzido", num)
            condicao.notify()
            condicao.release()
            time.sleep(random.random())

class Consumidor(Thread):
    def run(self):
        global fila
        while True:
            condicao.acquire()
            if not fila:
                print("Fila vazia, consumidor aguardando ...")
                condicao.wait()
                print("Produtor incluiu algum elemento na fila..")
            num = fila.pop(0)
            print("Consumido", num)
            condicao.release()
            time.sleep(random.random())


Produtor().start()
Consumidor().start()
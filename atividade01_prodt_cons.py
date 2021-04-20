# Escreva uma versão produtor consumidor multiprocessos. 

from threading import Thread, Condition
import time
import random

condicao = Condition()
fila_semafaro = []
contador = 0

class Produtor(Thread):
    global fila_semafaro
    def run(self):
            valor = '\033[7;30;42mVerde\033[m'
            condicao.acquire()
            fila_semafaro.append(valor)
            print(fila_semafaro[0])
            condicao.notify()
            condicao.release()
            time.sleep(3)

            valor = '\033[7;30;43mAmarelo\033[m'
            condicao.acquire()
            print()
            condicao.notify()
            condicao.release()
            time.sleep(2)

            valor = '\033[7;30;41mVermelho\033[m'
            condicao.acquire()
            print()
            condicao.notify()
            condicao.release()
            time.sleep(3)
           
            return

class Consumidor(Thread):
    def run(self):

            return

if __name__ == '__main__':
    Produtor().start()
    Consumidor().start()



'''
fila = []
condicao = Condition()

Produtor 
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

Consuumidor
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


'''
# \033[style:text:backm
# style: 0 none, 1 bold, 4 undeline, 7 negative
# text: 30 white, 31 red, 32 green, 33 yellow, 34 blue, 35 purple, 36 cyan , 37 gray
# back: 40 white, 41 red, 42 green, 43 yellow, 44 blue, 45 purple, 46 cyan , 47 gray
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
            print(f"Produzindo: {fila_semafaro[0]}")
            print(f"Status da Fila: {fila_semafaro}")
            condicao.notify()
            condicao.release()
            time.sleep(3)

            valor = '\033[7;30;43mAmarelo\033[m'
            condicao.acquire()
            fila_semafaro.append(valor)
            print(f"Produzindo: {fila_semafaro[0]}")
            print(f"Status da Fila: {fila_semafaro}")
            condicao.notify()
            condicao.release()
            time.sleep(2)

            valor = '\033[7;30;41mVermelho\033[m'
            condicao.acquire()
            fila_semafaro.append(valor)
            print(f"Produzindo: {fila_semafaro[0]}")
            print(f"Status da Fila: {fila_semafaro}")
            condicao.notify()
            condicao.release()
            time.sleep(3)

            print(f"Fila Consumida: {fila_semafaro}")
           
            return

class Consumidor(Thread):
    def run(self):
        while True:
            condicao.acquire(3)
            if not fila_semafaro:
                print("Fila vazia, consumidor aguardando ...")
                condicao.wait()
                print("Produtor incluiu algum elemento na fila..")
            
            print(f"Consumindo: {fila_semafaro.pop()}")
            print(f"Status da Fila: {fila_semafaro}")
            
            condicao.wait()
            print(f"Consumindo: {fila_semafaro.pop()}")
            print(f"Status da Fila: {fila_semafaro}")
            condicao.release()

            condicao.acquire()
            condicao.wait()
            print(f"Consumindo: {fila_semafaro.pop()}")
            print(f"Status da Fila: {fila_semafaro}")
            print(f"Pode atraversar !!!")
            condicao.release()

            return

if __name__ == '__main__':
    Produtor().start()
    Consumidor().start()

'''
# \033[style:text:backm
# style: 0 none, 1 bold, 4 undeline, 7 negative
# text: 30 white, 31 red, 32 green, 33 yellow, 34 blue, 35 purple, 36 cyan , 37 gray
# back: 40 white, 41 red, 42 green, 43 yellow, 44 blue, 45 purple, 46 cyan , 47 gray
'''
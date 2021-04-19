# Escreva uma versão multithreads para calcular a primalidade 
# de vários números. Após isso, compare o tempo de execução 
# da sua solução com a solução multiprocessos apresentada na 
# sala de aula.

from multiprocessing import Pool
import time # outra biblioteca com maior precisão testes de tempo de execução: import timeit
from unittest import TestCase, main


# Versão Primalidade Professor
def eh_primo(n):
    for i in range(3, int(n**0.5+1), 2):
            if n % i == 0:
                print(n, ' nao eh primo')
                return False
    print(n, ' eh primo')
    return True


# Minha Versão Primalidade
def ehPrimo_minha_versao(num):
    for divisor in range(2, num):
        if num % divisor == 0:
            print(num, ' não eh primo')
            return False
    if num < 2:
            print(num, 'não eh primo')
            return False
    print(num, ' eh primo')
    return True


class MyTestCase(TestCase):

    def test_valores_nulos(self):
        result = numeros
        self.assertIsNotNone(result)


if __name__ == '__main__':   

    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13] 
    pool = Pool()
    
    print("Execução 01")
    print()
    time.sleep(3)
    inicio_A = time.time()
    pool.map(eh_primo, numeros)
    fim_A = time.time()
    tempo_execucao_A = fim_A - inicio_A
    tempo_execucao_A = tempo_execucao_A * 1000
    
    time.sleep(1)

    print("\nExecução 02")
    print()
    time.sleep(3)
    inicio_B = time.time()
    pool.map(ehPrimo_minha_versao, numeros)
    fim_B = time.time()
    tempo_execucao_B = fim_B - inicio_B
    tempo_execucao_B = tempo_execucao_B * 1000

    print()
    print(f"tempo de execução A: {tempo_execucao_A} ms")
    print(f"tempo de execução B: {tempo_execucao_B} ms")

    with open('tempo_de_execucao.txt', "w", encoding="utf-8") as file:
            file.write(f"tempo de execução A: {tempo_execucao_A} ms\n")
            file.write(f"tempo de execução B: {tempo_execucao_B} ms")
            file.close()

    print("Executando testes")
    print()
    main()
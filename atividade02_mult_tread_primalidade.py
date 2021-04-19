# Escreva uma versão multithreads para calcular a primalidade 
# de vários números. Após isso, compare o tempo de execução 
# da sua solução com a solução multiprocessos apresentada na 
# sala de aula.

from multiprocessing import Pool

def eh_primo(n):
    for i in range(3, int(n**0.5+1), 2):
            if n % i == 0:
                print(n, ' nao eh primo')
                return False
    print(n, ' eh primo')
    return True

if __name__ == '__main__':
    numeros = [1297337] * 100
    pool = Pool()
    pool.map(eh_primo, numeros)
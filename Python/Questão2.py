""" Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""



def sequenciafib(n):

    fib_seq = [0, 1]
    while len(fib_seq) < n:
        next_value = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_value)
    return fib_seq

def pertencente(num):
    #verifica o pertencente

    fib_seq = sequenciafib(20)
    return num in fib_seq

# InPUT
numero = int(input("Informe um número: "))

# Verificacão:
if pertencente(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
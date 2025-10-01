import time


def buscaBinaria(x, lista):
    esquerda = 0
    direita = len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda+direita)//2
        if x == lista[meio]:
            return True
        elif x > lista[meio]:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return False

def intersecao(A, B):

    if len(A) > len(B): #fazer sempre com o menor vetor como referencia
        return intersecao(B,A)
    
    if len(A) == 0: #caso infantil
        return []
    
    meio = len(A)//2
    elem = A[meio]

    res = []

    if buscaBinaria (elem, B): #se o elemento está em B
        res.append(elem)
        
    esquerda = intersecao(A[:meio], B) #recursiva pros elementos da esquerda
    direita = intersecao(A[meio+1:], B) #recursiva pros elementos da direita

    return esquerda + res + direita


t_inicio = time.time()
print(intersecao([1,2,7,8,10,11,12,13,14,15,16,17,18], [1,2,3,4,6,7,8,9]))
print(round((time.time() - t_inicio),5))

import time

def mergeSort(lista): 

    #timeI = time.time() #tempo inicial do merge

    if len(lista) <=1:
        return lista
    
    meio = len(lista)//2
    
    esq = mergeSort(lista[:meio])
    dir = mergeSort(lista[meio:])

    i=j=k=0
    while i<len(esq) and j<len(dir): 
        if esq[i][1] < dir[j][1]: #ordenando pelo fim para pegar atividades curtas primeiro
            lista[k] = esq[i]
            i += 1
        else:
            lista[k] = dir[j]
            j += 1
        k += 1
    while i<len(esq):
        lista[k] = esq[i]
        i += 1
        k += 1
    while j<len(dir):
        lista[k] = dir[j]
        j += 1
        k += 1
    
    #timeF = time.time() #tempo final do merge
    #print('tempo de ordenação: ', timeF-timeI)
    return lista

def atv_comp(atividades):
    
    timeI = time.time()
     
    atividades = mergeSort(atividades)

    melhor = []

    def backtrack(i, ultFim, atual):
        #timeI2 = time.time() #tempo inicial da recursao

        nonlocal melhor #atualiza a lista com as melhores ops

        if i == len(atividades): #caso base, acabou a lista
            if len(atual) > len(melhor): #cabe mais atividades, atualiza melhor
                melhor = atual[:] #O(n), lista toda
            return
        
        inicio, fim = atividades[i]

        if inicio >= ultFim: #ultFim = fim da ultima atividade add
            atual.append((inicio,fim))
            backtrack(i+1, fim, atual) #recursao com a proxima atividade
            atual.pop() #tenta outra possb
        
        backtrack(i+1, ultFim, atual) #recursao sem incluir atv i
        #timeF2 = time.time() #tempo final da recursao 
        #print('tempo da recursao: ', timeF2-timeI2) 

    backtrack(0, 0, []) #primeiro i e com ultFim=0 para inicio sempre >ultFim

    timeF = time.time()

    print('tempo do algoritmo: ', timeF-timeI)
    return melhor


atividades =  [(15,17),(10,13),(7,12), (11,12), (5,8),(18,20),(17,19),(9,14),(12,17),(13,15)]
print('Atividades escolhidas (Backtrack): ', atv_comp(atividades))

'''comentei os times porque, por conta da recursao, acabam ficando muitos prints. 
mentive somente o final, que engloba todo o algoritmo. mas caso queira ver cada parte, 
só tirar o comentário. '''

        

        


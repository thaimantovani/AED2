import time

def atividades_compativeis(x, y):
    inicio = x[:]
    fim = y[:]

    n = len(inicio)

    for i in range(0,n):
        menor = i
        for j in range(i + 1, n):
            if fim[j] < fim[menor]:
                menor = j
        temp = fim[i]
        fim[i] = fim[menor]
        fim[menor] = temp
        
        temp2 = inicio[i]
        inicio[i] = inicio[menor]
        inicio[menor] = temp2

    max_atividade = [1] * n
    max_indice = [-1] * n

    for i in range(1, n):
        for j in range(0,i):
            if fim[j] <= inicio[i]:
                if max_atividade[j] + 1 > max_atividade[i]:
                    max_atividade[i] = max_atividade[j] + 1
                    max_indice[i] = j

    melhor_valor = max_atividade[0]
    melhor_indice = 0

    for i in range(1, n):
        if max_atividade[i] > melhor_valor:
            melhor_valor = max_atividade[i]
            melhor_indice = i

    escolhidas_inicio = []
    escolhidas_fim = []

    k = melhor_indice
    while k != -1:
        escolhidas_inicio.insert(0, inicio[k])
        escolhidas_fim.insert(0, fim[k])
        k = max_indice[k]

    return melhor_valor, escolhidas_inicio, escolhidas_fim

t_inicio = time.time()
inicio = [1, 3, 0, 5, 8, 5]
fim    = [2, 4, 6, 7, 9, 9]

resulatdo = 0
esc_i = 0
esc_f = 0

resultado, esc_i, esc_f = atividades_compativeis(inicio, fim)

print("Máximo de atividades compatíveis:", resultado)
print("\nAtividades escolhidas:")
for i in range(0,len(esc_i)):
    print(esc_i[i], "até", esc_f[i])

print("\nTempo total:", round((time.time() - t_inicio),5), "segundos")

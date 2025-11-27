import time 

atividades = [(15,17),(10,13),(7,12), (11,12), (5,8),
              (18,20),(17,19),(9,14),(12,17),(13,15)]

def ordenar_por_fim(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[j][1] < lista[i][1]:
                lista[i], lista[j] = lista[j], lista[i]

inicio_tempo = time.time()
ordenar_por_fim(atividades)

atividades_escolhidas = []
ultimo_fim = -1

for inicio, fim in atividades:
    if inicio >= ultimo_fim:
        atividades_escolhidas.append((inicio, fim))
        ultimo_fim = fim

fim_tempo= time.time()
tempo_total = fim_tempo - inicio_tempo

print("Atividades escolhidas (Guloso):", atividades_escolhidas)
print(tempo_total)


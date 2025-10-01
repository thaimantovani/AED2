import time
# Implementação Bottom-up
def cortebastao(precos, n):
    # maiores_vals[i] = valor máximo para uma barra de tamanho i
    maiores_vals = [0] * (n + 1)   # O(n)
    # melhores_cortes[i] = melhor tamanho do primeiro pedaço para barra i
    melhores_cortes = [0] * (n + 1)  # O(n)

    # Preenche de 1 até n nos vetores maiores_vals e melhores_cortes
    for i in range(1, n + 1):  
        max_val = float('-inf')  
        melhor_corte = 0         
        for j in range(1, i + 1):  
            if j <= len(precos): 
                if precos[j - 1] + maiores_vals[i - j] > max_val:  
                    max_val = precos[j - 1] + maiores_vals[i - j]  
                    melhor_corte = j  
        maiores_vals[i] = max_val       
        melhores_cortes[i] = melhor_corte  

    # Reconstruindo
    cortes_feitos = []                
    comprimento = n             
    while comprimento > 0:      
        cortes_feitos.append(melhores_cortes[comprimento])  
        comprimento -= melhores_cortes[comprimento]  

    return maiores_vals[n], cortes_feitos        

# Exemplo de entrada
t_inicio = time.time()
precos = [1, 5, 8, 9, 10, 17, 17, 20]  
n = int(input("Digite o comprimento da barra desejada em metros: "))  
valor, cortes = cortebastao(precos, n)  

print("Valor máximo:", valor)   
print("Cortes feitos:", cortes) 
print(round((time.time() - t_inicio),5))
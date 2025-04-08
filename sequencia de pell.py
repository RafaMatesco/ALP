n = int(input("Digite o n-esimo termo da sequencia de Pell:"))

pFuturo = 0
pAnterior = 0
pAtual = 1
sequenciaPell = [] # não é necessária essa lista, mas para imprimir depois fica melhor

for x in range(0, n):
    sequenciaPell.append(pAnterior)
    
    pFuturo = (2*pAtual) + pAnterior
    pAnterior = pAtual
    pAtual = pFuturo
    
    
print(sequenciaPell)
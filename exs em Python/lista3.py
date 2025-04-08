#EX 1 ========================================================
while True:
    nota = int(input("Digite a nota: "))
    if nota < 0 or nota > 10:
        print("Nota inválida")
    else:
        break
print("Nota válida")


#EX 2 ==========================================================
while True:
    nome = str(input('Digite seu nome: '))
    senha = str(input('Digite sua senha: '))

    if nome == senha:
        print('Nome e senha iguais, digite novamente')
    else:
        break

#EX 3 ========================================================== 
popA = 80000
popB = 200000
anos = 0

while True:
    popA = popA + (popA * 0.03)
    popB = popB + (popB * 0.015)
    print(popA, popB)
    anos = anos + 1
    if popA >= popB:
        break
    
print('Anos que se passaram até população A ultrapassar a população B: ', anos)

#EX 4 ========================================================== 
valorAnterior = 0
valorAtual = 1
valorProx = 0

numeroF = int(input('Digite o numero para encontrar sua posição no fibonacci: '))

for x in range(0,numeroF):
    valorProx = valorAtual + valorAnterior
    valorAnterior = valorAtual
    valorAtual = valorProx

    print(f'F{x}: {valorAtual}')
    
#EX 5 ========================================================== 
a = int(input())
b = int(input())
maior = max(a,b)
menor = min(a,b)

resto = maior % menor

if resto == 0:
    MDC = menor
else:
    while True:
        maior = menor
        menor = resto
        resto = maior % menor
        if resto == 0:
            MDC = menor
            break
            
print(f"MDC entre {a} e {b} é {MDC}")
            
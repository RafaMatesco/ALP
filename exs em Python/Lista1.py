#EXERCÍCIO 1==================================================================================
a = int(input('primeiro numero:'))
b = int(input('segundo numero:'))
print(f'soma dos numeros: {a+b}')
input()

#EXERCICIO 2==================================================================================
metros = float(input('Digite um valor em metros: '))
print(f'Valor convertido em milimetros: {metros * 1000:.2f}')
input()

#EXERCICIO 3==================================================================================
dias = int(input('dias: '))
horas = int(input('horas: '))
minutos = int(input('minutos: '))
segundos = int(input('segundos: '))

segundosTotal = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
print(f'Total de segundos: {segundosTotal}')

#EXERCICIO 4==================================================================================
salario = float(input('Digite o salario: '))
porcAumento = float(input('Digite o a porcentagem de aumento: '))
aumento = salario * porcAumento/100
salarioNovo = salario + aumento
print(f'Aumento: {aumento}')
print(f'Salario com aumento: {salarioNovo}')

#EXERCICIO 5==================================================================================
preco = float(input('Preco mercadoria: '))
desconto = float(input('Percentual desconto: '))
valorDescontado = preco * desconto/100
precoNovo = preco - valorDescontado
print(f'Valor descontado: {valorDescontado}')
print(f'Preco com desconto: {precoNovo}')

#EXERCICIO 6==================================================================================
distancia = int(input('Distância percorrida (Km): '))
velocidade = int(input('Velocidade média(Km/H): '))

tempo = distancia / velocidade
print(f'Tempo total de viagem: {tempo} horas')

#EXERCICIO 7==================================================================================
celsius = float(input("Digite a temperatura em celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("A temperatura em fahrenheit é:", fahrenheit)
input()

#EXERCICIO 8==================================================================================
fahrenheit = float(input("Digite a temperatura em fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print("A temperatura em celsius é:", celsius)
input()

#EXERCICIO 9==================================================================================
kms = float(input("Digite a quantidade de quilômetros: "))
diasAlugado = float(input("Digite a quantidade de dias que o aluguel durou: "))

preco = (kms * 0.15) + (diasAlugado * 60)

print("O preço total a ser pago é de R$", preco)
input()

#EXERCICIO 10==================================================================================
cigarrosPorDia = int(input("Quantos cigarros você fuma por dia? "))
anosFumando = int(input("Há quantos anos você fuma? "))

diasFumados = anosFumando * 365
cigarrosFumados = diasFumados * cigarrosPorDia

minutosPerdidos = cigarrosFumados * 10
diasPerdidos = minutosPerdidos / 1440 
#1440 por que divide os minutos por 60 e depois por 24

print(f"Você perdeu {diasPerdidos:.1f} dias de vida")
input()

#EXERCICIO 11==================================================================================
#o python tem um limite de digitos que só da pra ser ultrapassado se usar a biblioteca sys
#se não fizer isso o código dá erro
import sys
sys.set_int_max_str_digits(1000000)

print(len(str(2**1000000)))
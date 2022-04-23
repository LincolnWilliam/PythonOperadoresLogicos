# Calculo IMC , com operador logigo 'and'
# Leia README.md

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print('você está em estado de Magreza. ')

elif imc > 18.5 and imc <= 24.9:
    print('sua imc está normal. ')

elif imc >= 25 and imc <= 29.9:
    print('você está em estado de sobrepeso. ')

elif imc >= 30 and imc <= 39.9:
    print('você está em estado de Obesidade ')

elif imc >= 40:
    print (' seu estado é Obesidade grave.')
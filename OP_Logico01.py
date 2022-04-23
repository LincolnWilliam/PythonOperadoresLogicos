# Informe se o triangulo é, Esquilatero, Isósceles, Escanelo.

valor = int(input("Digite um valor: "))
valor2  = int(input("Digite um segundo valor: "))
valor3  = int(input("Digite um terceiro valor: "))

if (valor == valor2) and (valor == valor3):
    print('Seu triangulo é Equilatero')

elif (valor == valor2) or (valor == valor3) or (valor2 == valor3):
    print('Seu triangulo é Isósceles')

else:
    print('Seu triangulo é Escaleno') 
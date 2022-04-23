# informe o desconto de acordo com a idade.
idade = int(input('Digite a idade:'))

if idade < 12:
    print('você tem 100% de desconto')

elif idade >=12 and idade < 17:
    print('você tem 50% de desconto')

elif idade >=17 and idade < 22:
    print('você tem 25% de desconto')

else:
    print('você não tem desconto')
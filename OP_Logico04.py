# LER TRÊS NOTAS E FAZER A MÉDIA:
# Leia README.md
nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
nota3 = float(input('digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
print (media)
if media >= 9:
    print('você foi aprovado com louvor')

elif media >= 7 and media < 9:
    print('você foi aprovado')

elif media >= 4 and media < 7:
    print('você está de recuperação')

else:
    print('você está reprovado direto\nsem direito a recuperação')
# Selecionar a Área que o torcedor ira sentar.
# leia README.md
categoria = int(input('digite  o codigo da categoria: '
                      '1-professor, '
                      '2-estudante, '
                      '3-pcd, ' 
                      '4-nenhuma : '))
salario = float(input('digite seu salario: '))
idade = int(input('digite sua idade: '))

if categoria == 3 or salario > 3000 or idade == 60:
    print('voce vai para área vip')
elif categoria == 1 or categoria == 2 or salario <= 2000:
    print ('você vai para o camarote.')

else:
    print('você ira para pista')
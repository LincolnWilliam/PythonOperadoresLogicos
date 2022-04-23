# Retorna o periodo do dia de acordo com a hora informada.

hora = int(input('digite a hora: '))
if hora >= 6 and hora <= 11:
    print('bom dia')
elif hora >= 12 and hora <= 17:
    print('boa tarde')

elif hora >= 18 and hora <= 23:
    print('boa noite')
else:
    print('boa madrugada')
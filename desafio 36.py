casa = float(input('O valor da casa? : '))
salario = float(input('O seu salario? : '))
tempo = float(input('Em quantos anos você vai pagar?:'))
meses = float(tempo * 12)
prestação = casa / meses
trinta = salario/ 100 * 30
if prestação >trinta:
    print('O seu emprestimo não foi aprovado')
else:
    print('Você vai pagar R${} por mes, durante {} meses'.format(prestação, meses))
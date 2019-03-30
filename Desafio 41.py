ano = int(input('Infome o seu ano de nascimento: '))
idade = 2019 - ano
print('Você tem {} anos de Idade, Sua categoria é:'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SêNIOR')
elif idade > 20:
    print('MASTER')
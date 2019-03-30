n1 = float(input('Informe a primeira Nota: '))
n2 = float(input('Informe a segunda Nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('REPROVADO')
    print('Sua media é: {}'.format(media))
elif 5.0 < media < 6.9:
    print('RECUPERAÇÂO')
    print('Sua media é: {}'.format(media))
elif media > 7.0:
    print('APROVADO')
    print('Sua media é: {}'.format(media))
print('*-'*20)
ano = int(input('Informe o seu ano de nascimento: '))
tempo = str(18 - (2019 - ano))
if (2019 - ano) < 18:
    print('Você tem que se alistar em {} anos'.format(tempo))
elif (2019 - ano) == 18:
    print('Você tem que se alistar agora.')
elif (2019 - ano) > 18:
    print('Ja passou da da hora de se alistar, passou {} anos.'.format(tempo[1:]))
n1 = int(input('Digite o primeiro numero= '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('O primeoro valor e maior que o segundo')
elif n1 < n2:
    print('O segundo valor e maior que o primeiro')
elif n1 == n2:
    print('Não existe valor maior, ambos são iguais')
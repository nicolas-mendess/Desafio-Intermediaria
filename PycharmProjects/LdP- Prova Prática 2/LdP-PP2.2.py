ct = 0
soma = 0
media = 0
quantidade = 0

print('Digite [-1] para sair da repetição')
while True:
    n = int(input("Digite um número: "))
    if  n == -1 :
        break
    ct = ct + 1
    soma = soma + n
    media = soma / ct
    if n > 20:
        quantidade = quantidade + 1

print('\nQuantidade de valores digitados:', ct)
print("A soma dos valores digitados:", soma)
print("A média aritmética dos valores digitados:",media)
print("A quantidade de valores digitados maior que 20:", quantidade)

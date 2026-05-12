ct = 0
soma = 0
soma_par = 0
soma_impar = 0
ct_impar = 0
ct_par = 0

print('Digite zero [0] para sair')

while True:
    entrada = int(input("Número inteiro: "))

    if entrada == 0:
        break
    ct = ct + 1
    soma = soma + entrada

    if entrada % 2 == 0:

        soma_par = soma_par + entrada
        ct_par = ct_par + 1
        media_par = soma_par / ct_par
    else:
        soma_impar = soma_impar + entrada
        ct_impar = ct_impar + 1
        media_impar = soma_impar / ct_impar

print("\nA média de todos os pares é:", media_par)
print('A média de todos os ímpares é:', media_impar)
print("A quantidade total de números digitados", ct)
print("A soma total de números digitados:", soma)
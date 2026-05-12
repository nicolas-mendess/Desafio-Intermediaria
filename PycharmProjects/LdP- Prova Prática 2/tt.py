contagem_total = 0
soma_total = 0
soma_par = 0
soma_impar = 0
contagem_par = 0
contagem_impar = 0

print('Digite zero [0] para sair.')

while True:
    entrada = int(input("Número inteiro: "))

    if entrada == 0:
        break


    contagem_total = contagem_total + 1
    soma_total = soma_total + 1

    if entrada % 2 == 0:
        soma_par += entrada
        contagem_par += 1
    else:  # Número ímpar
        soma_impar += entrada
        contagem_impar += 1

media_par = soma_par / contagem_par if contagem_par > 0 else 0
media_impar = soma_impar / contagem_impar if contagem_impar > 0 else 0

print("Média dos números pares:", media_par)
print("Média dos números ímpares:", media_impar)
print("Quantidade total de números digitados:", contagem_total)
print("Soma total de números digitados:", soma_total)
salario_minimo = float(input("Digite o valor do salário mínimo: "))
salario_funcionario = 0
menos_cinco = 0
cinco_dez = 0
mais_dez = 0
soma = 0

print('Digite [0] para sair da repetição')
while True:
    n = int(input("Digite o Salario do funcionario: "))
    if  n == 0 :
        break

    soma += n

    if n < 5 * salario_minimo:
        menos_cinco += 1
    elif 5 * salario_minimo <= n < 10 * salario_minimo:
        cinco_dez += 1
    else:
        mais_dez += 1

print('\nQuantidade de funcionarios com menos que cinco salários mínimos:',menos_cinco)
print("Funcionarios na faixa de cinco até dez salários mínimos:", cinco_dez)
print("Funcionarios que ganham dez ou mais salários mínimos:", mais_dez)
print("O valor total da folha de pagamento da empresa:", soma)


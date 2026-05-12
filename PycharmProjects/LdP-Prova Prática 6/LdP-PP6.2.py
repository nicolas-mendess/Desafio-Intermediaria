def fatorial(n):
    calculo = 1
    for i in range(1, n + 1):
        calculo = calculo * i  
    return calculo

if __name__ == '__main__':
    numero = int(input("Digite o numero:"))
    resultado = fatorial(numero)
    print("Resultado:", resultado)


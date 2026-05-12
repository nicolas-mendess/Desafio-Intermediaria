def soma(x, y):
    return x + y

def subtrai(x, y):  
    calculo = x - y
    return calculo

def multiplica(x, y):  
    return x * y

def divide(x, y):  
    return x / y


if __name__ == '__main__': 
    print("Calculadora")             
    v1 = int(input("Primeiro valor: "))  
    v2 = int(input("Segundo valor: "))
    opcao = int(input("\n[1] Somar\n[2] Subtrair\n[3] Multiplicar\n[4] Dividir\nOpção: "))
    if opcao == 1:              
        print('\nSoma =', soma(v1, v2))
    elif opcao == 2:
        print('\nSubtração =', subtrai(v1, v2))
    elif opcao == 3:
        print('\nMultiplicação =', multiplica(v1, v2))
    elif opcao == 4:
        print('\nDivisão =', divide(v1, v2))
    else:
        print('Opção inválida')             

# Use sua criatividade, elabore o problema (o enunciado) de um problema que usa função e resolva o problema proposto,
# ou seja, faça a implementação da função def e da função principal (main).
# Usa a função para que calcula dois numeros e uma operação digitados pelo usuario, e retorna o resultado. 
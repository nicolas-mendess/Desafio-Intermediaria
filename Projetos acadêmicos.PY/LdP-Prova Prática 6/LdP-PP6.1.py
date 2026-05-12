def soma(a, b):       
    somar = a + b     
    return somar      
def subtrai(a, b):    
    subtrair = a - b
    return subtrair
def multiplicacao(a, b):
    multiplicar = a * b
    return multiplicar
def divisao(a, b):
    dividir = a/b
    return dividir

if __name__ == '__main__':             
    num1 = int(input("Primeiro valor inteiro: ")) 
    num2 = int(input("Segundo valor inteiro: "))
    opcao = str(input(f"[+] Somar\n[-] Subtrair\n[*] Multiplicar\n[/] Dividir\nOpção "))     
    if opcao == '+':   
        print('Soma= ', soma(num1, num2))
    elif opcao == '-':      
        print('Subtração= ', subtrai(num1, num2))
    elif opcao == '-':      
        print('Multiplicação= ', multiplicacao(num1, num2))
    elif opcao == '/':      
        print('Dividir= ', divisao(num1, num2))
    else:
        print('Opção inválida')      

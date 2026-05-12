def main(mensagem, numero):
    return mensagem, numero

if __name__ == "__main__":
    mensagem = input("Digite a mensagem: ")
    numero = int(input("Digite o número: "))
    print( main(mensagem, numero) )

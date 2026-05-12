def main(ano_nascimento):
    idade = 2026 - ano_nascimento
    return idade

if __name__ == "__main__":
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    print(main(ano_nascimento))
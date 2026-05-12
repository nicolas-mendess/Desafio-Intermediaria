def main(x, y, z):
    return x + y + z

if __name__ == "__main__":
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    z = int(input("Digite o terceiro número: "))
    return_soma = main(x, y, z)
    print("\nSoma =", return_soma)
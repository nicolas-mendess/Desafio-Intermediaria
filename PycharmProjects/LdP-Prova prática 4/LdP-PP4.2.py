numero = int(input("Valor inicial:"))
ct = 0

for numeros in range (numero, 0, -1):
    print(numeros)
    ct = ct + 1
print("A quantidade de valores gerado na sequência: ",ct)
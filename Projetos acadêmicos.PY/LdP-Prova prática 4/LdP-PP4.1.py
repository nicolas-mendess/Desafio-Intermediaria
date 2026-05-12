numero = int(input("Numero final:"))
ct = 0

for numeros in range (1, numero+1, 1):
    print(numeros)
    ct = ct + 1
print("A quantidade de valores gerado na sequência: ",ct)
ct = 0
cont = 0
for numeros in range (1, 500 + 1, 1):
    if numeros == int(numeros):
        ct = ct + numeros
        cont = cont + 1
print(ct)
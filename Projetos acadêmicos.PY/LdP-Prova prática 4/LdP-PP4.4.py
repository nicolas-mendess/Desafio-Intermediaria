ct = 0
cont = 0
for numeros in range (1, 500 + 1, 1):
    if numeros % 2 != 0:
        if numeros % 3 == 0:
            ct = ct + numeros
print(ct)
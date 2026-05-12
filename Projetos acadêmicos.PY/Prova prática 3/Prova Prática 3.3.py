candidato1 = 0
candidato2 = 0
candidato3 = 0
voto_nulo = 0
voto_branco = 0



while True:
    voto = int(input("Vote 1, 2, 3, 4, 5, 6 ou 0 para sair:"))
    if voto == 0:
        break
    elif voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 5:
         voto_nulo += 1
    elif voto == 6:
         voto_branco += 1
vt = candidato1 + candidato2 + candidato3 + voto_branco + voto_nulo


percentual_nulo = (voto_nulo / vt * 100)
percentual_branco = (voto_branco/vt * 100)

print("\nTotal de votos candidato 1:", candidato1)
print("Total de votos candidato 2:", candidato2)
print("Total de votos candidato 3:", candidato3)
print("Total de votos nulos:", voto_nulo)
print("Total de votos em branco:", voto_branco)
print("Percentual de votos nulos:", percentual_nulo)
print("Percentual de votos em branco:", percentual_branco)
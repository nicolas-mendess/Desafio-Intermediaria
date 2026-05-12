ct = 0
soma = 0
aprovados = 0
reprovados = 0
print('Digite [-1] para sair')
while True:
    nota = float(input("Nota do aluno: "))
    if nota == -1:
        break
    ct = ct + 1
    soma = soma + nota
    media = soma / ct
    if nota >= 5:
        aprovados = aprovados + 1
    else:
        reprovados = reprovados + 1

print("\nMédia da turma:", media)
print('Quantidade de alunos:', ct)
print('Aprovados', aprovados)
print('Reprovados', reprovados)
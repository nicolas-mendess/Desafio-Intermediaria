# Fundamentos de Ciência de Dados - Avaliação Final

Para esta avaliação, vocês deverão utilizar o arquivo **'solucoes.py'**, presente dentro do repositório, ao abri-lo, irão perceber 3 funções correspondentes aos 3 exercícios, cada um deles **devem** ser elaborandos dentro daquela função **sem alterar seu nome**!

Ao realizarem o comando **git push**, será disparado um teste automático que verificará o resultado do seu código, caso o mesmo esteja correto e passe em todos os testes, estão aprovados! 

Cada LeetCode irá coresponder a **30 pontos** em um total de **90**, caso passem em todos os testes com pelo menos 2 códigos, estão **aprovados!**
---
# LeetCode 1 — Longest Word in Sentence

Dada uma frase, encontre **a palavra mais longa**.

Se houver empate, retorne **a primeira palavra mais longa encontrada**.

---

### Entrada

```
"Python é uma linguagem extremamente poderosa"
```

### Saída esperada

```
extremamente
```

---

### Regras

* as palavras são separadas por espaço
* ignore pontuação
* use `split()` para separar as palavras

---

### Estrutura

```python
def palavra_mais_longa(frase):
    pass
```

---

### Exemplo de execução

```python
frase = "programar em python é muito divertido"

print(palavra_mais_longa(frase))
```

Saída:

```
programar
```

---

# LeetCode 2 — Two Sum 

Dada uma lista de números e um **valor alvo**, encontre **dois números cuja soma seja igual ao alvo**.

Retorne **os índices desses números**.

---

### Entrada

```
nums = [2, 7, 11, 15]
target = 9
```

### Saída

```
[0, 1]
```

Explicação:

```
nums[0] + nums[1] = 2 + 7 = 9
```

---

### Estrutura

```python
def two_sum(nums, target):
    pass
```

---

### Dica

Use um **dicionário para armazenar números já vistos**.

Exemplo de ideia:

```
valor -> índice
```

---

### Exemplo de execução

```python
nums = [3, 2, 4]
target = 6

print(two_sum(nums, target))
```

Saída esperada:

```
[1, 2]
```

---

# LeetCode 3 — Valid Parentheses (versão simplificada)


Dada uma string contendo apenas:

```
( )
```

Verifique se os **parênteses estão balanceados**.

---

### Entrada

```
"(())"
```

### Saída

```
True
```

---

### Entrada

```
"(()"
```

### Saída

```
False
```

---

### Regras

* cada `(` precisa ter um `)`
* os parênteses devem fechar na ordem correta

---

### Estrutura

```python
def parenteses_validos(s):
    pass
```

---

### Dica

Você pode resolver usando apenas **um contador**:

```
(
aumenta contador
```

```
)
diminui contador
```

Se o contador ficar **negativo**, a sequência é inválida.

No final, o contador precisa ser **zero**.

---

### Exemplo

```python
print(parenteses_validos("(())"))
```

Saída:

```
True
```

---

Bons estudos! 🐍

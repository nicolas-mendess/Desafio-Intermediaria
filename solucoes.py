def palavra_mais_longa(frase):
    frase = frase.strip()
    palavra_mais_longa =""

    for palavra in frase.split():
        if len(palavra) > len(palavra_mais_longa):
            palavra_mais_longa = palavra

    return palavra_mais_longa

    pass

def two_sum(nums, target):
    prev_map = {} 

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i

    pass

def parenteses_validos(s):
    contador = 0
    
    for char in s:
        if char == '(':
            contador += 1
        elif char == ')':
            contador -= 1
        
        if contador < 0:
            return False
            
    return contador == 0
    pass
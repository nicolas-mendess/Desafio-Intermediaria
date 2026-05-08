import pytest

from solucoes import (
    palavra_mais_longa,
    two_sum,
    parenteses_validos
)


# leetcode 1
@pytest.mark.parametrize(
    "frase,resultado",
    [
        ("python é muito poderoso", "poderoso"),
        ("programar em python é divertido", "programar"),
        ("a bb ccc dddd", "dddd"),
        ("uma frase simples", "simples"),
        ("palavra mais longa", "palavra"),
        ("abc defg hij", "defg"),
        ("teste duas palavras iguais Aplausos", "palavras")
    ]
)
def test_palavra_mais_longa(frase, resultado):
    assert palavra_mais_longa(frase) == resultado

def test_palavra_mais_longa_empate():
    frase = "abc defg hij"
    assert palavra_mais_longa(frase) == "defg"

def test_palavra_mais_longa_tipo():
    resultado = palavra_mais_longa("teste simples")
    assert isinstance(resultado, str)


# leetcode 2
@pytest.mark.parametrize(
    "nums,target",
    [
        ([2,7,11,15], 9),
        ([3,2,4], 6),
        ([3,3], 6),
        ([1,5,8,10], 13),
    ]
)
def test_two_sum(nums, target):

    result = two_sum(nums, target)

    # tipo correto
    assert isinstance(result, list)

    # tamanho correto
    assert len(result) == 2

    i, j = result

    # indices inteiros
    assert isinstance(i, int)
    assert isinstance(j, int)

    # indices válidos
    assert 0 <= i < len(nums)
    assert 0 <= j < len(nums)

    # indices diferentes
    assert i != j

    # lógica correta
    assert nums[i] + nums[j] == target


# leetcode 3
@pytest.mark.parametrize(
    "entrada,resultado",
    [
        ("()", True),
        ("(())", True),
        ("((()))", True),
        ("(()())", True),
        ("(", False),
        (")(", False),
        ("(()", False),
        ("())", False),
        ("())(", False),
    ]
)
def test_parenteses_validos(entrada, resultado):
    assert parenteses_validos(entrada) == resultado

def test_parenteses_tipo():
    resultado = parenteses_validos("(())")
    assert isinstance(resultado, bool)


# robustez
def test_parenteses_string_grande():

    entrada = "(" * 50 + ")" * 50

    assert parenteses_validos(entrada) == True

def test_palavra_mais_longa_frase_grande():

    frase = "a bb ccc dddd eeeee ffffff ggggggg"

    assert palavra_mais_longa(frase) == "ggggggg"
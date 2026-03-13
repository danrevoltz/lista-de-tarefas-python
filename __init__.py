# This file is intentionally left empty to allow pytest to recognize the tests directory.
def palavra_mais_longa(frase):
    palavras = frase.split()
    maior = "a"
    for palavra in palavras:
        if len(palavra) > len(maior):
            maior = palavra
            return maior 
        frase = "Python é uma linguagem extremamente poderosa"
    print(palavra_mais_longa(frase))
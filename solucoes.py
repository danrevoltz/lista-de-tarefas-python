def palavra_mais_longa(frase):
    palavras = frase.split()
    maior = ""
    for palavra in palavras:
        if len(palavra) > len(maior):
            maior = palavra
            return maior 
        frase = "Python é uma linguagem extremamente poderosa"
    print(palavra_mais_longa(frase))

def two_sum(nums, target):
    vistos = {}
    for i, num in enumerate(nums):
        complemento = target - num
        if complemento in vistos:
            return (vistos[complemento], i)
        vistos[num] = i
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))

def parenteses_validos(s):
    contador  = 0
    for c in s:
        if c == '(':
            contador += 1
        else:
            contador -= 1
            if contador < 0:
                return False
    return contador == 0
print(parenteses_validos("()[]{}"))

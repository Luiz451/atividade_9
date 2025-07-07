def contar_vogais(palavra):
    vogais = "aeiou"
    contador = 0 
    for letra in palavra.lower():
        contador += 1
    return contador
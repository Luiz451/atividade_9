def palidromo(palavra):
    palavra_nova = palavra.replace(" ", "").lower()
    if palavra_nova == palavra:
        return True
    else:
        return False
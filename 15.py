def analisa_lista(lista):
    maximo = max(lista)
    minimo = min(lista)
    media = sum(lista) / len(lista)
    return {'maximo': maximo, 'minimo': minimo, 'media': media}
def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    if lista1 is None or lista2 is None:
        return None
    elif len(lista1) > len(lista2):
        return None
    else:
        tamanho = len(lista1)
    
    for i in range(tamanho):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    return lista_intercalada
def senha_segura(senha):
    '''
    Ter pelo menos 8 caracteres.


    Conter pelo menos uma letra maiúscula.


    Conter pelo menos uma letra minúscula.


    Conter pelo menos um número.
    '''
    if len(senha) < 8:
        return False
    if not any(c.isupper() for c in senha):
        return False
    if not any(c.islower() for c in senha):
        return False
    if not any(c.isdigit() for c in senha):
        return False
    else:
        return True
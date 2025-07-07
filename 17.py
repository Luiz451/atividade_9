import random
def simular_dado(n):
    faces = [1, 2, 3, 4, 5, 6]
    resultados = []
    for i in range(n):
        resultado = random.choice(faces)
        resultados.append(resultado)
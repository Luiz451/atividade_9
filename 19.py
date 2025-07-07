import random
def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    print("Bem-vindo ao jogo de adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")
    while True:
        palpite = input('Digite seu palpite ou "sair para encerrar o jogo: ')
        if palpite.lower() == "sair":
            print('Obrigado por jogar!')
            break
        if not palpite.isdigit():
            print("Por favor, digite um número válido ou 'sair' para encerrar o jogo.")
            continue
            palpite = int(palpite)
            tentativas += 1
            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
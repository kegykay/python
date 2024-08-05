import desenhos as d
from random import choice
import banco_dados


def jogar():
    lista_palavras = list()
    arquivo = open('projeto_jogoforca/words.txt', 'r')
    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)

    sorteada = choice(lista_palavras)

    for x in range(2):
        print()

    digitadas = []
    acertos = []
    leters = []
    erros = 0

    nome = input("Nome do jogador: ")

    print("   |-----¬")
    print("   |     :")
    print("   |")
    print("   |")
    print("   |")
    print("   |\n=======")

    while True:
        adivinha = d.imprimir_palavra_secreta(sorteada, acertos)

        # CONDIÇÃO DE VITÓRIA
        if (adivinha == sorteada):
            print("\nVocê acertou!".upper())
            print("parabéns :)\n".upper())
            break

        # TENTATIVAS
        tentativa = input("\nDigite uma letra: ").upper().strip()
        if (tentativa in digitadas):
            leters.append(tentativa)
            print("\nVocê já tentou esta letra!")
            print(f"Letras já utilizadas: {leters}\n")
            continue
        else:
            digitadas.append(tentativa)
            if (tentativa in sorteada.upper()):
                acertos.append(tentativa)
            else:
                erros += 1
                print("\nVocê errou!".upper())

        score = d.forca(erros)

        # CONDIÇÃO DE DERROTA
        if (erros == 6):
            print("\nVocê errou a palavra e morreu! xD")
            print(f"A palavra escolhida foi {sorteada}.")
            print("MAAASS, não fique para baixo, reinicie o jogo e vamos de novo!! :)\n")
            break

    banco_dados.inserir_dado(nome, score)

    
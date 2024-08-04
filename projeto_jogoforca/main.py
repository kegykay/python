import desenhos as d

# SOLICITA A PALAVRA QUE DEVE SER ADIVINHADA
palavra = input("\nDigite uma palavra secreta: ").upper().strip()

for x in range(100):
    print()

digitadas = []
acertos = []
erros = 0


print("   |-----¬")
print("   |     :")
print("   |")
print("   |")
print("   |")
print("   |\n=======")

while True:
    adivinha = d.imprimir_palavra_secreta(palavra, acertos)

    # CONDIÇÃO DE VITÓRIA
    if (adivinha == palavra):
        print("\nVocê acertou!".upper())
        print("parabéns :)\n".upper())
        break

    # TENTATIVAS
    tentativa = input("\nDigite uma letra: ").upper().strip()
    if (tentativa in digitadas):
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if (tentativa in palavra):
            acertos += tentativa
        else:
            erros += 1
            print("\nVocê errou!".upper())
            print("Não fique para baixo, reinicie o jogo e vamos de novo!! :)\n")

    d.forca(erros)

    # CONDIÇÃO DE DERROTA
    if (erros == 6):
        print("\nVocê errou a palavra e morreu! xD")
        print(f"A palavra escolhida foi {palavra}.\n")
        break


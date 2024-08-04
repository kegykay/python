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
    adivinha = ""
    for letra in palavra:
        if (letra in acertos):
            adivinha += letra
        else:
            adivinha += "\u0394"
    print(f"ADIVINHE ({len(palavra)} LETRAS): ")
    
    for letra in adivinha:
        print(f"{letra} ", end="")
    print()

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

    # DESENHANDO A FORCA
    print("   |-----¬")
    print("   |     :")
    if (erros >= 1):
        print("   |     O  ")
    else:
        print("   |")

    linha2 = ""
    if (erros == 2):
        linha2 = ("     |  ")
    elif (erros == 3):
        linha2 = ("    /|  ")
    elif (erros >= 4):
        linha2 = ("    /|\ ")
    print(f"   |{linha2}")

    linha3 = ""
    if (erros == 5):
        linha3 += ("    /  ")
    elif (erros >= 6):
        linha3 += ("    / \ ")
    print(f"   |{linha3}")
    print("   |\n=======")

    # CONDIÇÃO DE DERROTA
    if (erros == 6):
        print("\nVocê errou a palavra e morreu! xD")
        print(f"A palavra escolhida foi {palavra}.\n")
        break


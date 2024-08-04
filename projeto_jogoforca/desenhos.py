def imprimir_palavra_secreta(palavra, acertos):
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

    return adivinha

def forca(erros):
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
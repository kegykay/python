def imprimir_palavra_secreta(palavra, acertos):
    adivinha = ""
    for letra in palavra:
        if (letra.upper() in acertos):
            adivinha += letra
        else:
            adivinha += "_"
    print(f"ADIVINHE ({len(palavra)} LETRAS): ")
    
    for letra in adivinha:
        print(f"{letra} ", end="")
    print()

    return adivinha

def forca(erros):
    score = 1200
    print("   |-----¬")
    print("   |     :")
    if (erros >= 1):
        print("   |     O  ")
        score = 1000
    else:
        print("   |")

    linha2 = ""
    if (erros == 2):
        linha2 = ("     |  ")
        score = 800
    elif (erros == 3):
        linha2 = ("    /|  ")
        score = 600
    elif (erros >= 4):
        linha2 = ("    /|\ ")
        score = 400
    print(f"   |{linha2}")

    linha3 = ""
    if (erros == 5):
        linha3 += ("    /  ")
        score = 200
    elif (erros >= 6):
        linha3 += ("    / \ ")
        score = 0
    print(f"   |{linha3}")
    print("   |\n=======")


    return score
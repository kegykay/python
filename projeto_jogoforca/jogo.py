import main as m

def mostrar_menu():
    print("-"*30)
    print("|" + " "*8 + "JOGO DA FORCA" + " "*7 + "|")
    print("-"*30)
    print("|" + " "*9 + "1 - JOGAR" + " "*10 + "|")
    print("|" + " "*9 + "2 - SCORE" + " "*10 + "|")
    print("|" + " "*9 + "3 - SAIR" + " "*11 + "|")
    print("-"*30)


while True:
    mostrar_menu()
    
    opcao = int(input("Escolha a opção que deseja (1/2/3): "))

    if (opcao == 1):
        print("\nA PALAVRA FOI SORTEADA!!")
        print("COMEÇAR JOGO!!! :)\n")
        m.jogar()
        input("Digite qualquer tecla para continuar...")
    elif (opcao == 2):
        print("Mostrar Score")

    elif (opcao == 3):
        print("\nSaindo do Jogo.")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
        continue


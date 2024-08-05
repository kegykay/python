import main as m
import banco_dados

def mostrar_menu():
    print("-"*30)
    print("|" + " "*8 + "JOGO DA FORCA" + " "*7 + "|")
    print("-"*30)
    print("|" + " "*9 + "1 - JOGAR" + " "*10 + "|")
    print("|" + " "*9 + "2 - SCORE" + " "*10 + "|")
    print("|" + " "*9 + "3 - SAIR" + " "*11 + "|")
    print("-"*30)


while True:
    conn = banco_dados.conectar()
    banco_dados.criar_tabela(conn)
    mostrar_menu()
    
    opcao = int(input("Escolha a opção que deseja (1/2/3): "))

    if (opcao == 1):
        print("\nA PALAVRA FOI SORTEADA!!")
        print("COMEÇAR JOGO!!! :)")
        m.jogar()
        input("Digite qualquer tecla para continuar...\n")
    elif (opcao == 2):
        print("")
        print(" "*9 + "SCORE:")
        dados = banco_dados.listar_dados()
        if not (dados):
            print("Score vazio.")
        else:
            i = 1
            for player in dados:
                print(f"{i} -> {player[1]}, Pontuação: {player[2]}")
                i += 1

        input("Digite qualquer tecla para continuar...\n")

    elif (opcao == 3):
        print("\nSaindo do Jogo.")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
        continue

banco_dados.desconectar(conn)

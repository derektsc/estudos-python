import os

restaurantes = ["Derek's bar", "Prime Pizza"]

def exibir_nome_programa():
    print ('Sabor Express')

def exibir_opcoes():
    print ('1. Cadastrar restaurante')
    print ('2. Listar restaurante')
    print ('3. Ativar restaurante')
    print ('4. Sair\n')

def finalizar_app():
    exibir_subtitulo("Finalizando aplicação")

def back_menu():
    input("Digite uma tecla para voltar ao menu inicial")
    main()

def opcao_invalida():
    print("Opção invalida!")
    back_menu()

def cadastrar_restaurante():
    exibir_subtitulo("Cadastro de novas restaurantes \n")
    nome_do_restaurante = input("Digite o nome dor estaurante: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado na lista com sucesso!\n")
    try:
        input_number = int(input("Digite 1 para cadastrar um novo restaurante, ou 2 para voltar ao menu"))
        if input_number == 1:
            cadastrar_restaurante()
        elif input_number == 2:
            main()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes\n")
    #para cada restaurante na lista restaurantes mostrar o nome
    for restaurante in restaurantes:
        print(restaurante)
    back_menu()
    

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma Opção '))
        print(f'Voce escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
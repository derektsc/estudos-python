import os

#restaurantes = ["Derek's bar", "Prime Pizza"]
restaurantes = [{'nome': 'Prime Pizza', 'categoria': 'Pizzaria', 'ativo': False},
                {'nome': 'derek bar', 'categoria': 'bar', 'ativo': True }
                ]

def exibir_nome_programa():
    print ('Sabor Express')

def exibir_opcoes():
    print ('1. Cadastrar restaurante')
    print ('2. Listar restaurante')
    print ('3. Alternar estado do restaurante')
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
    categoria = input("Digite a categoria: ")
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
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
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f"{nome_restaurante} | {categoria} | {ativo}")
    back_menu()

def alternar_estado_restaurante():
    exibir_subtitulo("Restaurantes disponiveis: \n")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        print(f"{nome_restaurante}")
    restaurante_selecionado = input("Digite o nome do restaurante que deseja alternar estado: ")
    
    for restaurante in restaurantes:
        if restaurante_selecionado == restaurante['nome']:
            restaurante['ativo'] = not restaurante['ativo']
    print(f"Estado alternado com sucesso do restaurante {restaurante_selecionado}")

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
            alternar_estado_restaurante()
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
# Dupla: Enzo Onuma Bianconi e Henrique Dutra Siqueira

import os  # Usado para verificar se o arquivo de clientes existe


def cadastro_clientes():
    arquivo = "clientes.txt"  # Nome do arquivo onde os clientes ficam salvos

    def cadastrar_cliente():
        # Opção 1 do menu: cadastra um novo cliente no arquivo
        print(f"\n{'='*30}")
        print(f"{'CADASTRAR CLIENTE':^30}")
        print(f"{'='*30}")

    def listar_clientes():
        # Opção 2 do menu: lê o arquivo e mostra todos os clientes cadastrados
        print(f"\n{'='*30}")
        print(f"{'LISTAR CLIENTES':^30}")
        print(f"{'='*30}")    

    def alterar_cliente():
        # Opção 3 do menu: procura um cliente pelo nome e atualiza os dados
        print(f"\n{'='*30}")
        print(f"{'ALTERAR CLIENTE':^30}")
        print(f"{'='*30}")

    def excluir_cliente():
        # Opção 4 do menu: procura um cliente pelo nome e remove do arquivo
        print(f"\n{'='*30}")
        print(f"{'EXCLUIR CLIENTE':^30}")
        print(f"{'='*30}")

    # Menu principal: fica em execução até o usuário escolher voltar (0)
    while True:
        print(f"\n{'='*30}")
        print(f"{'SISTEMA DE CLIENTES':^30}")
        print(f"{'='*30}")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Alterar cliente")
        print("4 - Excluir cliente")
        print("0 - Voltar para o menu")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            alterar_cliente()
        elif opcao == "4":
            excluir_cliente()
        elif opcao == "0":
            break  # Sai do laço e a função é encerrada
        else:
            print("Opção inválida. Tente novamente.")

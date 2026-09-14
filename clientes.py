# Dupla: Enzo Onuma Bianconi e Henrique Dutra Siqueira

import os  # Usado para verificar se o arquivo de clientes existe


def cadastro_clientes():
    arquivo = "clientes.txt"  # Nome do arquivo onde os clientes ficam salvos

    # Caracteres aceitos no nome (letras, acentos e espaço)
    letras_nome = (
        "abcdefghijklmnopqrstuvwxyz"
        "áàâãéèêíïóôõöúçñ"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "ÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ "
    )

    # Caracteres aceitos na extensão do domínio do email (ex: com, br, org)
    letras_dominio = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def perguntar_sim_nao(pergunta):
        # Faz uma pergunta de sim/não e só aceita 's' ou 'n' como resposta
        while True:
            resposta = input(pergunta).strip().lower()
            if resposta == "s":
                return True
            elif resposta == "n":
                return False
            else:
                print("Valor inválido! Digite apenas 's' para sim ou 'n' para não.")

    def validar_nome():
        # Solicita e valida o nome: só letras/espaços, entre 2 e 60 caracteres
        while True:
            nome = " ".join(input("\nDigite o nome do cliente: ").split()) 

            nome_valido = True
            for letra in nome:
                if letra not in letras_nome:
                    nome_valido = False

            if nome == "":
                print("Valor inválido! O nome não pode ficar vazio.")
            elif not nome_valido:
                print("Valor inválido! Use apenas letras e espaços.")
            elif len(nome) < 2 or len(nome) > 60:
                print("Valor inválido! O nome deve ter entre 2 e 60 caracteres.")
            else:
                return nome  # Nome válido

            if not perguntar_sim_nao("Deseja tentar novamente? (s/n) "):
                return ""  # Usuário desistiu

    def validar_email():
        # Solicita e valida o email, checando formato manualmente (sem regex)
        while True:
            email = input("\nDigite o email do cliente: ").strip()
            email_valido = True

            if email == "":
                email_valido = False
                print("Valor inválido! O email não pode ficar vazio.")
            elif len(email) > 320:
                email_valido = False
                print("Valor inválido! O email deve ter no máximo 320 caracteres.")
            else:
                partes = email.split("@")  # Separa em usuário e domínio

                if len(partes) != 2:
                    email_valido = False
                    print("Valor inválido! O email deve conter exatamente um '@'.")
                else:
                    usuario = partes[0]
                    dominio = partes[1]

                    if usuario == "" or dominio == "":
                        email_valido = False
                        print("Valor inválido! Preencha corretamente antes e depois do '@'.")
                    elif "." not in dominio:
                        email_valido = False
                        print("Valor inválido! O domínio deve ter um ponto, como em 'dominio.com'.")
                    elif dominio[0] == "." or dominio[len(dominio) - 1] == ".":
                        email_valido = False
                        print("Valor inválido! O domínio não pode começar ou terminar com ponto.")
                    else:
                        extensao = dominio.split(".")
                        ultima_parte = extensao[len(extensao) - 1]

                        extensao_valida = True
                        for letra in ultima_parte:
                            if letra not in letras_dominio:
                                extensao_valida = False

                        if len(ultima_parte) < 2 or not extensao_valida:
                            email_valido = False
                            print("Valor inválido! Digite um email no formato nome@dominio.com.")

            if email_valido:
                return email  # Email válido

            if not perguntar_sim_nao("Deseja tentar novamente? (s/n) "):
                return ""  # Usuário desistiu

    def validar_telefone():
        # Solicita e valida o telefone: só números, com 10 ou 11 dígitos (DDD + número)
        while True:
            telefone = input("\nDigite o telefone com DDD: ").strip()

            # Remove formatação comum, tipo (11) 91234-5678
            numeros = telefone.replace(" ", "")
            numeros = numeros.replace("-", "")
            numeros = numeros.replace("(", "")
            numeros = numeros.replace(")", "")

            if numeros == "":
                print("Valor inválido! O telefone não pode ficar vazio.")
            else:
                try:
                    int(numeros)  # Só serve para confirmar que são todos números
                except ValueError:
                    print("Valor inválido! Digite apenas números (pode incluir DDD).")
                else:
                    if len(numeros) == 10 or len(numeros) == 11:
                        return numeros  # Telefone válido, já limpo
                    else:
                        print("Valor inválido! O telefone deve ter 10 ou 11 dígitos.")

            if not perguntar_sim_nao("Deseja tentar novamente? (s/n) "):
                return ""  # Usuário desistiu

    def cadastrar_cliente():
        # Opção 1 do menu: cadastra um novo cliente no arquivo
        print(f"\n{'='*30}")
        print(f"{'CADASTRAR CLIENTE':^30}")
        print(f"{'='*30}")

        nome = validar_nome()
        if nome == "":
            print("Cadastro cancelado.")
            return

        email = validar_email()
        if email == "":
            print("Cadastro cancelado.")
            return

        telefone = validar_telefone()
        if telefone == "":
            print("Cadastro cancelado.")
            return

        try:
            # O modo "a" cria o arquivo automaticamente, caso ele não exista
            with open(arquivo, "a", encoding="utf-8") as arq:
                arq.write(f"{nome};{email};{telefone}\n")
        except PermissionError:
            print("Não foi possível salvar. Feche o arquivo se ele estiver aberto em outro programa.")
            return
        except OSError as erro:
            print(f"Não foi possível salvar o cliente: {erro}")
            return

        print(f'Cliente "{nome}" cadastrado com sucesso!')

    def listar_clientes():
        # Opção 2 do menu: lê o arquivo e mostra todos os clientes cadastrados
        print(f"\n{'='*30}")
        print(f"{'LISTAR CLIENTES':^30}")
        print(f"{'='*30}")

        if not os.path.exists(arquivo):
            print("Nenhum cliente cadastrado.")
            return

        try:
            with open(arquivo, "r", encoding="utf-8") as arq:
                linhas = arq.readlines()
        except PermissionError:
            print("Não foi possível abrir o arquivo. Feche-o se estiver aberto em outro programa.")
            return
        except OSError as erro:
            print(f"Não foi possível ler o arquivo: {erro}")
            return

        if len(linhas) == 0:
            print("Nenhum cliente cadastrado.")
            return

        for linha in linhas:
            dados = linha.strip().split(";")
            if len(dados) == 3:
                nome = dados[0]
                email = dados[1]
                telefone = dados[2]
                print(f"Nome: {nome} | Email: {email} | Telefone: {telefone}")
            else:
                # Protege contra uma linha corrompida ou fora do formato esperado
                print("Registro inválido encontrado no arquivo e foi ignorado.")    

    def alterar_cliente():
        # Opção 3 do menu: procura um cliente pelo nome e atualiza os dados
        print(f"\n{'='*30}")
        print(f"{'ALTERAR CLIENTE':^30}")
        print(f"{'='*30}")

        if not os.path.exists(arquivo):
            print("Nenhum cliente cadastrado.")
            return

        try:
            with open(arquivo, "r", encoding="utf-8") as arq:
                linhas = arq.readlines()
        except PermissionError:
            print("Não foi possível abrir o arquivo. Feche-o se estiver aberto em outro programa.")
            return
        except OSError as erro:
            print(f"Não foi possível ler o arquivo: {erro}")
            return

        if len(linhas) == 0:
            print("Nenhum cliente cadastrado.")
            return

        nome_busca = input("\nDigite o nome do cliente que deseja alterar: ").strip().lower()
        if nome_busca == "":
            print("Valor inválido! O nome não pode ficar vazio.")
            return

        indice_encontrado = -1
        for i in range(len(linhas)):
            if linhas[i].lower().startswith(nome_busca + ";"):
                indice_encontrado = i
                break  # Para na primeira ocorrência encontrada

        if indice_encontrado == -1:
            print("Cliente não encontrado.")
            return

        print(f"\nCliente encontrado: {linhas[indice_encontrado].strip()}")
        print("Digite os novos dados abaixo:")

        novo_nome = validar_nome()
        if novo_nome == "":
            print("Alteração cancelada.")
            return

        novo_email = validar_email()
        if novo_email == "":
            print("Alteração cancelada.")
            return

        novo_telefone = validar_telefone()
        if novo_telefone == "":
            print("Alteração cancelada.")
            return

        linhas[indice_encontrado] = f"{novo_nome};{novo_email};{novo_telefone}\n"

        try:
            with open(arquivo, "w", encoding="utf-8") as arq:
                arq.writelines(linhas)
        except PermissionError:
            print("Não foi possível salvar. Feche o arquivo se ele estiver aberto em outro programa.")
            return
        except OSError as erro:
            print(f"Não foi possível salvar as alterações: {erro}")
            return

        print("Cliente alterado com sucesso!")

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

# Dupla: João Pedro Formiga Baptista e Matheus Henriques Geroldo
import os

ARQUIVO_PRODUTOS = "produtos.txt"

def menu():
    print("\n===== MENU DE PRODUTOS =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Alterar produto")
    print("4 - Excluir produto")
    print("0 - Voltar ao menu principal")

def carregar_produtos():
    produtos = []

    if not os.path.exists(ARQUIVO_PRODUTOS):
        return produtos

    with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as arquivo:
        linhas_brutas = arquivo.readlines()

    for linha_bruta in linhas_brutas:
        linha = linha_bruta.strip()
        try:
            nome, preco = linha.split(";")
            produtos.append((nome, float(preco)))
        except ValueError:
            print(f"Linha inválida ignorada: {linha}")

    return produtos

def produto_existe(nome):
    produtos = carregar_produtos()
    for nome_cadastrado, preco in produtos:
        if nome_cadastrado.lower() == nome.lower():
            return True
    return False

def cadastrar_produto():
    print("\n--- Cadastro de Produto ---")

    while True:
        nome = input("\nNome do produto: ").strip()
        if nome == "":
            print("O nome não pode ficar em branco.")
            continue
        if produto_existe(nome):
            print("Produto já cadastrado!")
            return
        break

    while True:
        try:
            preco = float(input("\nPreço do produto: R$ "))
        except ValueError:
            print("Valor inválido! Digite um número.")
            continue
        if preco <= 0:
            print("O preço deve ser maior que zero. Tente novamente.")
            continue
        break

    with open(ARQUIVO_PRODUTOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{preco}\n")
    print(f"\nProduto '{nome}' cadastrado com sucesso!")

def listar_produtos():
    print("\n--- Lista de Produtos ---")

    produtos = carregar_produtos()

    if not produtos:
        print("Nenhum produto cadastrado ainda.")
        return

    for nome, preco in produtos:
        print(f"Nome: {nome} - Preço: R${preco:.2f}")

def alterar_produto():
    print("\n--- Alterar Produto ---")
    produtos = carregar_produtos()

    if not produtos:
        print("Nenhum produto cadastrado ainda.")
        return

    nome_pesquisa = input("Digite o nome do produto que deseja alterar: ").strip()
    
    for i, (nome, preco) in enumerate(produtos):
        if nome.lower() == nome_pesquisa.lower():
            print(f"Produto encontrado: {nome} - R${preco:.2f}")
            
            while True:
                novo_nome = input("Digite o novo nome (ou Enter para manter): ").strip()
                if novo_nome == "":
                    novo_nome = nome
                    break
                
                # Validação direta na lista carregada para evitar bugs
                nome_ja_cadastrado = False
                if novo_nome.lower() != nome.lower():
                    for n_cad, _ in produtos:
                        if n_cad.lower() == novo_nome.lower():
                            nome_ja_cadastrado = True
                            break
                
                if nome_ja_cadastrado:
                    print("Produto já cadastrado com esse nome!")
                    continue
                break
                
            while True:
                novo_preco_str = input("Digite o novo preço (ou Enter para manter): R$ ").strip()
                if novo_preco_str == "":
                    novo_preco = preco
                    break
                try:
                    novo_preco = float(novo_preco_str)
                    if novo_preco <= 0:
                        print("O preço deve ser maior que zero.")
                        continue
                    break
                except ValueError:
                    print("Valor inválido!")
            
            produtos[i] = (novo_nome, novo_preco)
            
            with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as arquivo:
                for n, p in produtos:
                    arquivo.write(f"{n};{p}\n")
            print("Produto altered com sucesso!")
            return

    print("Produto não encontrado.")

def excluir_produto():
    print("\n--- Excluir Produto ---")
    produtos = carregar_produtos()

    if not produtos:
        print("Nenhum produto cadastrado ainda.")
        return

    nome_pesquisa = input("Digite o nome do produto que deseja excluir: ").strip()

    for i, (nome, preco) in enumerate(produtos):
        if nome.lower() == nome_pesquisa.lower():
            confirmacao = input(f"Tem certeza que deseja excluir '{nome}'? (S/N): ").strip().upper()
            if confirmacao == "S":
                produtos.pop(i)
                with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as arquivo:
                    for n, p in produtos:
                        arquivo.write(f"{n};{p}\n")
                print("Produto excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
            return

    print("Produto não encontrado.")

def executar_produtos():
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            alterar_produto()
        elif opcao == "4":
            excluir_produto()
        elif opcao == "0":
            print("Saindo do módulo de produtos...")
            break
        else:
            print("Opção inválida! Escolha novamente.")


if __name__ == "__main__":
    executar_produtos()
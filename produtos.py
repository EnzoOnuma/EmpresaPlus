# Dupla: João Pedro Formiga Baptista e Matheus Henriques Geroldo
import os

ARQUIVO_PRODUTOS = "produtos.txt"

def menu():
    print("\n===== MENU DE PRODUTOS =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
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

def cadastrar_produto():
    print("\n--- Cadastro de Produto ---")

    while True:
        nome = input("\nNome do produto: ").strip()
        if nome == "":
            print("O nome não pode ficar em branco.")
            continue
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
        print(f"Nome: {nome} - Preço: R${preco}")

if __name__ == "__main__":
    cadastrar_produto()
    carregar_produtos()
    listar_produtos()
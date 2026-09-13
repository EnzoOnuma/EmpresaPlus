# Dupla: João Pedro Formiga Baptista e Matheus Henriques Geroldo

ARQUIVO_PRODUTOS = "produtos.txt"

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

if __name__ == "__main__":
    cadastrar_produto()
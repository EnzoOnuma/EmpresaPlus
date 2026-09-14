import os
from clientes import cadastro_clientes
from produtos import executar_produtos

def menu_principal():
    print(f"\n{'='*30}")
    print(f"{'SISTEMA PRINCIPAL':^30}")
    print(f"{'='*30}")
    print("1 - Módulo de Clientes")
    print("2 - Módulo de Produtos")
    print("0 - Sair do Sistema")

def main():
    while True:
        menu_principal()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastro_clientes()
        elif opcao == "2":
            executar_produtos()
        elif opcao == "0":
            print("\nEncerrando o sistema.")
            break
        else:
            print("Opção inválida! Tente novamente.")

main()
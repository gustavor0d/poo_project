from models.base import session
from models.cliente import Cliente
from utils.helpers import cls, valor_entrada
from time import sleep

def cadastrar_cliente():
    print("="*8, "Cadastro de Cliente", "="*8)
    print("\n(Digite '0' para cancelar o cadastro)\n")

    nome = valor_entrada("Cliente", "Nome: ")
    if nome is None:
        return

    while True:
        idade_str = input("Idade: ")

        try:
            idade = int(idade_str)

            if idade == 0:
                cls()
                print("Cadastro de cliente cancelado.")
                return

            if 0 < idade < 16:
                cls()
                print(f"Você deve ser maior de 15 anos para realizar um cadastro em nosso sistema!\nCadastro do cliente '{nome}' cancelado automáticamente.")
                return
            
            elif idade < 0 or idade > 100:
                print(f"\nInsira uma idade válida para o {nome}\n")
                continue

            else:
                break

        except:
            print("\nOops, idade inválida! Tente novamente.\n")

    telefone = valor_entrada("Cliente", "Telefone: ")
    if telefone is None:
        return

    cliente = Cliente(nome=nome, idade=idade, telefone=telefone)

    session.add(cliente)
    session.commit()

    cls()
    print(f"Cliente '{nome}' cadastrado com sucesso!\n")
    print(f"ID do cliente: {cliente.idCliente}")

def listar_clientes():
    clientes = session.query(Cliente).all()

    if clientes:
        while True:
            cls()

            print("Lista de Clientes cadastrados:\n")
            print("ID".ljust(3) + " | " + "Nome".ljust(25) + " | " + "Idade".ljust(5) + " | " + "Telefone")
            print("-" * 53)
            for cliente in clientes:
                print(str(cliente.idCliente).ljust(3) + " | " + cliente.nome.ljust(25) + " | " + str(cliente.idade).ljust(5) + " | " + cliente.telefone)

            print("\n\nOpções:\n")
            print("1. Deletar Clientes")
            print("0. Voltar")

            opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                    while True:
                        escolha_cliente = input("\nDigite o ID do Cliente (ou '0' para cancelar): ")

                        try:
                            id_cliente = int(escolha_cliente)

                            if id_cliente == 0:
                                cls()
                                print("Operação cancelada.")
                                break

                            if id_cliente < 0 or id_cliente > len(clientes):
                                print("\nID inválido, tente novamente.")
                                continue
                            
                            else:
                                deletar_cliente(id_cliente)
                                return
                            
                        except:
                            print("\nOops, você não digitou um valor numérico! Tente novamente.")

            if opcao == '0':
                cls()
                break

            else:
                print("\nOops, opção inválida! Tente novamente...")
                sleep(0.5)
                continue

    else:
        cls()
        print("Nenhum cliente cadastrado.")

def deletar_cliente(id_cliente):
    cliente = session.query(Cliente).get(id_cliente)
    
    if cliente:
        print(f"\n\tDeseja realmente deletar o cliente ID {id_cliente}?"
              "\n\t[S] Para Sim"
              "\n\t[N] Para Não")

        while True:
            opcao = input("\n\t>>> ").lower()

            if opcao == 's':
                cls()
                session.delete(cliente)
                session.commit()
                print(f"Cliente ID {id_cliente} deletado com sucesso.")
                break

            elif opcao == 'n':
                cls()
                print("Operação cancelada!")
                return
            
            else:
                print("\n\t[Erro] Entrada inválida!")
                continue
    else:
        cls()
        print(f"Cliente ID {id_cliente} não encontrado.")

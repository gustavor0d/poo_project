from models.base import session
from models.cliente import Cliente
from utils.helpers import cls, valor_entrada
from time import sleep


def cadastrar_cliente():
    cls()
    print("="*14, "Cadastro de Cliente", "="*14)
    print("\n(Digite '0' em qualquer etapa para cancelar o cadastro)\n")
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
    print(f"ID: {cliente.idCliente}")


def listar_clientes():
    clientes = session.query(Cliente).all()
    if clientes:
        while True:
            cls()
            visualizar_clientes(clientes)
            print("\n\nOpções:\n")
            print("1. Cadastrar Clientes")
            print("2. Editar Clientes")
            print("3. Deletar Clientes")
            print("0. Voltar")
            opcao = input("\nEscolha uma opção: ")
            if opcao == '1':
                cadastrar_cliente()
                return
            elif opcao == '2':
                cls()
                print("Opção em desenvolvimento...")
                sleep(1)
                continue
            elif opcao == '3':
                id_verificado = verificar_id(clientes)
                if id_verificado is not False:
                    deletar_cliente(id_verificado)
                    return                
            elif opcao == '0':
                cls()
                print("Voltando...")
                sleep(0.4)
                cls()
                break
            else:
                cls()
                print("\nOops, opção inválida! Tente novamente...")
                sleep(0.7)
    else:
        cls()
        print("Nenhum cliente cadastrado.")


def atualizar_cliente(id_cliente):
    pass


def deletar_cliente(id_cliente):
    cliente = session.query(Cliente).filter_by(idCliente=id_cliente).first()
    if cliente:
        print(f"\n\tDeseja realmente deletar o cliente: {cliente.nome}?"
                "\n\t[S] Para Sim"
                "\n\t[N] Para Não")
        while True:
            opcao = input("\n\t>>> ").lower()
            if opcao == 's':
                session.delete(cliente)
                session.commit()
                cls()
                print(f"Cliente ID {cliente.idCliente} deletado com sucesso.")
                return True
            elif opcao == 'n':
                cls()
                print("Operação cancelada!")
                sleep(0.5)
                cls()
                return False
            else:
                print("\n\tEntrada inválida!")
    else:
        cls()
        print("Um erro desconhecido foi encontrado.")
        sleep(1.5)
        cls()
        return


def verificar_id(busca):
    while True:
        cls()
        visualizar_clientes(busca)
        id = input(f"\n\nDigite o ID do Cliente (ou '0' para cancelar): ")
        try:
            id = int(id)
            if id == 0:
                cls()
                print("Operação cancelada.")
                sleep(0.5)
                return False
            elif id < 0 or id > len(busca):
                print("\nID inválido, tente novamente...")
                sleep(0.6)
                continue
            else:
                return id            
        except:
            print("\nOops, você não digitou um valor numérico! Tente novamente.")
            sleep(1.2)


def visualizar_clientes(clientes):
    print("Lista de Clientes cadastrados:\n")
    print("ID".ljust(3) + " | " + "Nome".ljust(25) + " | " + "Idade".ljust(5) + " | " + "Telefone")
    print("-" * 53)
    for cliente in clientes:
        print(str(cliente.idCliente).ljust(3) + " | " + cliente.nome.ljust(25) + " | " + str(cliente.idade).ljust(5) + " | " + cliente.telefone)

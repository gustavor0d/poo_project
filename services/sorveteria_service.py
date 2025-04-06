from models.base import session
from models.sorveteria import Sorveteria
from models.sabor import Sabor
from services.sabor_service import cadastrar_sabor, listar_sabores
from utils.helpers import cls, valor_entrada
from time import sleep


def cadastrar_sorveteria():
    cls()
    print("="*12, "Cadastro de Sorveteria", "="*12)
    print("\n(Digite '0' em qualquer etapa para cancelar o cadastro)\n")
    nome = valor_entrada("Sorveteria", "Digite o Nome: ")
    if nome is None:
        return
    endereco = valor_entrada("Sorveteria", "Digite o Endereço: ")
    if endereco is None:
        return
    telefone = valor_entrada("Sorveteria", "Digite o Telefone: ")
    if telefone is None:
        return
    sorveteria = Sorveteria(nome=nome, endereco=endereco, telefone=telefone)
    session.add(sorveteria)
    session.commit()
    cls()
    print(f"Sorveteria '{nome}' cadastrada com sucesso!\n")
    print(f"ID: {sorveteria.idSorveteria}")


def listar_sorveterias():
    sorveterias = session.query(Sorveteria).all()
    if sorveterias:
        while True:
            cls()
            visualizar_sorveterias(sorveterias)
            print("\n\nOpções:\n")
            print("1. Cadastrar Sorveterias")
            print("2. Editar Sorveterias")
            print("3. Deletar Sorveterias")
            print("4. Visualizar Sabores")
            print("5. Cadastrar Sabores")
            print("0. Voltar")
            opcao = input("\nEscolha uma opção: ")
            if opcao == '1':
                cadastrar_sorveteria()
                return
            elif opcao == '2':
                cls()
                print("Opção em desenvolvimento...")
                sleep(1)
                continue
            elif opcao == '3':
                id_verificado = verificar_id(sorveterias)
                if id_verificado is not False:
                    deletar_sorveteria(id_verificado)
                    return
            elif opcao == '4':
                visualizar_sabores(sorveterias)
                continue
            elif opcao == '5':
                cadastrar_sabor()
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
        print("Nenhuma sorveteria cadastrada.")


def atualizar_sorveteria(id_sorveteria):
    pass


def deletar_sorveteria(id_sorveteria):
    sorveteria = session.query(Sorveteria).filter_by(idSorveteria=id_sorveteria).first()

    if sorveteria:
        print(f"\n\tDeseja realmente deletar a sorveteria: '{sorveteria.nome}'?"
                "\n\t[S] Para Sim"
                "\n\t[N] Para Não")
        while True:
            opcao = input("\n\t>>> ").lower()
            if opcao == 's':
                session.delete(sorveteria)
                session.commit()
                cls()
                print(f"Sorveteria ID {sorveteria.idSorveteria} deletada com sucesso.")
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

def visualizar_sabores(sorveterias):
    while True:
        cls()
        print("Lista de Sorveterias com sabores cadastrados:")
        print("\n" + "ID".ljust(3) + " | " + "Nome".ljust(15) + " | " + "Endereço".ljust(15) + " | " + "Telefone".ljust(10) + " | " + "Qtd. Sabores")
        print("-" * 68)
        lista_qtd_sabores = []
        for sorveteria in sorveterias:
            quantidade_sabores = len(session.query(Sabor).filter_by(sorveteria_id=sorveteria.idSorveteria).all())
            if quantidade_sabores > 0:
                print(str(sorveteria.idSorveteria).ljust(3) + " | " + sorveteria.nome.ljust(15) + " | " + sorveteria.endereco.ljust(15) + " | " + sorveteria.telefone.ljust(10) + " | " + str(quantidade_sabores))
                lista_qtd_sabores.append(sorveteria.idSorveteria)
        if len(lista_qtd_sabores) == 0:
            for i in range(3, 0, -1):
                cls()
                print("\nNão existe nenhuma sorveteria com sabor cadastrado!")
                print(f"\nVoltando automáticamente em {i} segundos...")
                sleep(1)
            return False
        else:
            id = input(f"\n\nDigite o ID da Sorveteria (ou '0' para cancelar): ")
            try:
                id = int(id)
                if id == 0:
                    cls()
                    print("Operação cancelada.")
                    return False
                elif id not in lista_qtd_sabores:
                    print("\nID informado não corresponde com nenhum apresentado na lista de sorveterias com sabores cadastrados! \nVerifique e tente novamente...")
                    sleep(3)
                    continue
                else:
                    return listar_sabores(id)
            except:
                print("\nOops, você não digitou um valor numérico! Tente novamente.")
                sleep(1.2)


def verificar_id(busca):
    while True:
        cls()
        visualizar_sorveterias(busca)

        id = input(f"\n\nDigite o ID da Sorveteria (ou '0' para cancelar): ")
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


def visualizar_sorveterias(sorveterias):
    print("Lista de Sorveterias cadastradas:")
    print("\n" + "ID".ljust(3) + " | " + "Nome".ljust(15) + " | " + "Endereço".ljust(15) + " | " + "Telefone".ljust(10) + " | " + "Qtd. Sabores")
    print("-" * 68)
    for sorveteria in sorveterias:
        quantidade_sabores = len(session.query(Sabor).filter_by(sorveteria_id=sorveteria.idSorveteria).all())
        print(str(sorveteria.idSorveteria).ljust(3) + " | " + sorveteria.nome.ljust(15) + " | " + sorveteria.endereco.ljust(15) + " | " + sorveteria.telefone.ljust(10) + " | " + str(quantidade_sabores))

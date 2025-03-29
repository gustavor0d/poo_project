from models.base import session
from models.sorveteria import Sorveteria
from utils.helpers import cls
from services.sabor_service import listar_sabores

def cadastrar_sorveteria():
    print("\n(Digite '0' para cancelar o cadastro)\n")

    nome = input("Nome da Sorveteria: ")
    if nome == '0':
        cls()
        print("\nCadastro de sorveteria cancelado.")
        return

    endereco = input("Endereço: ")
    if endereco == '0':
        cls()
        print("\nCadastro de sorveteria cancelado.")
        return

    telefone = input("Telefone: ")
    if telefone == '0':
        cls()
        print("\nCadastro de sorveteria cancelado.")
        return

    sorveteria = Sorveteria(nome=nome, endereco=endereco, telefone=telefone)
    session.add(sorveteria)
    session.commit()

    cls()
    print(f"\nSorveteria '{nome}' cadastrada com sucesso!\n")
    print(f"ID da sorveteria: {sorveteria.idSorveteria}")

def listar_sorveterias():
    sorveterias = session.query(Sorveteria).all()

    if sorveterias:
        print("\n" + "ID".ljust(5) + " | " + "Nome".ljust(20) + " | " + "Endereço".ljust(25) + " | " + "Telefone".ljust(15))
        print("-" * 75)

        for sorveteria in sorveterias:
            print(str(sorveteria.idSorveteria).ljust(5) + " | " + sorveteria.nome.ljust(20) + " | " + sorveteria.endereco.ljust(25) + " | " + sorveteria.telefone.ljust(15))
        
        print("-" * 75)

        while True:
            print("\nOpções:\n")
            print("1. Visualizar Sabores")
            print("2. Deletar Sorveterias")
            print("0. Voltar")

            opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                listar_sabores()
                break

            if opcao == '2':
                    while True:
                        escolha_sorveteria = input("\nDigite o ID da Sorveteria (ou '0' para cancelar): ")

                        try:
                            id_sorveteria = int(escolha_sorveteria)

                            if id_sorveteria == 0:
                                cls()
                                print("\nOperação cancelada.")
                                return

                            if id_sorveteria < 0 or id_sorveteria > len(sorveterias):
                                print("\nID inválido, tente novamente.")
                                continue
                            
                            else:
                                deletar_sorveteria(id_sorveteria)
                                return
                            
                        except:
                            print("\nOops, você não digitou um valor numérico! Tente novamente.")

            if opcao == '0':
                cls()
                break

            else:
                print("\nOops, opção inválida! Tente novamente.")
                continue
    else:
        cls()
        print("\nNenhuma sorveteria cadastrada.")

def deletar_sorveteria(id_sorveteria):
    sorveteria = session.query(Sorveteria).get(id_sorveteria)
    
    if sorveteria:
        print(f"Deseja realmente deletar a sorveteria ID {id_sorveteria}?\n[S] Para Sim\n[N] Para Não")

        while True:
            opcao = input("\n>>> ").lower()

            if opcao == 's':
                cls()
                session.delete(sorveteria)
                session.commit()
                print(f"Sorveteria ID {id_sorveteria} deletada com sucesso.")
                break

            elif opcao == 'n':
                cls()
                print("Operação cancelada!")
                return
            
            else:
                print("\nEntrada inválida!")
                continue
    else:
        print(f"\nSorveteria ID {id_sorveteria} não encontrada.")

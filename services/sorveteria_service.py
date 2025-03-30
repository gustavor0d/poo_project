from models.base import session
from models.sorveteria import Sorveteria
from models.sabor import Sabor
from services.sabor_service import listar_sabores
from utils.helpers import cls, valor_entrada
from time import sleep

def cadastrar_sorveteria():
    print("="*6, "Cadastro de Sorveteria", "="*6)
    print("\n(Digite '0' para cancelar o cadastro)\n")

    nome = valor_entrada("Sorveteria", "Digite um Nome: ")
    if nome is None:
        return

    endereco = valor_entrada("Sorveteria", "Digite um Endereço: ")
    if endereco is None:
        return

    telefone = valor_entrada("Sorveteria", "Digite um Telefone: ")
    if telefone is None:
        return

    sorveteria = Sorveteria(nome=nome, endereco=endereco, telefone=telefone)
    session.add(sorveteria)
    session.commit()

    cls()
    print(f"Sorveteria '{nome}' cadastrada com sucesso!\n")
    print(f"ID da Sorveteria: {sorveteria.idSorveteria}")

def listar_sorveterias():
    sorveterias = session.query(Sorveteria).all()

    if sorveterias:
        while True:
            cls()

            print("Lista de Sorveterias cadastradas:")
            print("\n" + "ID".ljust(3) + " | " + "Nome".ljust(15) + " | " + "Endereço".ljust(15) + " | " + "Telefone".ljust(10) + " | " + "Qtd. Sabores")
            print("-" * 68)
            for sorveteria in sorveterias:
                print(str(sorveteria.idSorveteria).ljust(3) + " | " + sorveteria.nome.ljust(15) + " | " + sorveteria.endereco.ljust(15) + " | " + sorveteria.telefone.ljust(10) + " | " + str(len(session.query(Sabor).filter_by(sorveteria_id=sorveteria.idSorveteria).all())))

            print("\n\nOpções:\n")
            print("1. Visualizar Sabores")
            print("2. Deletar Sorveterias")
            print("0. Voltar")

            opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                sabores = listar_sabores()

                if sabores is False:
                    continue

                print("\n\nOpções:\n")
                print("0. Voltar")

                while True:
                    voltar = input("\nEscolha uma opção: ")

                    if voltar == '0':
                        break

                    else:
                        print("\nOops, opção inválida! Tente novamente...")

            if opcao == '2':
                    while True:
                        escolha_sorveteria = input("\nDigite o ID da Sorveteria (ou '0' para cancelar): ")

                        try:
                            id_sorveteria = int(escolha_sorveteria)

                            if id_sorveteria == 0:
                                cls()
                                print("Operação cancelada.")
                                break

                            if id_sorveteria < 0 or id_sorveteria > len(sorveterias):
                                print("\nID de sorveteria inválido, tente novamente.")
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
                print("\nOops, opção inválida! Tente novamente...")
                sleep(0.5)
                continue
    else:
        cls()
        print("Nenhuma sorveteria cadastrada.")

def deletar_sorveteria(id_sorveteria):
    sorveteria = session.query(Sorveteria).get(id_sorveteria)
    
    if sorveteria:
        print(f"\n\tDeseja realmente deletar a sorveteria ID {id_sorveteria}?"
              "\n\t[S] Para Sim"
              "\n\t[N] Para Não")

        while True:
            opcao = input("\n\t>>> ").lower()

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
                print("\n\t[Erro] Entrada inválida!")
                continue
    else:
        cls()
        print(f"Sorveteria ID {id_sorveteria} não encontrada.")

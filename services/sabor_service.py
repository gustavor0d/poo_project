from models.base import session
from models.sorveteria import Sorveteria
from models.sabor import Sabor
from utils.helpers import cls, valor_entrada


def cadastrar_sabor():
    sorveterias = session.query(Sorveteria).all()
    if not sorveterias:
        cls()
        print("É necessário ter pelo omenos uma sorveteria criada para cadastrar um sabor.")
        return
    cls()
    print("Lista de Sorveterias:\n")
    print("ID".ljust(3) + " | " + "Nome".ljust(15))
    print("-" * 20)
    for sorveteria in sorveterias:
        print(str(sorveteria.idSorveteria).ljust(3) + " | " + sorveteria.nome.ljust(15))
    while True:
        id_sorveteria = input("\nEscolha o ID de uma sorveteria para cadastrar o sabor (ou digite '0' para cancelar): ")
        try:
            id_sorveteria = int(id_sorveteria)
            if id_sorveteria == 0:
                cls()
                print("Cadastro de sabor cancelado.")
                return
            if id_sorveteria < 0 or id_sorveteria > len(sorveterias):
                print("\nID da sorveteria inválida.")
                continue
            else:
                break
        except:
            print("\nOops, você não digitou um valor numérico! Tente novamente.")
    sorveteria_selecionada = sorveterias[id_sorveteria - 1]
    cls()
    print(f"* Sorveteria: '{sorveteria_selecionada.nome}' selecionada com sucesso!\n")
    print("="*15, "Cadastro de Sabor", "="*15)
    print("\n(Digite '0' em qualquer etapa para cancelar o cadastro)\n")
    nome = valor_entrada("Sabor", "Nome do Sabor: ")
    if nome is None:
        return
    descricao = valor_entrada("Sabor", "Descrição do Sabor adicionado: ")
    if descricao is None:
        return
    while True:
        preco = input("Preço do Sabor: ")
        try:
            preco_escolhido = float(preco)
            if preco_escolhido <= 0:
                cls()
                print("Cadastro de sabor cancelado.")
                return
            else:
                break
        except:
            print("\nValor de preço inválido. Tente novamente!")
    sabor = Sabor(nome=nome, descricao=descricao, preco=preco_escolhido, sorveteria=sorveteria_selecionada)
    session.add(sabor)
    session.commit()
    cls()
    print(f"Sabor '{nome}' cadastrado com sucesso na sorveteria: '{sorveteria_selecionada.nome}'")


def listar_sabores(id_sorveteria):
    sorveterias = session.query(Sorveteria).all()
    sorveteria_selecionada = sorveterias[id_sorveteria - 1]
    sabores = session.query(Sabor).filter_by(sorveteria_id=sorveteria_selecionada.idSorveteria).all()
    cls()
    print(f"Sabores disponíveis na sorveteria: '{sorveteria_selecionada.nome}':")
    print("\n" + "ID".ljust(3) + " | " + "Sabor".ljust(20) + " | " + "Descrição".ljust(40) + " | " + "Preço (R$)".ljust(10))
    print("-" * 88)
    for sabor in sabores:
        print(f"{sabor.idSabor}".ljust(3) + " | " + sabor.nome.ljust(20) + " | " + sabor.descricao.ljust(40) + " | " + f"{sabor.preco:.2f}".ljust(10))
    input("\nPressione 'enter' para voltar...\n")
    return

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base 
import os

def cls():
    return os.system("cls")

cls()

Base = declarative_base()

pedido_sabor = Table('pedido_sabor', Base.metadata,
    Column('pedido_id', Integer, ForeignKey('pedido.idPedido')),
    Column('sabor_id', Integer, ForeignKey('sabor.idSabor'))
)

class Sorveteria(Base):
    __tablename__ = 'sorveteria'

    idSorveteria = Column(Integer, primary_key=True)
    nome = Column(String)
    endereco = Column(String)
    telefone = Column(String)
    sabores = relationship("Sabor", back_populates="sorveteria")

    def adicionar_sabor(self, sabor):
        self.sabores.append(sabor)

class Sabor(Base):
    __tablename__ = 'sabor'

    idSabor = Column(Integer, primary_key=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(Float)
    sorveteria_id = Column(Integer, ForeignKey('sorveteria.idSorveteria'))
    sorveteria = relationship("Sorveteria", back_populates="sabores")

class Cliente(Base):
    __tablename__ = 'cliente'

    idCliente = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    telefone = Column(String)
    pedidos = relationship("Pedido", back_populates="cliente")

class Pedido(Base):
    __tablename__ = 'pedido'

    idPedido = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('cliente.idCliente'))
    cliente = relationship("Cliente", back_populates="pedidos")
    sabores = relationship("Sabor", secondary=pedido_sabor)
    total = Column(Float)

    def calcular_total(self):
        self.total = sum(sabor.preco for sabor in self.sabores)

engine = create_engine('sqlite:///sorveteria.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

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

def cadastrar_sabor():
    sorveterias = session.query(Sorveteria).all()

    if not sorveterias:
        cls()
        print("\nNenhuma sorveteria cadastrada.")
        return
    
    print("\nLista de sorveteria(s):")

    for i, sorveteria in enumerate(sorveterias, 1):
        print(f"ID: {i} - {sorveteria.nome}")

    while True:
        escolha_sorveteria = input("\nEscolha o ID da sorveteria para cadastrar o sabor (ou digite '0' para cancelar): ")

        try:
            id_sorveteria = int(escolha_sorveteria) - 1

            if id_sorveteria + 1 == 0:
                cls()
                print("\nCadastro de sabor cancelado.")
                return
        
            if id_sorveteria < 0 or id_sorveteria >= len(sorveterias):
                print("\nID da sorveteria inválida.")
                continue
            else:
                break
        except:
            print("\nOops, você não digitou um valor numérico! Tente novamente.")
    
    sorveteria_selecionada = sorveterias[id_sorveteria]
    
    cls()
    print(f"Sorveteria: {sorveteria_selecionada.nome} selecionada com sucesso!")

    print("\n(Digite '0' para cancelar o cadastro)\n")

    nome = input("Nome do Sabor: ")
    if nome == '0':
        cls()
        print("\nCadastro de sabor cancelado.")
        return

    descricao = input("Descrição do Sabor adicionado: ")
    if descricao == '0':
        cls()
        print("\nCadastro de sabor cancelado.")
        return

    while True:
        preco = input("Preço do Sabor: ")

        try:
            preco_escolhido = float(preco)

            if preco_escolhido <= 0:
                cls()
                print("\nCadastro de sabor cancelado.")
                return
            
            else:
                break

        except:
            print("\nValor de preço inválido. Tente novamente!")

    sabor = Sabor(nome=nome, descricao=descricao, preco=preco_escolhido, sorveteria=sorveteria_selecionada)
    session.add(sabor)
    session.commit()

    cls()
    print(f"\nSabor '{nome}' cadastrado com sucesso na sorveteria: {sorveteria_selecionada.nome}")

def cadastrar_cliente():
    print("\n(Digite '0' para cancelar o cadastro)\n")

    nome = input("Nome do cliente: ")
    if nome == '0':
        cls()
        print("\nCadastro de cliente cancelado.")
        return

    while True:
        idade_str = input("Idade: ")

        try:
            idade = int(idade_str)

            if idade == 0:
                cls()
                print("\nCadastro de cliente cancelado.")
                return

            if 0 < idade < 16:
                print(f"\nVocê deve ser maior de 15 anos para realizar um cadastro em nosso sistema!\nCadastro do(a) {nome} cancelado.")
                return
            
            elif idade < 0 or idade > 80:
                print(f"\nInsira uma idade válida para o {nome}\n")
                continue

            else:
                break

        except:
            print("\nOops, idade inválida! Tente novamente.\n")

    telefone = input("Telefone: ")
    if telefone == '0':
        cls()
        print("\nCadastro de cliente cancelado.")
        return

    cliente = Cliente(nome=nome, idade=idade, telefone=telefone)

    session.add(cliente)
    session.commit()

    cls()
    print(f"\nCliente '{nome}' cadastrado com sucesso!\n")
    print(f"ID do cliente: {cliente.idCliente}")

def realizar_pedido():
    clientes = session.query(Cliente).all()
    sorveterias = session.query(Sorveteria).all()
    
    if not clientes:
        cls()
        print("\nAinda não existe nenhum cliente cadastrado para realizar um pedido!")
        return
    
    if not sorveterias:
        cls()
        print("\nAinda não existe nenhuma sorveteria cadastrada.")
        return
    
    print("\nLista de cliente(s):")
    for i, cliente in enumerate(clientes, 1):
        print(f"ID: {i} - Nome: {cliente.nome}")

    while True:
        escolha_cliente = input("\nEscolha o ID do cliente que irá realizar o pedido (digite '0' para cancelar): ")

        try:
            id_cliente = int(escolha_cliente) - 1

            if id_cliente + 1 == 0:
                cls()
                print("\nRealização do pedido cancelada.")
                return
        
            if id_cliente < 0 or id_cliente >= len(clientes):
                print("\nID do cliente inválido.")
                continue

            else:
                break
            
        except:
            print("\nOops, você não digitou um valor numérico! Tente novamente.")

    cliente = clientes[id_cliente]

    cls()

    print(f"Cliente {cliente.nome} selecionado com sucesso!")
       
    print("\nSorveterias:")
    for i, sorveteria in enumerate(sorveterias, 1):
        print(f"ID: {i} - Sorveteria: {sorveteria.nome} - Qtd. Sabores:", len(session.query(Sabor).filter_by(sorveteria_id=sorveterias[i-1].idSorveteria).all()))
    
    while True:
        escolha_sorveteria = input("\nEscolha o ID da sorveteria que irá realizar o pedido: ")

        try:
            id_sorveteria = int(escolha_sorveteria) - 1

            if id_sorveteria + 1 == 0:
                cls()
                print("\nRealização do pedido cancelada.")
                return

            if id_sorveteria < 0 or id_sorveteria >= len(sorveterias):
                print("\nID da sorveteria inválido.")
                continue

            else:
                break

        except:
            print("\nOops, você não digitou um valor numérico! Tente novamente.")
    
    sorveteria_escolhida = sorveterias[id_sorveteria]
    
    sabores = session.query(Sabor).filter_by(sorveteria_id=sorveteria_escolhida.idSorveteria).all()
    
    if not sabores:
        cls()
        print(f"\nNenhum sabor cadastrado na sorveteria: {sorveteria_escolhida.nome}.")
        return
    
    pedido = Pedido(cliente=cliente)
    
    cls()

    print(f"Escolha os sabores para o pedido de {cliente.nome} na sorveteria {sorveteria_escolhida.nome}.")
    print("\n(Digite '0' para finalizar o pedido com os itens adicionados)\n")
    
    for i, sabor in enumerate(sabores, 1):
        print(f"ID: {i} - Sabor : " + str(sabor.nome).ljust(15) + f"- Preço: R$ {sabor.preco:.2f}")
    
    print()

    contagem_pedidos = 0

    while True:
        if contagem_pedidos == 0:
            print("(Pedidos: 0)")
        
        id_sabor = input("ID do sabor: ")

        try:
            escolha_sabor = int(id_sabor) - 1

            if escolha_sabor + 1 == 0:
                break

            elif escolha_sabor < 0 or escolha_sabor > len(sabores):
                print("\nID do sabor inválido.\n")
                continue
            
            sabor_escolhido = sabores[escolha_sabor - 1]
            pedido.sabores.append(sabor_escolhido)
            contagem_pedidos += 1

            print(f"\n(Pedidos: {contagem_pedidos} | Sabor: {sabor_escolhido.nome})")

        except:
            print("ID inválido.")
    
    if contagem_pedidos > 0:
        pedido.calcular_total()
        session.add(pedido)
        session.commit()

        cls()        
        print(f"\nPedido realizado com sucesso! Cliente: {cliente.nome}, Sorveteria: {sorveteria_escolhida.nome}, Total: R$ {pedido.total:.2f} | {contagem_pedidos} Pedido(s).")

    else:
        cls()
        print("\nPedido cancelado. Nenhum sabor selecionado.")

def listar_pedidos():
    pedidos = session.query(Pedido).all()

    if pedidos:
        print("\n" + "ID".ljust(5) + " | " + "Cliente".ljust(20) + " | " + "Sorveteria".ljust(20) + " | " + "Sabor(es)".ljust(30) + " | " + "Total".ljust(10))
        print("-" * 100)

        for pedido in pedidos:
            if pedido.sabores:
                sorveteria_nome = pedido.sabores[0].sorveteria.nome
            
            sabores = ', '.join([sabor.nome for sabor in pedido.sabores])
            print(str(pedido.idPedido).ljust(5) + " | " + pedido.cliente.nome.ljust(20) + " | " + sorveteria_nome.ljust(20) + " | " + sabores.ljust(30) + " | " + f"R${pedido.total:.2f}".ljust(10))
    else:
        cls()
        print("\nNenhum pedido localizado.")

def listar_sabores():
    sorveterias = session.query(Sorveteria).all()

    while True:
        escolha_sorveteria = input("\nDigite o ID da Sorveteria (ou '0' para cancelar): ")

        try:
            id_sorveteria = int(escolha_sorveteria) - 1

            if id_sorveteria + 1 == 0:
                cls()
                print("\nOperação cancelada.")
                return

            if id_sorveteria < 0 or id_sorveteria >= len(sorveterias):
                print("\nID da sorveteria inválida.")
                continue

            else:
                break
            
        except:
            print("\nOops, você não digitou um valor numérico! Tente novamente.")

    sorveteria_selecionada = sorveterias[id_sorveteria]
    sabores = session.query(Sabor).filter_by(sorveteria_id=sorveteria_selecionada.idSorveteria).all()
    
    if not sabores:
        cls()
        print(f"\nNenhum sabor cadastrado na sorveteria: {sorveteria_selecionada.nome}.")
        
    else:
        cls()
        print(f"\nSabores disponíveis na sorveteria {sorveteria_selecionada.nome}:")
        print("\n" + "ID".ljust(5) + " | " + "Sabor".ljust(20) + " | " + "Descrição".ljust(40) + " | " + "Preço (R$)".ljust(10))
        print("-" * 90)

        for i, sabor in enumerate(sabores, 1):
            print(f"{i}".ljust(5) + " | " + sabor.nome.ljust(20) + " | " + sabor.descricao.ljust(40) + " | " + f"{sabor.preco:.2f}".ljust(10))

def deletar_sorveteria(id_sorveteria):
    sorveteria = session.query(Sorveteria).get(id_sorveteria)

    cls()
    
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

def deletar_cliente(id_cliente):
    cliente = session.query(Cliente).get(id_cliente)

    cls()
    
    if cliente:
        print(f"Deseja realmente deletar o cliente ID {id_cliente}?\n[S] Para Sim\n[N] Para Não")

        while True:
            opcao = input("\n>>> ").lower()

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
                print("\nEntrada inválida!")
                continue

    else:
        print(f"\nCliente ID {id_cliente} não encontrado.")

def listar_clientes():
    clientes = session.query(Cliente).all()

    if clientes:
        print("\n" + "ID".ljust(3) + " | " + "Nome".ljust(25) + " | " + "Idade".ljust(5) + " | " + "Telefone".ljust(20))
        print("-" * 60)

        for cliente in clientes:
            print(str(cliente.idCliente).ljust(3) + " | " + cliente.nome.ljust(25) + " | " + str(cliente.idade).ljust(5) + " | " + cliente.telefone.ljust(20))

        print("-" * 60)

        while True:
            print("\nOpções:\n")
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
                                print("\nOperação cancelada.")
                                return

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
                print("\nOops, opção inválida! Tente novamente.")
                continue

    else:
        cls()
        print("\nNenhum cliente cadastrado.")

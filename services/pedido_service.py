from models.base import session
from models.cliente import Cliente
from models.sorveteria import Sorveteria
from models.sabor import Sabor
from models.pedido import Pedido
from utils.helpers import cls

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

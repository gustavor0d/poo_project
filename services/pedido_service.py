from models.base import session
from models.cliente import Cliente
from models.sorveteria import Sorveteria
from models.sabor import Sabor
from models.pedido import Pedido
from utils.helpers import cls, data_format, data
from time import sleep

def realizar_pedido():
    clientes = session.query(Cliente).all()
    sorveterias = session.query(Sorveteria).all()
    if not clientes:
        cls()
        print("Ainda não existe nenhum cliente cadastrado para realizar um pedido!")
        return
    if not sorveterias:
        cls()
        print("Ainda não existe nenhuma sorveteria cadastrada para realizar um pedido!")
        return
    cls()
    print("Lista de Clientes:\n")
    print("ID".ljust(3) + " | " + "Nome")
    print("-" * 20)
    for cliente in clientes:
        print(str(cliente.idCliente).ljust(3) + " | " + cliente.nome)
    while True:
        escolha_cliente = input("\nEscolha o ID do cliente que irá realizar o pedido (digite '0' para cancelar): ")
        try:
            id_cliente = int(escolha_cliente) - 1
            if id_cliente + 1 == 0:
                cls()
                print("Realização do pedido cancelada.")
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
    print("\nSorveterias:\n")
    print("ID".ljust(3) + " | " + "Nome".ljust(15) + " | " + "Qtd. Sabores")
    print("-" * 38)
    for sorveteria in sorveterias:
        print(str(sorveteria.idSorveteria).ljust(3) + " | " + sorveteria.nome.ljust(15) + " | " + str(len(session.query(Sabor).filter_by(sorveteria_id=sorveteria.idSorveteria).all())))
    while True:
        escolha_sorveteria = input("\nEscolha o ID da sorveteria que o cliente irá realizar o pedido (digite '0' para cancelar): ")
        try:
            id_sorveteria = int(escolha_sorveteria) - 1
            if id_sorveteria + 1 == 0:
                cls()
                print("Realização do pedido cancelada.")
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
        print(f"Nenhum sabor cadastrado na sorveteria: '{sorveteria_escolhida.nome}'.")
        return
    pedido = Pedido(cliente=cliente)
    cls()
    print(f"Pedido de: {cliente.nome}")
    print(f"\nSabores disponíveis na sorveteria {sorveteria_escolhida.nome}:\n")
    print("ID".ljust(5) + " | " + "Sabor".ljust(20) + " | " + "Descrição".ljust(40) + " | " + "Preço (R$)".ljust(10))
    print("-" * 90)
    for sabor in sabores:
        print(f"{sabor.idSabor}".ljust(5) + " | " + sabor.nome.ljust(20) + " | " + sabor.descricao.ljust(40) + " | " + f"{sabor.preco:.2f}".ljust(10))
    print("\n\n(Digite '0' para finalizar o pedido com os itens adicionados)\n")
    contagem_pedidos = 0
    valor_momento = 0.0
    status_pedido = False
    while True:
        if contagem_pedidos <= 0:
            print("(Carrinho vazio)")
        else:
            status_pedido = True
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
            valor_momento += sabor_escolhido.preco
            print(f"\n(Pedidos: {contagem_pedidos}) | Sabor: {sabor_escolhido.nome} | +R$ {sabor_escolhido.preco:.2f} | Valor total: R$ {valor_momento:.2f}")
            if contagem_pedidos == 10:
                print(f"\nVocê atingiu a quantidade máxima de itens no mesmo pedido! ({contagem_pedidos})")
                print(f"\n\tDeseja continuar com a compra? Total: R$ {valor_momento:.2f}")
                print("\t[S] para Sim")
                print("\t[N] para Não")
                finalizar_pedido = input("\n\t>>> ").lower()
                if finalizar_pedido == 's':
                    status_pedido = True
                    break
                elif finalizar_pedido == 'n':
                    status_pedido = False
                    break
                else:
                    print("\nOpção não identificada! Por segurança, iremos cancelar seu pedido automáticamente...")
                    sleep(3)
                    status_pedido = False
                    break
        except:
            print("\n[ID de sabor inválido]\n")
    if contagem_pedidos > 0 and status_pedido:
        pedido.calcular_total()
        pedido.atribuir_data(data)
        session.add(pedido)
        session.commit()
        cls()        
        print(f"Pedido realizado com sucesso!"
              f"\nCliente: {cliente.nome}"
              f"\nSorveteria: {sorveteria_escolhida.nome}"
              f"\nTotal: R$ {pedido.total:.2f} | {contagem_pedidos} Pedido(s)."
              f"\nData: {data_format(pedido.data)}")
    elif contagem_pedidos == 0:
        cls()
        print("Pedido cancelado. Nenhum sabor selecionado.")
    else:
        cls()
        print("Pedido cancelado no carrinho.")


def listar_pedidos():
    pedidos = session.query(Pedido).all()
    clientes = session.query(Cliente).all()
    sorveterias = session.query(Sorveteria).all()
    if not pedidos:
        cls()
        print("Nenhum pedido localizado.")
        return
    elif not clientes:
        cls()
        print("Você deletou todos os clientes, por isso não conseguimos recuperar a lista de pedidos.")
        return
    elif not sorveterias:
        cls()
        print("Você deletou todas as sorveterias, por isso não conseguimos recuperar a lista de pedidos.")
        return
    else:
        try:
            while True:
                cls()
                print("Lista de Pedidos:\n")
                print("ID".ljust(5) + " | " + "Cliente".ljust(20) + " | " + "Sorveteria".ljust(20) + " | " + "Sabor(es)".ljust(30) + " | " + "Total".ljust(10) + " | " + "Data Pedido".ljust(10))
                print("-" * 120)
                for pedido in pedidos:
                    if pedido.sabores:
                        sorveteria_nome = pedido.sabores[0].sorveteria.nome
                    sabores = ', '.join([sabor.nome for sabor in pedido.sabores])
                    print(str(pedido.idPedido).ljust(5) + " | " + pedido.cliente.nome.ljust(20) + " | " + sorveteria_nome.ljust(20) + " | " + sabores.ljust(30) + " | " + f"R${pedido.total:.2f}".ljust(10)  + " | " + str(data_format(pedido.data)).ljust(10))
                print("\n\nOpções:\n")
                print("0. Voltar")
                opcao = input("\nEscolha uma opção: ")
                if opcao == '0':
                    cls()
                    print("Voltando...")
                    sleep(0.4)
                    cls()
                    break
                else:
                    cls()
                    print("\nOops, opção inválida! Tente novamente...")
                    sleep(0.7)
        except AttributeError:
            cls()
            print("Um erro desconhecido foi encontrado.")
            sleep(1.5)
            cls()
            return

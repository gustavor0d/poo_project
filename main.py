from sorveteria import cls, cadastrar_sorveteria, cadastrar_sabor, cadastrar_cliente, realizar_pedido, listar_pedidos, listar_sorveterias, listar_clientes

def menu():
    
    while True:
        print("\nMenu:\n"
            "1. Cadastrar Sorveteria\n"
            "2. Cadastrar Sabor\n"
            "3. Cadastrar Cliente\n"
            "4. Realizar Pedido\n"
            "5. Listar Pedidos\n"
            "6. Listar Sorveterias\n"
            "7. Listar Clientes\n"
            "0. Sair")

        match(input("\nEscolha uma opção: ")):
            case '1':
                cls()
                cadastrar_sorveteria()
            case '2':
                cls()
                cadastrar_sabor()
            case '3':
                cls()
                cadastrar_cliente()
            case '4':
                cls()
                realizar_pedido()
            case '5':
                cls()
                listar_pedidos()
            case '6':
                cls()
                listar_sorveterias()
            case '7':
                cls()
                listar_clientes()
            case '0':
                cls()
                print("\nPrograma finalizado.\n")
                break
            case _:
                cls()
                print("\nOpção inválida! Tente novamente.")

if __name__ == '__main__':
    menu()

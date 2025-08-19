from CRUD_Pedidos import(
    fazer_pedido,
    listar_pedido,
    atualizar_pedido,
    remover_pedido,
    fechar_conta
)

from CRUD_Cardapio import(
    adicionar_prato,
    listar_cardapio,
    atualizar_prato,
    remover_prato
)

from CRUD_Mesas import(
    criar_mesa,
    listar_mesas,
    atualizar_mesa,
    remover_mesa
)


from config import pratos_ref
from config import mesas_ref
from config import pedidos_ref


def menu():
    while True:
        print("----- RESTAURANTE DOS CRUDES -----")
        print("1- Cardápio")
        print("2- Pedidos")
        print("3- Mesas")
        print("0- Sair")
        resposta = int(input("Digite a opção desejada: "))

        if resposta == 1: 
            while True:
                print("-- Cardápio --")
                print("1- Adicionar Prato")
                print("2- Listar Cardápio")
                print("3- Atualizar Prato")
                print("4- Remover Prato")
                print("0- Voltar ao Menu Principal")
                opcao1 = int(input("Digite a opção desejada: "))

                if opcao1 == 1: 
                    adicionar_prato()
                elif opcao1 == 2:
                    listar_cardapio()
                elif opcao1 == 3:
                    if not pratos_ref.get():
                        print("Não há pratos salvos no banco de dados, por favor crie um prato antes de utilizar essa função.")
                    else:
                        atualizar_prato()
                elif opcao1 == 4:
                    if not pratos_ref.get():
                        print("Não há pratos salvos no banco de dados, por favor crie um prato antes de utilizar essa função.")
                    else:
                        remover_prato()
                elif opcao1 == 0:
                    print("Voltando ao Menu Principal...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif resposta == 2:
            while True:
                print("-- Pedidos --")
                print("1- Fazer Pedido")
                print("2- Listar Pedidos")
                print("3- Atualizar Status do Pedido")
                print("4- Remover pedido")
                print("5- Fechar Conta")
                print("0- Voltar ao Menu Principal")
                opcao2 = int(input("Digite a opção desejada: "))
            
                if opcao2 == 1:
                    if not mesas_ref.get or not pratos_ref.get():
                        print("Não há mesas ou pratos salvas no banco de dados, por favor crie uma mesa ou um prato antes de utilizar essa função.")
                    else:
                        fazer_pedido()
            
                elif opcao2 == 2:
                    listar_pedido()
            
                elif opcao2 == 3:
                    if not pedidos_ref.get():
                        print("Não há pedidos salvos no banco de dados, por favor crie um pedido antes de utilizar essa função.")
                    else:
                        atualizar_pedido()
            
                elif opcao2 == 4:
                    if not pedidos_ref.get():
                        print("Não há pedidos salvos no banco de dados, por favor crie um pedido antes de utilizar essa função.")
                    else:
                        remover_pedido()

                elif opcao2 == 5:
                    if not pedidos_ref.get():
                        print("Não há pedidos salvos no banco de dados, por favor crie um pedido antes de utilizar essa função.")
                    else:
                        fechar_conta()

                elif opcao2==0:
                    print("Voltando ao Menu Principal...")
                    break

        elif resposta == 3:
         while True:
            print("--- Mesas ---")
            print("1- Criar Mesa")
            print("2- Listar Mesas")
            print("3- Atualizar Mesa")
            print("4- Remover Mesa")
            print("0- Voltar ao Menu Principal")
            opcao3 = int(input("Digite a opção desejada: "))

            if opcao3==1:
                criar_mesa()

            elif opcao3==2:
                listar_mesas()

            elif opcao3==3:
                if not mesas_ref.get():
                    print("Não há mesas salvas no banco de dados, por favor crie uma mesa antes de utilizar essa função.")
                else:
                    atualizar_mesa()

            elif opcao3==4:
                if not mesas_ref.get():
                    print("Não há mesas salvas no banco de dados, por favor crie uma mesa antes de utilizar essa função.")
                else:
                    remover_mesa()

            elif opcao3==0:
                print("Voltando ao Menu Principal...")
                break

        elif resposta==0:
         print("Saindo do programa...")
         break

        else:
            print("Opção inválida.")
    
menu()
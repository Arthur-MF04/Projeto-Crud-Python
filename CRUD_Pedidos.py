from config import pratos_ref
from config import mesas_ref
from config import pedidos_ref

def fazer_pedido():
    finalizar = False
    while True:
        num_mesa = int(input("Digite o número da mesa: "))

        if num_mesa < 1:
            print("Por favor, insira um número positivo para a mesa.")
            continue

        mesa_ref = mesas_ref.child(str(num_mesa))
        if mesa_ref.get() is None:
            print(f"Essa mesa não existe. Tente novamente.")
            continue

        break
        
    while not finalizar:
        while True:
            pedido_id = int(input("Diga a ID (número) do pedido: ")) 
            
            if pedido_id < 1:
                print("ID inválida. Digite um inteiro.")
                continue

            if pedidos_ref.child(str(pedido_id)).get() is not None:
                print("Essa ID já existe. Escolha outra.")
                continue

            break

        while True:
            nome_prato = input("Digite o nome do prato: ").lower()
            prato = pratos_ref.child(nome_prato).get()
            if prato is None:
                print("Prato não encontrado.")
                continue
            break

        pedido_dict = {
            "id": pedido_id,
            "prato": prato["nome"],
            "preco": prato["preco"],
            "mesa": num_mesa,
            "status": "c"
        }
        pedidos_ref.child(str(pedido_id)).set(pedido_dict)
        print(f"Pedido {pedido_id} criado para a mesa {num_mesa}.")
        resposta = input("Deseja fazer outro pedido para a mesma mesa? [S/N]: ").lower()
        if resposta == 'n':
            finalizar = True


def listar_pedido():
    dados = pedidos_ref.get()
    if not dados:
        print("Não há pedidos cadastrados.")
        return
    
    registros = dados.values() if isinstance(dados, dict) else dados
    registros = [p for p in registros if isinstance(p, dict)]

    print("\n--- Pedidos ---")
    for pedido in registros:
        nome_prato = pedido.get('prato')
        preco_prato = pratos_ref.child(nome_prato).child('preco').get()
        status = pedido.get('status')
        descricao = ""

        if status == 'c':
            descricao = 'Cozinhando'
        elif status == 'p':
            descricao = 'Preparando'
        elif status == 'e':
            descricao = 'Entregue'

        print(f"Id:     {pedido.get('id')}")
        print(f"Prato:  {nome_prato}")
        print(f"Preço:  R${float(preco_prato):.2f}")
        print(f"Mesa:   {pedido.get('mesa')}")
        print(f"Status: {descricao}")
        print("-"*20)


def atualizar_pedido():
    id_pedido = int(input("Digite a ID do pedido: "))

    pedido_ref = pedidos_ref.child(str(id_pedido))
    if pedido_ref.get() is None:
        print(f"ID {id_pedido} não encontrado.")
        return

    while True:
        print("Digite o novo status do pedido:")
        print("C - Cozinhando")
        print("P - Preparado")
        print("E - Entregue")
        novo_status = input("Status [C/P/E]: ").lower()
        if novo_status in ('c', 'p', 'e'):
            break
        print("Status inválido, tente novamente.")

    pedido_ref.update({"status": novo_status})
    print(f"Pedido {id_pedido} atualizado com sucesso.")



def remover_pedido():
    id_pedido = int(input("Digite a ID do pedido: "))

    pedido_ref = pedidos_ref.child(str(id_pedido))
    if pedido_ref.get() is None:
        print(f"ID {id_pedido} não encontrado.")
        return

    pedido_ref.delete()
    print(f"Pedido {id_pedido} removido com sucesso.")


def fechar_conta():
    mesa_num = int(input("Digite o número da mesa: "))

    pedidos_mesa = pedidos_ref.order_by_child('mesa').equal_to(mesa_num).get()
    if not pedidos_mesa:
        print("Esta mesa não possui pedidos.")
        return

    total = 0.0
    print(f"\n--- Pedidos da mesa {mesa_num} ---")
    for pedido, dados in pedidos_mesa.items():
        nome_prato = dados.get('prato')
        preco = pratos_ref.child(nome_prato).child('preco').get()
        print(f"Pedido {pedido}: {nome_prato} — R$ {float(preco):.2f}")
        total += float(preco)
    print(f"\nTotal a pagar: R${total:.2f}")

    resposta = input("A conta foi paga? [S/N]: ").lower()
    if resposta == 's':
        for pedido in pedidos_mesa.keys():
            pedidos_ref.child(pedido).delete()
        print("Conta fechada, todos os pedidos dessa mesa foram removidos.")
    else:
        print("Conta ainda aberta.")
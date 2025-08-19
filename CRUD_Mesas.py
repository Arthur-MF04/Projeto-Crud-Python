from config import mesas_ref

def criar_mesa():
    print("--- Criando Mesa ---")
    num_mesa=int(input("Digite o número da mesa: "))

    while num_mesa < 1:
        print("Por favor, insira um número positivo para a mesa.")
        num_mesa=int(input("Digite o número da mesa: "))

    mesa_ref = mesas_ref.child(str(num_mesa))
    if mesa_ref.get() is not None:
        print("Essa mesa já está cadastrada.")
        return


    while True:
        print("Digite o status da mesa (D, R, O, I):")
        print("D - Disponível")
        print("R - Reservado")
        print("O - Ocupado")
        print("I - Indisponível")
        status = input().lower()
        if status in ('d', 'r', 'o', 'i'):
            break
        print("Status inválido. Tente novamente.")

    mesa_dict = {
        'numero': num_mesa,
        'status': status
    }
    mesa_ref.set(mesa_dict)
    print("Mesa criada com sucesso.")

def listar_mesas():
    todas = mesas_ref.get()
    if not todas:
        print("Não há mesas cadastradas.")
        return
    
    mesas_ordenadas = sorted(
        (m for m in todas.values() if isinstance(m, dict)),
        key=lambda m: m.get('numero', 0)
    )

    print("\n-- Mesas --")
    for m in mesas_ordenadas:
        numero = m.get('numero')
        status_code = m.get('status')
        status = {
            'd': 'Disponível',
            'r': 'Reservado',
            'o': 'Ocupado'
        }.get(status_code, 'Indisponível')
        print(f"Mesa {numero}: status: {status}")
        

def atualizar_mesa():
    print("--- Atualizando Mesa ---")
    num_mesa = int(input("Digite o número da mesa que deseja atualizar: "))

    mesa_ref = mesas_ref.child(str(num_mesa))
    if mesa_ref is None:
        print("Mesa não encontrada.")
        return


    while True:
        print("Digite o novo status da mesa (D, R, O, I):")
        print("D - Disponível")
        print("R - Reservado")
        print("O - Ocupado")
        print("I - Indisponível")
        status_mesa = input().lower()

        if status_mesa in ('d', 'r', 'o', 'i'):
            break
        print("Status inválido. Tente novamente.")

    mesa_ref.update({'status': status_mesa})
    print("Mesa atualizada com sucesso.")

def remover_mesa():
    print("--- Removendo Mesa ---")
    num_mesa = int(input("Digite o número da mesa que deseja remover: "))

    mesa_ref = mesas_ref.child(str(num_mesa))
    if mesa_ref.get() is None:
        print("Mesa não encontrada.")
        return

    mesa_ref.delete()
    print("Mesa removida com sucesso.")

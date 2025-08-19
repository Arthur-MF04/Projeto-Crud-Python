from config import pratos_ref
 
def adicionar_prato():
    while True:
        nome = input("Nome do prato: ").lower()
        if not nome:
            print("O nome do prato é necessário para continuar.")
        else:
            break
    if pratos_ref.child(nome).get() is not None:
        print("Esse prato já está cadastrado.")
        return

    descricao = input("Descrição: ")
    ingredientes = input("Ingredientes: ")
    preco = float(input("Preço: "))
    categoria = input("Categoria: ")

    prato_dict = {
        "nome": nome,
        "descricao": descricao,
        "ingredientes": ingredientes,
        "preco": preco,
        "categoria": categoria
    }

    pratos_ref.child(nome).set(prato_dict)
    print("Prato adicionado com sucesso.")

def listar_cardapio():
    cardapio = pratos_ref.get()
    if not cardapio:
        print("Cardápio vazio.")
        return

    print("\n-- Cardápio --")
    for dados in cardapio.values():
        print(f"Nome: {dados.get('nome')}")
        print(f"Descrição: {dados.get('descricao')}")
        print(f"Ingredientes: {dados.get('ingredientes')}")
        print(f"Preço: R${dados.get('preco', 0):.2f}")
        print(f"Categoria: {dados.get('categoria')}")
        print("-" * 20)


def atualizar_prato():
    nome = input("Digite o nome do prato que deseja atualizar: ").lower()
    dados_prato = pratos_ref.child(nome).get()
    if dados_prato is None:
        print("Prato não encontrado no cardápio.")
        return

    print(f"Prato encontrado: {nome}")
    print("Você pode apertar Enter para manter os dados já salvos.")

    while True:
        novo_nome = input("Novo nome: ")
        if not novo_nome:
            novo_nome = nome 
            break
        if pratos_ref.child(novo_nome).get() is not None:
            print("Este nome já está cadastrado. Tente outro.")
        else:
            break
    nova_descricao = input(f"Nova descrição [{dados_prato.get('descricao')}]: ") or dados_prato.get('descricao')
    novos_ingredientes = input(f"Novos ingredientes [{dados_prato.get('ingredientes')}]: ") or dados_prato.get('ingredientes')
    novo_preco_input = input(f"Novo preço [{dados_prato.get('preco')}]: ")
    if novo_preco_input:
        novo_preco = float(novo_preco_input)
    else:
        novo_preco = dados_prato.get('preco')   

    nova_categoria = input(f"Nova categoria [{dados_prato.get('categoria')}]: ") or dados_prato.get('categoria')

    
    if novo_nome != nome:
        pratos_ref.child(novo_nome).set({
            "nome": novo_nome,
            "descricao": nova_descricao,
            "ingredientes": novos_ingredientes,
            "preco": novo_preco,
            "categoria": nova_categoria
        })
        pratos_ref.child(nome).delete()

    else:
        pratos_ref.child(nome).update({
            "descricao": nova_descricao,
            "ingredientes": novos_ingredientes,
            "preco": novo_preco,
            "categoria": nova_categoria
        })

    print("Prato atualizado com sucesso.")

def remover_prato():
    nome = input("Digite o nome do prato que deseja remover: ").lower()

    prato_ref = pratos_ref.child(nome)
    if prato_ref.get() is None:
        print("Prato não encontrado no cardápio.")
        return

    prato_ref.delete() 
    print("Prato removido com sucesso.")
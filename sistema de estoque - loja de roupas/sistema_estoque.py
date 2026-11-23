estoque =   {"camisetas": 
                {"camiseta 1": {"valor": 49.99, "quantidade": 20}, 
                "camiseta 2": {"valor": 59.99, "quantidade": 22}},
            "calcas": 
                {"calca 1": {"valor": 99.99, "quantidade": 6}, 
                "calca 2": {"valor": 119.99, "quantidade": 20}}
            }

carrinho = {}

def formatar_exibicao(texto):
    return texto.replace("calcas", "calças").replace("calca", "calça")

def finalizar_compra(carrinho, estoque):
    if not carrinho:
        print("\nSeu carrinho está vazio.")
        return
    valor_total = 0
    print("CARRINHO")
    for produto, dados in carrinho.items():
        quantidade = dados["quantidade"]
        valor = dados["valor"]
        valor_total += dados["valor"]
        print(f"""
{formatar_exibicao(produto).upper()}
Quantidade: {quantidade}
Valor: R${valor:.2f}""")
    print(f"\nValor Total: R${valor_total:.2f}")
    for produto, dados in carrinho.items():
        categoria = dados["categoria"]
        quantidade = dados["quantidade"]
        estoque[categoria][produto]["quantidade"] -= quantidade
    carrinho.clear()
    print("\nCompra realizada!!!")
        
def mostrar_carrinho (carrinho):
    print("CARRINHO")
    if not carrinho:
        print("\nSeu carrinho está vazio.")
        return
    valor_total = 0
    for produto, dados in carrinho.items():
        quantidade = dados["quantidade"]
        valor = dados["valor"]
        valor_total += dados["valor"]
        print(f"""
{formatar_exibicao(produto).upper()}
Quantidade: {quantidade}
Valor: R${valor:.2f}""")
    print(f"\nValor Total: R${valor_total:.2f}")
    
    while True:
        try:
            escolha = int(input("""Escolha uma das opções:
1- Limpar Carrinho
2- Voltar
: """))
            
            if escolha == 1:
                carrinho.clear()
                print("\nCarrinho limpo!")
                return
            elif escolha == 2:
                return
            else:
                print("Digite uma opção válida")
        except ValueError:
            print("Digite uma opção válida")
            continue
def adicionar_carrinho (produto, nome_categoria, quantidade_desejada, carrinho, total_produto):
    if produto in carrinho:
        carrinho[produto]["quantidade"] += quantidade_desejada
        carrinho[produto]["valor"] += total_produto
    else:
        carrinho[produto] = {
            "categoria": nome_categoria,
            "quantidade": quantidade_desejada, 
            "valor": total_produto
        }
    return
            
def calcular (estoque, nome_categoria, produto, quantidade_desejada, carrinho):
    total_produto = estoque[nome_categoria][produto]["valor"] * quantidade_desejada
    adicionar_carrinho(produto, nome_categoria, quantidade_desejada, carrinho, total_produto)
    print(f"""
    Adicionado ao carrinho!!
    Total: R${total_produto:.2f}
    Quantidade: {quantidade_desejada}""")
    return

def validar_quantidade (estoque, nome_categoria, produto, quantidade_desejada, carrinho):
    disponivel = estoque[nome_categoria][produto]["quantidade"]
    no_carrinho = carrinho[produto]["quantidade"] if produto in carrinho else 0
    restante = disponivel - no_carrinho
    if quantidade_desejada < 0:
        print("\nDigite uma quantidade maior que 0.\n")
        return False
    elif quantidade_desejada > restante:
        print(f"\nEstoque insuficiente. Disponível para adicionar: {restante}.\n")
        return False
    else:
        return True
    
while True:
    try:
        menu = int(input("""
Seja bem-vindo(a) a loja de roupas!
        
O que deseja explorar?
        
1 - CAMISETAS
2 - CALÇAS
3 - Ver Carrinho
4 - Finalizar Compra
5 - Sair
        
: """))
        
        if menu == 5:
            print("\nSaindo...")
            break
        elif menu == 1:
            nome_categoria = "camisetas"
        elif menu == 2:
            nome_categoria = "calcas"
        elif menu == 3:
            mostrar_carrinho(carrinho)
            continue
        elif menu == 4:
            finalizar_compra(carrinho, estoque)
            continue
        else:
            print("\nDigite uma opção válida.")
            continue
        print("")
    except ValueError:
        print("\nDigite uma opção válida.")
        continue
    
    while True:

        print(f"{formatar_exibicao(nome_categoria).upper()}")
        
        for produto, dados in estoque[nome_categoria].items():
            preco = dados["valor"]
            quantidade_total = dados["quantidade"]
            print(f"""
            {formatar_exibicao(produto).upper()}
            Preço: R${preco:.2f}
            Quantidade: {quantidade_total}
            """)
            
        produto = input("Digite a peça que deseja ou 0 para voltar: ").replace("ç", "c").replace("Ç", "C").strip().lower()
        if produto == "0":
            break
        if produto not in estoque[nome_categoria]:
            print("Digite uma peça válida.\n")
            continue
        else:
            while True:
                try:
                    quantidade_desejada = int(input("Digite a quantidade deseja ou 0 para voltar: "))
                except ValueError:
                    print("\nDigite uma quantidade válida.\n")
                    continue
                if quantidade_desejada == 0:
                    break
                if validar_quantidade(estoque, nome_categoria, produto, quantidade_desejada, carrinho):
                    calcular(estoque, nome_categoria, produto, quantidade_desejada, carrinho)
                    break
                else:
                    continue
        break
        
        
        
        
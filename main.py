from repositorio import Repositorio
from item import Item 


    
    

class Copo: 
    def __init__(self):
        self.carregar_repositorios()
        
        self.iniciar()
        
    def iniciar(self):
        while True: 
            self.tela_principal()
            
            entrada = input("\nInsira: ")
            if entrada == '1':
                self.tela_cadastrar_copo()
            elif entrada == '2':
                self.tela_cadastrar_subreceita(salvar=True)
            elif entrada == '3':
                self.tela_cadastrar_ingrediente()
            elif entrada == '4':
                self.tela_cadastrar_embalagens()
            elif entrada == '9':
                self.consultar_banco()
            elif entrada == '0':
                break
            else:
                print("\nInsira uma opção válida")
                
    def carregar_repositorios(self):
        self.repo = Repositorio()
        self.ingredientes = self.repo.ingredientes
        self.subreceitas = self.repo.subreceitas
        self.embalagens = self.repo.embalagens
    
    def tela_principal(self):
        print("1 - Cadastrar copo")
        print("2 - Cadastrar subreceita")
        print("3 - Cadastrar ingrediente")
        print("4 - Cadastrar embalagens")
        print("9 - Consultar banco de dados")
        print("0 - Sair")
    
    def tela_cadastrar_subreceita(self, salvar=False):
        ingredientes_subreceitas = []
        print("**INGREDIENTES**")
        print("\nINSIRA QUAIS INGREDIENTES E QUAIS QUANTIDADES, insira 0 para sair")
        print("exemplo: 'ingrediente' 'quantidade em gramas' ")
        print("")
        self.mostrar_ingredientes()
        
        if salvar:
            nome_receita = input("\nInsira o nome da receita: ").capitalize()
        
        while True:                
            inp = input("Insira: ")
            
            if inp == '0':
                break
            
            ing, qtd  = int(inp.split()[0]), float(inp.split()[1])
            
            ingr = self.localizar_item(ing, self.ingredientes)
            print(f"escolhido: {ingr.nome}\n")

            ingredientes_subreceitas.append((ing, qtd))

        quantidade = sum(map(lambda x: x[1], ingredientes_subreceitas))
        valor = self.calcular(ingredientes_subreceitas, self.ingredientes)
        print(f"Valor: {valor}, Quantidade: {quantidade}")
        if salvar:
            self.salvar_items(quantidade, 'gramas', nome_receita, valor, 'subreceitas')
            self.salvar_items(quantidade, 'gramas', nome_receita, valor, 'ingredientes')
        
        else:
            return quantidade, valor
        input("\nAPERTE QUALQUER TECLA PARA CONTINUAR\n")
        
    def tela_cadastrar_copo(self):
        
        subreceitas_usados = []
        
        print("\n**SUBRECEITAS\n**")
        print("\nINSIRA QUAIS SUBRECEITAS E QUAIS QUANTIDADES, insira 0 para sair")
        print("exemplo: 'subreceita' 'quantidade em gramas' ")
        print("")
        self.mostrar_subreceitas()
        #nome_copo = input("Insira o nome da receita: ")
        
        while True:                
            inp = input("\nInsira: ")
            
            if inp == '0':
                break
            
            subrec, qtd  = int(inp.split()[0]), float(inp.split()[1])
            
            item = self.localizar_item(subrec, self.subreceitas)
            print(f"escolhido: {item.nome}\n")

            subreceitas_usados.append((subrec, qtd))

        quantidade = sum(map(lambda x: x[1], subreceitas_usados))
        valor = self.calcular(subreceitas_usados, self.subreceitas)
        
        print(f"Valor: {valor}")
        
        qtd_ing, valor_ing = self.tela_cadastrar_subreceita()
        
        quantidade += qtd_ing 
        valor+= valor_ing
        
        valor_embalagem = self.tela_selecionar_embalagens()
        
        valor+= valor_embalagem
        
        preco_final = float(input("Insira o preço do copo: "))
        tx_ifood = 0.27
        
        valor += preco_final * tx_ifood 
        print(f"VALOR COPO: {valor}")
        
        input("\nAPERTE QUALQUER TECLA PARA CONTINUAR\n")
    
    def mostrar_subreceitas(self):
        for subreceita in sorted(self.subreceitas, key= lambda x: x.nome):
            if len(str(subreceita.id)) == 2:                
                print(f"{subreceita.id}- {subreceita.nome}") 
            else:
                print(f"{subreceita.id} - {subreceita.nome}") 
        
        
    def mostrar_ingredientes(self):
        for ingrediente in sorted(self.ingredientes, key= lambda x: x.nome):
            if len(str(ingrediente.id)) == 2:                
                print(f"{ingrediente.id}- {ingrediente.nome}") 
            else:
                print(f"{ingrediente.id} - {ingrediente.nome}") 
                
    def mostrar_embalagens(self):
        for embalagem in sorted(self.embalagens, key= lambda x: x.nome):
            if len(str(embalagem.id)) == 2:                
                print(f"{embalagem.id}- {embalagem.nome}") 
            else:
                print(f"{embalagem.id} - {embalagem.nome}") 
                
    def localizar_item(self, id, lista):
        for item in lista:
            if item.id == id:
                return item 


    def consultar_banco(self):
        print("\n**INGREDIENTES**\n")
        print(f"{'Id'.center(4)}| {'Quantidade'.center(7)} |" + f" {'Ingrediente'.center(20)} |" + f" {'Valor'.center(10)} |" + f" {'Valor Unitário'.center(10)} |")
        print("-"*(74))
        for item in sorted(self.ingredientes, key= lambda x: x.nome):
            print(f"{str(item.id).center(4)} {f'{str(item.unidade)}g'.center(13)} {item.nome[:20].ljust(22)} {f'{item.valor:.2f}'.ljust(14)} {f'{item.valor_unitario():.4f}'.ljust(10)} ")
            
        print()
        print("**SUBRECEITAS**\n")
        print(f"{'Id'.center(4)}| {'Quantidade'.center(7)} |" + f" {'Ingrediente'.center(20)} |" + f" {'Valor'.center(10)} |" + f" {'Valor Unitário'.center(10)} |")
        print("-"*(74))
        for item in sorted(self.subreceitas, key= lambda x: x.nome):
            print(f"{str(item.id).center(4)} {f'{str(item.unidade)}g'.center(13)} {item.nome[:20].ljust(22)} {f'{item.valor:.2f}'.ljust(14)} {f'{item.valor_unitario():.4f}'.ljust(10)} ")
            
        print()
        
        print("**EMBALAGENS**\n")
        print(f"{'Id'.center(4)}| {'Quantidade'.center(7)} |" + f" {'Ingrediente'.center(20)} |" + f" {'Valor'.center(10)} |" + f" {'Valor Unitário'.center(10)} |")
        print("-"*(74))
        for item in sorted(self.embalagens, key= lambda x: x.nome):
            print(f"{str(item.id).center(4)} {f'{str(item.unidade)}'.center(13)} {item.nome[:20].ljust(22)} {f'{item.valor:.2f}'.ljust(14)} {f'{item.valor_unitario():.4f}'.ljust(10)} ")
        print()
        
        
    def tela_selecionar_embalagens(self):
        embalagens_selecionadas = []
        print("\n**EMBALAGENS**\n")
        print("\nINSIRA QUAIS EMBALAGENS, insira 0 para sair")
        print("exemplo: 'embalagem1' ")
        print("")
        self.mostrar_embalagens()
        
        while True:                
            inp = input("Insira: ")
            
            if inp == '0':
                break
            
            emb =  int(inp)
            
            embal = self.localizar_item(emb, self.embalagens)
            print(f"escolhido: {embal.nome}\n")
            embalagens_selecionadas.append(embal)

        valor = sum(map(lambda x: x.valor_unitario(), embalagens_selecionadas))
        print(f"Valor Embalagens: {valor}\n")

        input("APERTE QUALQUER TECLA PARA CONTINUAR")

        return valor
        
        
    def calcular(self, lista_items_usados, lista_items):
        valor = 0 
        for item in lista_items_usados:
            item_objeto = self.localizar_item(item[0], lista_items)
            custo = item_objeto.valor_unitario() * item[1]
            valor += custo
        
        return valor
        
    def tela_cadastrar_ingrediente(self):
        print("\n**CADASTRO INGREDIENTES**\n")
        nome = input("Insira o nome do item: ").capitalize()
        quantidade = input("Insira o peso em gramas: ")
        valor = input("Insira o valor do item: ")
        self.salvar_items(quantidade, 'gramas', nome, valor, 'ingredientes')
        
    def tela_cadastrar_embalagens(self):
        print("\n**CADASTRO EMBALAGENS**\n")
        nome = input("Insira o nome do item: ").capitalize()
        quantidade = input("Insira a quantidade: ")
        valor = input("Insira o valor do item: ")
        self.salvar_items(quantidade, 'gramas', nome, valor, 'embalagens')
        
    def salvar_items(self, quantidade, dimensao, nome, valor, tabela):
        try:    
            self.repo.salvar_items(quantidade, dimensao, nome, valor, tabela=tabela)
        except Exception as e:
            print(f"\nErro ao cadastrar: {e}\n")
        else:
            print("\nCadastrado com sucesso!!\n")
            self.carregar_repositorios()
            
if __name__ == "__main__":
    Copo()  
class Item:
    def __init__(self, id, unidade, dimensao, nome, valor):
        self.id = id
        self.unidade = unidade
        self.dimensao = dimensao
        self.nome = nome
        self.valor = valor
        
    def valor_unitario(self):
        try:
            div = self.valor / self.unidade 
        except ZeroDivisionError:
            return 0
        else:
            return div

if __name__ == '__main__':
    Item() 
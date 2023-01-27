from database import Database
from item import Item 

class Repositorio:
    def __init__(self):
        self.ingredientes = []
        self.subreceitas = []
        self.embalagens = []
        self.db = Database()
        self.popular_ingredientes()
        self.popular_subreceitas()
        self.popular_embalagens()
        
    def popular_ingredientes(self):
        self.db.conectar()
        leitura_banco = self.db.ler('ingredientes')
        self.db.fechar()
        for linha in leitura_banco:
            item = Item(
                id= linha[0],
                unidade=linha[1],
                dimensao = linha[2],
                nome = linha[3],
                valor = linha[4])
            
            self.ingredientes.append(item )
    
    def popular_subreceitas(self):
        self.db.conectar()
        leitura_banco = self.db.ler('subreceitas')
        self.db.fechar()
        for linha in leitura_banco:
            item = Item(
                id= linha[0],
                unidade=linha[1],
                dimensao = linha[2],
                nome = linha[3],
                valor = linha[4])
            
            self.subreceitas.append(item )
            
    def popular_embalagens(self):
        self.db.conectar()
        leitura_banco = self.db.ler('embalagens')
        self.db.fechar()
        for linha in leitura_banco:
            item = Item(
                id= linha[0],
                unidade=linha[1],
                dimensao = linha[2],
                nome = linha[3],
                valor = linha[4])
            
            self.embalagens.append(item )
            
    def salvar_items(self, *args, tabela=''):
        self.db.conectar()
        self.db.salvar_items(*args, tabela=tabela)
        self.db.fechar()
if __name__ == '__main__':
    Repositorio()
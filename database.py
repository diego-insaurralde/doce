import sqlite3 as db
import csv

class Database:
    
    def __init__(self):
        pass
        
    
    def conectar(self):
        self.conn =  db.connect('dellacacau.db')
        self.cursor = self.conn.cursor()
        
    def fechar(self):
        self.conn.close()
    
    def criar_tabela(self, nome_tabela):
        self.cursor.execute(f""" 
        CREATE TABLE IF NOT EXISTS {nome_tabela} (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            unidade REAL NOT NULL,
            dimensao TEXT NOT NULL,
            nome TEXT NOT NULL, 
            valor REAL NOT NULL          

        );
        """)
    def salvar(self):
        with open('excel.csv', 'r',  ) as f:
            reader = csv.reader(f)
            for i, line in enumerate(reader):
                if i == 0:
                    continue
            
                self.cursor.execute("""
                INSERT INTO ingredientes (unidade, dimensao, nome, valor)
                VALUES (?,?,?,?)
                """, line)
                self.conn.commit()
                
    def ler(self, tabela):
        self.cursor.execute(f"""
        SELECT * FROM {tabela};
        """)
        
        return self.cursor.fetchall()
    
    def salvar_unico(self):
        lista = [1000, 'gramas', 'Biscoito Triturado', 23.50]
        self.cursor.execute("""
                INSERT INTO ingredientes (unidade, dimensao, nome, valor)
                VALUES (?,?,?,?)
                """, lista)
        self.conn.commit()
    
    def salvar_items(self, *args, tabela=''):
        self.cursor.execute(f"""
                INSERT INTO {tabela} (unidade, dimensao, nome, valor)
                VALUES (?,?,?,?)
                """, args)
        self.conn.commit()
    
    def deletar(self, tabela, id):
        try:
            self.cursor.execute(f"""
                    DELETE FROM {tabela} WHERE id = {id} 
                    """)
            self.conn.commit()
        except Exception as e:
            print(f"Erro: {e}")
        else:
            print("Deletado com sucesso")

    
    def atualizar(self, tabela, id, campo, valor ):
        try:
            self.cursor.execute(f"""
                    UPDATE {tabela} 
                    SET {campo} = {valor}
                    WHERE id = {id}
                    """)
            self.conn.commit()
        except Exception as e:
            print(f"Erro: {e}")
        else:
            print("Atualizado com sucesso")
if __name__ == '__main__':
    banco = Database()
    banco.conectar()
    #banco.criar_tabela('embalagens')
    banco.deletar('ingredientes', 20)
    #banco.atualizar('ingredientes', 17, 'unidade', 129)
        
    #banco.criar_tabela('subreceitas')
    banco.fechar()

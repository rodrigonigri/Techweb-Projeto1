import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, name):
        '''
        Construtor: cria uma nova base de dados com o nome passado
        '''
        self.name = name
        self.conn = sqlite3.connect(self.name+'.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title STRING, content TEXT NOT NULL);')
        return None

    def add(self, note):
        '''
        Recebe um argumento do tipo Note, e insere seus dados no banco. 
        '''
        self.conn.execute("INSERT INTO note (title, content) VALUES ('{title}', '{content}');".format(title = note.title, content = note.content))
        self.conn.commit()
        return None
    
    def get_all(self):
        '''
        Não recebe nada, e devolve uma lista de Notes do banco de dados
        '''
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        self.conn.commit()
        result = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            lista = Note(id,title,content)
            result.append(lista)
        return result

    def update(self, entry):
        '''
        Recebe um Note e atualiza essa entrada no banco de dados
        '''
        self.conn.execute("UPDATE note SET title = '{title}', content = '{content}' WHERE id = '{id}'".format(title = entry.title, content = entry.content, id = entry.id))
        self.conn.commit()
        return None

    def delete(self, note_id):
        '''
        Recebe o valor de um id, e apaga essa entrada do banco de dados
        '''
        self.conn.execute("DELETE FROM note WHERE id = {id}".format(id = note_id))
        self.conn.commit()
        return None


from typing import Text
import json
from database import Database


def extract_route(request):
    '''
    Recebe um request e devolve a rota sem "/" 
    '''
    return request.split('\n')[0].split(' ')[1].replace('/', '', 1)



def read_file(path):
    '''
    Recebe um path e devolve o conteúdo do arquivo
    '''
    with open(path, 'rb') as f:
        return f.read()



def load_data(nome_arquivo):
    with open("data/"+ nome_arquivo,  encoding='utf-8') as arquivo_json:

        dicionario = json.load(arquivo_json)
    return dicionario



def load_template(filename):
    with open("templates/" + filename, 'r', encoding='utf-8') as file:
        return file.read()



def add_note(anotacao):
    with open ("data/notes.json", encoding="UTF-8") as notes:
        conteudo = json.load(notes)
    conteudo.append(anotacao)

    with open ("data/notes.json", "w", encoding='UTF-8') as notes:
        json.dump(conteudo, notes, ensure_ascii=False)



def build_response(body='', code=200, reason='OK', headers=''):
    if body == '' and headers == "": # SEM BODY E HEADER
        return (f'HTTP/1.1 {code} {reason}\n\n').encode()

    elif body != '' and headers == "": # COM BODY
        return (f'HTTP/1.1 {code} {reason}\n\n{body}').encode()

    elif body == '' and headers != "": # COM HEADER
        return (f'HTTP/1.1 {code} {reason}\n{headers}\n\n').encode()

    elif body != '' and headers != "": # COM HEADER E BODY
        return (f'HTTP/1.1 {code} {reason}\n {headers}\n\n{body}').encode()



from os import error, replace
from utils import load_data, load_template, add_note, build_response
import urllib
from database import Database, Note

banco = Database("banco")

def index(request):
    '''
    Recebe uma request (POST / HTTP/1.1...)
    '''
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados

        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}

        for chave_valor in corpo.split('&'):
            params[chave_valor.split('=')[0]] = urllib.parse.unquote_plus(chave_valor.split('=')[1])

            print(params)

        #add_note(params)
        lista_valores = list(params.values())
        banco.add(Note(title=lista_valores[0], content=lista_valores[1]))

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content)
        for dados in banco.get_all()
    ]
    notes = '\n'.join(notes_li)

    if request.startswith('POST'):
        return build_response(code=303, reason='See Other', headers='Location: /') + load_template('index.html').format(notes=notes).encode()
    else:
        return build_response() + load_template('index.html').format(notes=notes).encode()

#https://ai.thestempedia.com/example/hash-table-search-in-python/
def criar_tabela_hash(tamanho):
    return [None] * tamanho

def hash_funcao(chave, tamanho):
    return sum(ord(c) for c in chave) % tamanho

def inserir_tabela_hash(tabela, chave, valor):
    indice = hash_funcao(chave, len(tabela))
    if tabela[indice] is None:
        tabela[indice] = [(chave, valor)]
    else:
        tabela[indice].append((chave, valor))

def buscar_tabela_hash(tabela, chave):
    indice = hash_funcao(chave, len(tabela))
    if tabela[indice] is None:
        return None
    else:
        for item in tabela[indice]:
            if item[0] == chave:
                return item[1]
    return None 

def executar():
    tabela_hash = criar_tabela_hash(10)
    inserir_tabela_hash(tabela_hash, "igor", {"nome": "Igor", "email": "igor@Gmail.com"})
    inserir_tabela_hash(tabela_hash, "maria", {"nome": "Maria", "email": "maria@gmail.com"})
    inserir_tabela_hash(tabela_hash, "joao", {"nome": "João", "email": "joao@gmail.com"})
    perfil_igor = buscar_tabela_hash(tabela_hash, "igor")
    perfil_maria = buscar_tabela_hash(tabela_hash, "maria")
    perfil_joao = buscar_tabela_hash(tabela_hash, "joao")
    print("Perfil de Igor:", perfil_igor)
    print("Perfil de Maria:", perfil_maria)
    print("Perfil de João:", perfil_joao)

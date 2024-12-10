def inserir(arvore, chave):
    if arvore is None:
        return {'chave': chave, 'esquerda': None, 'direita': None}
    if chave < arvore['chave']:
        arvore['esquerda'] = inserir(arvore['esquerda'], chave)
    else:
        arvore['direita'] = inserir(arvore['direita'], chave)
    return arvore

def buscar(arvore, chave):
    if arvore is None:
        return False
    if chave == arvore['chave']:
        return True
    elif chave < arvore['chave']:
        return buscar(arvore['esquerda'], chave)
    else:
        return buscar(arvore['direita'], chave)
    
def executar():
    precos =  [100,50,150,30,70,130,170]
    arvore_binaria = None
    for preco in precos:
        arvore_binaria = inserir(arvore_binaria, preco)
    preco_busca = 70
    encontrado = buscar(arvore_binaria, preco_busca)
    if encontrado:
        print(f"O preço {preco_busca} foi encontrado")
    else:
        print(f"O preço {preco_busca} não foi encontrado")

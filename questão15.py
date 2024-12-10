def executar():
    def inserir(arvore, chave):
        if arvore is None:
            return {'chave': chave, 'esquerda': None, 'direita': None}
        if chave < arvore['chave']:
            arvore['esquerda'] = inserir(arvore['esquerda'], chave)
        else:
            arvore['direita'] = inserir(arvore['direita'], chave)
        return arvore

    def nota_minima(arvore):
        while arvore['esquerda'] is not None:
            arvore = arvore['esquerda']
        return arvore['chave']
    def nota_maxima(arvore):
        while arvore['direita'] is not None:
            arvore = arvore['direita']
        return arvore['chave']


    notas = [85, 70, 95, 60, 75, 90, 100]
    arvore_binaria = None
    for nota in notas:
        arvore_binaria = inserir(arvore_binaria, nota)
    nota_minima = nota_minima(arvore_binaria)
    nota_maxima = nota_maxima(arvore_binaria)

    print(f"A menor nota é: {nota_minima}")
    print(f"A maior nota é: {nota_maxima}")


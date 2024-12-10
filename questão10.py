pilha_navegacao = []
pilha_avanco = []

def visitar_pagina(pagina):
    pilha_navegacao.append(pagina)
    pilha_avanco.clear()
    print(f"Visitando a página: {pagina}")

def voltar():
    if pilha_navegacao:
        pagina_atual = pilha_navegacao.pop()  
        pilha_avanco.append(pagina_atual)  
        if pilha_navegacao:
            print(f"Voltando para: {pilha_navegacao[-1]}")
        else:
            print("Você está na pagina inicial")
    else:
        print("Nenhuma página para voltar")

def avancar():
    if pilha_avanco:
        pagina_atual = pilha_avanco.pop() 
        pilha_navegacao.append(pagina_atual) 
        print(f"Avançando para: {pagina_atual}")
    else:
        print("Nenhuma página para ir alem")

def executar():
    visitar_pagina("Página 1")
    visitar_pagina("Página 2")
    visitar_pagina("Página 3")
    visitar_pagina("Página 4")
    voltar()
    avancar()
    voltar()
    avancar()

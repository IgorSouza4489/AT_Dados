fila = []

def add_chamado(chamado):
    fila.append(chamado)
    print(f"Chamado '{chamado}' adicionado à fila")

def att_chamado():
    if fila:
        chamado_atendido = fila.pop(0)  
        print(f"Chamado '{chamado_atendido}' atendido")
    else:
        print("Nenhum chamado na fila")

def mostrar_fila():
    if fila:
        print("Fila:", fila)
    else:
        print("A fila está vazia")

def executar():
    #testes de chamados
    add_chamado("Chamado 1")
    add_chamado("Chamado 2")
    mostrar_fila()
    att_chamado()  
    att_chamado()  
    mostrar_fila()
    add_chamado("Chamado 3")
    add_chamado("Chamado 4")
    mostrar_fila()
    att_chamado()  

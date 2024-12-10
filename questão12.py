import os
def listar_arquivos(diretorio):
    for item in os.listdir(diretorio):
        caminho_item = os.path.join(diretorio, item)  
        if os.path.isdir(caminho_item):
            listar_arquivos(caminho_item)  
        else:
            print(caminho_item)

def executar():
    diretorio_inicial = os.getcwd()
    listar_arquivos(diretorio_inicial)

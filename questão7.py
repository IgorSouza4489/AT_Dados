def checar_duplos(lista):
    listaTemp = set()  
    for elemento in lista:
        if elemento in listaTemp:
            return True  
        listaTemp.add(elemento) 
    return False 

def executar():
    lista_duplos = [1, 2, 3, 4, 5, 6, 7, 1]  
    lista_sem_duplos = [1, 2, 3, 4, 5, 6, 7]   
    print(checar_duplos(lista_duplos))  
    print(checar_duplos(lista_sem_duplos))  

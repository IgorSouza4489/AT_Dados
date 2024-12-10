import questão4
import questão6
import questão7
import questão8
import questão9
import questão10
import questão11
import questão12
import questão13
import questão14
import questão15
#Um aplicativo de mensagens precisa buscar um contato pelo nome em uma lista de contatos não ordenada. 
# Implemente o algoritmo de busca linear para encontrar um nome específico e exibir o número de telefone correspondente.
print("Questão 3")
contatos = [
    {"nome": "Igor", "telefone": "9732-7666"},
    {"nome": "Santos", "telefone": "1111-7666"},
    {"nome": "Souza", "telefone": "2222-7666"},
    {"nome": "Janja", "telefone": "3334-7666"},
    {"nome": "Moro", "telefone": "3333-4444"}
]

def buscar_contato(nome):
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            return contato["telefone"]
    return None

nome_busca = "Igor"
telefone = buscar_contato(nome_busca)
if telefone:
    print(f"O número de telefone de {nome_busca} é {telefone}")
else:
    print(f"contato não encontrado")




print("Questão 4")
questão4.executar()

print("Questão 6")
questão6.executar()

print("Questão 7")
questão7.executar()

print("Questão 8")
questão8.executar()

print("Questão 9")
questão9.executar()

print("Questão 10")
questão10.executar()

print("Questão 11")
questão11.executar()

print("Questão 12")
questão12.executar()

print("Questão 13")
questão13.executar()

print("Questão 14")
questão14.executar()

print("Questão 15")
questão15.executar()



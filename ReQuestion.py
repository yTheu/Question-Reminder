import datetime
import os

#Verificar se há questões para hoje
def VerificarQuestoes():
    print("Esse recurso ainda não funciona, mas você pode usar um bloco de notas ;)")

# Função para adicionar uma questão
def AdicionarQuestao():
    data_atual = datetime.datetime.now().date()

    disciplina = str(input("\n[ReQuestion] Qual a disciplina da questão?\n[Você] "))
    motivo_erro = str(input("\n[ReQuestion] O que te fez errar?\n[Você] "))
    url = input("\n[ReQuestion] Digite a URL da questão\n[Você] ")

    with open("questoes.txt", "a") as registro:
        registro.write(f"Questão\n\tDisciplina: {disciplina}\n\tMotivo do Erro: {motivo_erro}\n\tAcesso: {url}\n\tData de Inserção: {data_atual.strftime('%d-%m-%Y')}\n\n")
    print("[ReQuestion] Questão adicionada com sucesso!")

#Função para mostrar todas as questões
def MostrarQuestoes():
    if not os.path.exists("questoes.txt"):
        print("Não há questões adicionadas.")
        return

    with open("questoes.txt", "r") as registro:
        print(registro.read())


# Função Principal
print("\n[ReQuestion] \t----- Olá, seja bem vindo! -----\n")

print("[ReQuestion] Eae, Matheus! O que vamos fazer hoje?")
request = int(input("\t1 - Ver questões para hoje\n\t2 - Adicionar questão\n\t3 - Ver todas as questões\n\n[Você] "))

if request == 1:
    VerificarQuestoes()

elif request == 2:
    AdicionarQuestao()

elif request == 3:
    print("\n[ReQuestion] Mostrando todas as questões...\n")
    MostrarQuestoes()

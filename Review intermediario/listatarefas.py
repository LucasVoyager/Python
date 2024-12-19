import json

lista_fazer = []
lista_desfeitas = []

lista_tarefa = 'lista_tarefas.json'

def carregar_tarefas():
    global lista_fazer, lista_desfeitas
    try:
        with open(lista_tarefa, 'r') as arquivo:
            dados = json.load(arquivo)
            lista_fazer = dados.get("lista_fazer", [])
            lista_desfeitas = dados.get("lista_desfeitas", [])
    except (FileNotFoundError, json.JSONDecodeError):
        lista_fazer, lista_desfeitas = [], []

def salvar_tarefas():
    with open(lista_tarefa, 'w') as arquivo:
        json.dump({"lista_fazer": lista_fazer, "lista_desfeitas": lista_desfeitas}, arquivo, indent=4)

def main():
    carregar_tarefas()
    while True:
        print("Lista Atual", lista_fazer)
        print("Digite valor para entrada: Fazer (F), Desfazer (D), Refazer (R) e Sair (S) ")
        receber_entrada = input('Digite a entrada: ').upper()

        if (receber_entrada == 'F'):
            entrada_fazer = input('Digite entrada o que fazer: ')
            lista_fazer.append({
                "comando":receber_entrada, 
                "fazer": entrada_fazer
            })
            lista_desfeitas.clear()
            salvar_tarefas()
            print(f'Tarefa "{entrada_fazer}" adicionada!!')
        elif (receber_entrada == 'D'):
            if (lista_fazer):
                tarefa_desfeita = lista_fazer.pop()
                lista_desfeitas.append(tarefa_desfeita)
                salvar_tarefas()
                print(f'Tarefa desfeita "{tarefa_desfeita}" desfeita!!!')
            else:
                print('nenhuma tarefa foi encontrada')
        elif (receber_entrada == 'R'):
            if lista_desfeitas:
                tarefas_refeitas = lista_desfeitas.pop()
                lista_fazer.append(tarefas_refeitas)
                salvar_tarefas()
                print(f'tarefa refeita "{tarefas_refeitas}" refeita!!!')
            else:
                print('nao foi encontrado tarefa desfeitas')
        elif (receber_entrada == 'S'):
            print('Fechando programa!!!')
            break
        else:
            print('comando invalido!!!')

if __name__ == '__main__':
    main()
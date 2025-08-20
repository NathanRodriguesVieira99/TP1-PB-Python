from tasks import tasks


def addTask():
    task = input('Adicione uma tarefa: ')
    tasks.append(task)

    print(f'Tarefa "{task}" foi adicionada a sua lista.')

from tasks import tasks


def listTasks():
    if not tasks:
        print('Não há tarefas.')
    else:
        print('Minhas Tarefas: ')
        for index, task in enumerate(tasks):
            print(f'Tarefa #{index}. {task}')
            print('-------------')

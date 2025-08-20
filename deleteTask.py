from listTasks import listTasks
from tasks import tasks


def deleteTask():
    if not tasks:
        print('Não há tarefas para deletar')
        return

    listTasks()
    try:
        taskToDelete = int(input('Digite o número da tarefa para deletar: '))
        if 0 <= taskToDelete < len(tasks):
            removed = tasks.pop(taskToDelete)
            print(f'Tarefa #{removed} foi removida.')
        else:
            print(f'Tarefa não foi encontrada.')
    except:
        print('Opcão inválida!')

from addTask import addTask
from deleteTask import deleteTask
from listTasks import listTasks


while True:
    print('\n')
    print('Minha lista de tarefas')
    print('----------------------')
    print('1 - Adicionar uma nova tarefa')
    print('2 - Remover uma tarefa')
    print('3 - Listar minhas tarefas')
    print('4 - Sair')

    choice = input('Escolha uma opção: ')

    if (choice == '1'):
        addTask()
    elif (choice == '2'):
        deleteTask()
    elif (choice == '3'):
        listTasks()
    elif (choice == '4'):
        break
    else:
        print('Escolha inválida!')

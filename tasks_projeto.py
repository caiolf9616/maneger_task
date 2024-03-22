import time
tasks = {}
# Função de comando que permite adicionar tarefas
def add_tasks():
    global tasks
    name_task = (input('Nome da Tarefa: '))
    description_task = (input('Descrição:'))
    category_task = (input('Categoria:'))
    priority_task = (input('Prioriade: '))
    print('Adicionada com Sucesso!')
    time.sleep(2)

    tasks_detailss = {
        'Tarefa': name_task,
        'Descrição': description_task,
        'Categoria': category_task,
        'Prioridade': priority_task
    }
    tasks[name_task] = tasks_detailss
    return tasks
    
# Função de comando que permite lista as tarefas
def list_tasks():
    if not tasks:
        print('A agenda esta vazia!')
        time.sleep(2)
    else:
     for name_task, tasks_detailss in tasks.items():
        print(f'{name_task}')
        for k, v in tasks_detailss.items():
            print(f'{k}:{v}')
            time.sleep(2)     
                 
   
   
        
# Função de Comando que permite marca como tarefa feita
def tasks_done():
    done = input('Informa o nome da tarefa Concluida: ')
    if done in tasks:
        print('Tarefa Concluida!')
        time.sleep(2)
        task_detaills = tasks[done]
        print('Detalhes da tafera Cocluída:')
        time.sleep(2)
        for k, v in task_detaills.items():
            print(f'{k}: {v}')
    else:
        print('Tarefa não emcontrada!') 
        time.sleep(2) 
     
    
# Função de comando que permite mostra tarefas por prioridade
def priority_tasks():
    tasks_priority = {
        'Baixa'.lower():[],
        'Media'.lower():[],
        'Alta'.lower():[]
    }
    for task_name,task_details in tasks.items():
        priority = task_details['Prioridade'].lower()
        tasks_priority[priority].append(task_name)
        
    see_priority = input('Informe a prioridade das tarefas que deseja ver: ').lower()
    print()
    if see_priority in tasks_priority:
        print('Tarefas com Propiedade', see_priority.capitalize() + ':')
        print()
        for task_name in tasks_priority[see_priority]:
            print('Nome da tarefa:', tasks[task_name]['Tarefa'])
            print('Descrição:', tasks[task_name]['Descrição'])
            print('Categoria:', tasks[task_name]['Categoria'])
            print('Prioridade:',tasks[task_name]['Prioridade'])   
            print() 
            print('//'*20)
    else:
        print('Vazia ou não encontrada, tente novamente!')
        time.sleep(2) 
# Função que permite excuir uma tarefa 
def delete_task():
    dell_task = input('Informe a tarefa que deseja excluir: ').lower()
    if dell_task in tasks:
        del tasks[dell_task]
        print('Tarefa Excluida com sucesso!')
        time.sleep(2)
    else:
        print('Tarefa não emcontrada.')
        time.sleep(2)    
    
            
   
# Menu de interação com o usuario

 
print('Bem Vindo a Sua Agenda de Tarefas!') 
print()

while True:
    print ('Quais das opções abaixo você deseja')
    try:
        choice = int(input('''1-> Adicionar Tarefas
2-> listar tarefa
3-> Adicionar tarefas já feitas
4-> Vizualizar por Prioridade
5-> Excluir tarefa
6-> Sair
: '''))
    except ValueError:
        print('Opção invalida')
        time.sleep(2)
        continue
    
   
         
    
            
    if choice == 1:
        add_tasks()
    elif choice == 2:
         list_tasks()
    elif choice == 3:
        tasks_done()
    elif choice == 4:
        priority_tasks()
    elif choice == 5:
        delete_task()
    elif choice == 6:
        break 
    else:
        time.sleep(2)
        print('Opção invalida, tente novamente!')
                      

  
   
                
                
    
        
    



    
    



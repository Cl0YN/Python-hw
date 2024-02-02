import json
from dataclasses import dataclass
import datetime
from dataclasses import asdict


@dataclass
class Task:
    name: str
    date: int
    status: str
    
    
tasks = []
taskstatus = ["new", "performed", "review", "done", "canceled"]


def createtask():
    name=input("Введите названия задачи:")
    date=datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    status=input("Введите статус задачи:")
    while True:
        if status not in taskstatus:
           print("Такого статуса нет")
           status=input("Введите статус задачи:")
        else:
            break
             
    task=Task(name, date, status)
    tasks.append(task)
    
    
def save_task_to_json():
    taski = []
    for i in tasks:
        taski.append(asdict(i))
    with open("hw1.json", "w") as file:
        json.dump(taski,file,indent=4 )     
        
            
def show_tasks():
    if not tasks:
        print("Список задач пуст")
        return
    
    print("{:<10} {:<20} {:<10} {:<10}".format("No", "Название", "Дата", "Статус")) 
    print("-"*50)
    
    for idx, task in enumerate(tasks):
        print("{:<10} {:<20} {:<10} {:<10}".format(idx+1, task.name, task.date, task.status))
        
        
def change_status():
    if not tasks:
        print("Список задач пуст")
        return

    print("Текущие задачи:")
    show_tasks()
    
    task_num = int(input("Введите номер задачи для изменения статуса: "))
    task = tasks[task_num-1]
    
    print("Текущий статус задачи:", task.status)
    print("Выберите новый статус:", taskstatus)
    
    new_status = input("Введите новый статус: ")
    while new_status not in taskstatus:
        print("Такого статуса нет!")
        new_status = input("Введите новый статус: ")
        
    task.status = new_status
    
    print("Статус задачи успешно изменен на", task.status)
        
        
def show_history():
    if not tasks:
        print("Список задач пуст")
        return
    
    last_task = tasks[-1]
    
    print("{:<10} {:<20} {:<10} {:<10}".format("No", "Название", "Дата", "Статус"))
    print("-"*50)  
    print("{:<10} {:<20} {:<10} {:<10}".format(len(tasks), last_task.name, last_task.date, last_task.status))       
 
 
# managertasks
while True:
    print("Вас приветствует менеджер задач:")
    print("1-Создать новую задачу")
    print("2-Сохранить задачу")
    print("3-Посмотреть все задачи")
    print("4-Изменить статус задачи")
    print("5-Посмотреть историю задач")
    print("0-Выход")
    
    
    choice = int(input("Выберите пункт меню: "))
    
    
    if choice == 1:
        createtask()
    elif choice == 2:
        save_task_to_json()
    elif choice == 3:
        show_tasks()
    elif choice == 4:
        change_status()
    elif choice==5:
        show_history()
    elif choice == 0:
        print("Работа завершена")
        break
    else:
        print("Неверно выбран пункт меню")
        choice = int(input("Выберите пункт меню: "))
        


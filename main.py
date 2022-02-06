import random

HELP = '''
Список доступных команд:
* print  - Напечать все задачи на заданную дату
* add - Добавить задачу
* help - Напечатать справку по программе
* show - Показать все добавленные задачи
* random - Добавлять случайную задачу на дату Сегодня'''

RANDOM_TASKS = ["Пройти курс по JS", "Написать письмо", "Покормить кота", "Помыть машину", "Помыть посуду", "Поставить будильник"]

tasks = {

}

# Сегодня, завтра, 13.12 ...
# [Задача1, задача2, задача3]
# Дата -> [Задача1, задача2, задача3]

run = True

def add_todo(date, task):
  if date in tasks:
    #Дата есть в словаре
    #Добавляем в список задачу
    tasks[date].append(task)
  else:
    #Даты в словаре нет
    #Создаем запись с ключом date
    tasks[date] = []
    tasks[date].append(task)
  print('Задача ', task, ' добавлена на дату', date)  

while run:
  command = input('Введите команду: ')
  if command == 'help':
      print(HELP)
  elif command == 'show':
    date = input('Введите дату для отображения списка задачи: ')
    if date in tasks:
      for task in tasks[date]:
        print('- ', task)
    else:
      print('Такой даты нет')  
  elif command == 'add':
    date = input('Введите дату для добавления задачи: ')
    task = input('Введите название задачи: ')
    add_todo(date, task)
  elif command == "random":
    task = random.choice(RANDOM_TASKS)
    add_todo("Сегодня", task)
  else:
    print('Неизвестная команда!')
    break

print('До свидания!')
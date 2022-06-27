
from datetime import date
import datetime

class ToDo:
    def __init__(self, filename='todo.txt'):
        self.filename = filename
        self.todo_list = {}
    
    def add_task(self, task_des: str, date: date=date.today()):
        # add the task to the list
        if self.todo_list.get(date):
            self.todo_list[date] += [task_des]
        else:
            self.todo_list[date] = [task_des]
    
    def show_list(self):
        dates = self.todo_list.keys()
        if not dates:
            print('No Tasks')
            return
        for date in dates:
            print('Date:', date)
            for index, task in enumerate(self.todo_list[date], start=1):
                print(f"{index}: {task}")
        print('End')
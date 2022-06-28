
from datetime import date
import datetime

class ToDo:
    def __init__(self):
        self.todo_list = {}
        self.id = 1
    
    def give_id(self):
        id, self.id = self.id, self.id+1
        return id
    
    def add_task(self, task: str, date: date=date.today()):
        # add the task to the list
        if self.todo_list.get(date):
            self.todo_list[date][self.give_id()] = {
                        'task': task,
                        'is_done': False
                    }
        else:
            self.todo_list[date] = {
                    self.give_id() : {
                        'task': task,
                        'is_done': False
                    }
                }
    
    def complete_task(self, date, id):
        if self.todo_list.get(date):
            day_tasks_list = self.todo_list[date]
            if day_tasks_list.get(id):
                day_tasks_list[id]['is_done'] = True
            else:
                return 'Invalid Id'
        else:
            return 'Invalid date'
        return 'Good Job'
    
    def remove_day_task(self, date):
        if self.todo_list.get(date):
            self.todo_list.pop(date)
        else:
            return 'Not Found'
        return 'Deleted day!'

    def remove_task(self, date, id):
        if self.todo_list.get(date):
            day_tasks_list = self.todo_list[date]
            if day_tasks_list.get(id):
                day_tasks_list.pop(id)
            else:
                return 'Invalid Id'
        else:
            return 'Invalid date'
        return 'Deleted task!'

    def show_list(self):
        dates = self.todo_list.keys()
        if not dates:
            print('No Tasks')
            return
        for date in dates:
            print('Date:', date)
            for key, value in self.todo_list[date].items():
                state = 'Complete' if value['is_done'] else 'Not complete'
                print(f"    Id: {key} - {value['task']} - {state}")
        print('End')
import json
import tkinter as tk
from pathlib import Path


tasks = []
FILE = Path("task.json")

def open_file():
    with open(FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def seve_file():
    with open(FILE, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
        return

def update_tasks(task_name, status):
    if(len(task_name) == 0):
        return
    
    if task_name and status != None:
        task_existe = False
        for task in tasks:
            if task["task_name"] == task_name:
                task["complete"] = status
                task_existe = True
        
        if not task_existe:
            new_task = {
                "task_id": len(tasks),
                "task_name": task_name,
                "complete": status
            }
            tasks.append(new_task)  
        
        seve_file()
        
        return
    
def add_new_task(parent_window):
    window2 = tk.Toplevel()
    window2.geometry("250x150")
    window2.config( padx=40, pady=20)
    window2.title("nova terefa")   
    
    tk.Label(window2, text="Nova tarefa", font=60).grid(row=0, columnspan=2,pady=5)
    
    tk.Label(window2, text="Nome", font=40).grid(row=1, column=0, pady=5)
    name = tk.Entry(window2) 
    name.grid(row=1, column=1, pady=5)
                    
    def on_click():
        update_tasks(name.get(), False)
        window2.destroy()
        render_tasks(parent_window)
    
    tk.Button(window2, text="adicionar tarefa", command=on_click).grid(row=(len(tasks) + 2), columnspan=3)


def render_tasks(window):
    
    for widget in window.grid_slaves():
        if int(widget.grid_info()["row"] > 0 ) :
            widget.destroy()
    
    for task in tasks: 
        var = tk.BooleanVar(value=task["complete"])       
        tk.Checkbutton( window, 
                        text=task["task_name"],
                        font=40, 
                        command=lambda name=task["task_name"], status=var: update_tasks(name, status.get()),
                        variable=var,
                        ).grid(row=task["task_id"] + 1,pady=5, sticky="W") 
        
    def on_click():
        add_new_task(window)
        
    tk.Button(  window, 
                text="adicionar tarefa", 
                command=on_click
            ).grid(row=len(tasks) + 2, columnspan=2)


def interface_init():
    window = tk.Tk()
    window.geometry("250x600")
    window.config( padx=40, pady=20)
    window.title("tarefas")
    
    tk.Label(window, text="Lista de tarefas", font=60).grid(row=0)
    
    render_tasks(window)
  
    tk.mainloop()    
        
def task_read():
    res = open_file()
    
    if(len(res) > 0):
        for task in res:
            tasks.append(task) 

if __name__ == "__main__":
    task_read()
    interface_init()

from tkinter import *

root = Tk(className='Task manager')

#tasks list
# tasks_list = ['walking','cycling','running','reading','watching tv','watching phone','gyming','revision','tracking',
#             'talking']
# task_var = StringVar()
# task_var.set('No of tasks')
# source_menu = OptionMenu(root,task_var,*tasks_list).grid()
# task_var.set('walking')

l1 = Label(root,text='Enter your task: ',font=('Times New Roman',15))
l1.grid(row=0,column=0,sticky= W,pady=2)
e1 = Entry(root,font=('Times New Roman',15))
e1.grid(row=0,column=1,sticky= W,pady=2)

def add_task():

    task_name = e1.get()
    listbox.insert(END,task_name) #this would enter new task at the end 
    e1.delete(0,END) #to delete the last typed task
    
    print(f'task {task_name} is added sucessfully to your list!')

add_btn = Button(root,text='Add',command=add_task)
add_btn.grid(row=1,column=1, sticky= W, pady=2)

listbox = Listbox(root)
listbox.grid()
entry = Entry(root)

listbox.grid()

def del_task():

    # this is to select specified task
    index = listbox.curselection()

    # If there is a selected task, delete it from the listbox
    if index:
        listbox.delete(index)
        # Print a confirmation message
        print(f"Task deleted successfully")
    else:
        # Print an error message
        print(f"No task selected")

dele = Button(root,text='Delete',command=del_task)
dele.grid()

root.mainloop()


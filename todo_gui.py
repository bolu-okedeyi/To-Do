import tkinter as tk
import todo 

window = tk.Tk()
window.title('NIIT TODO APP')





# controller function
def display_todo():
    the_list_box.delete(0,tk.END)
    all_todo=todo.gui_view_all_todo()
    for the_todo in all_todo:
        the_list_box.insert(tk.END,the_todo)

def search_a_todo():
    the_list_box.delete(0,tk.END)
    searched_value=title.get()
    result=todo.search_todo(searched_value)
    if result==[]:
        the_list_box.insert(tk.END,'No Result Found')
    else:
         the_list_box.insert(tk.END,result)
        
def update_a_todo():
    selected=the_list_box.curselection()
    new_title=title.get()
    print(selected)



def add_to_todo():
    title_content=title.get()
    description=desc_entry.get(0.0,tk.END)
    todo.add_todo(title_content,description)
    display_todo()
    

#get screen width and heigth

my_system_height = window.winfo_screenheight()
my_system_width = window.winfo_screenwidth()

#window.minsize(my_system_width,my_system_height)

#add a welcome message
welcome_info = tk.Label(window, bg='darkgreen', fg='white', text="Welcome to Niit Todo Software", height=2)
welcome_info.pack(fill=tk.X)

#add two frames as containers
left_frame = tk.Frame(window)
right_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT, anchor=tk.NW)
right_frame.pack(side=tk.LEFT, anchor=tk.NW)

#create a paned window widgets & add to the left-frame
paned_1 = tk.PanedWindow(left_frame)
#add a label to the paned window
title_label = tk.Label(paned_1, text='Todo Title')
#pack the label to the left
title_label.pack(side=tk.LEFT)
#add an entry to the paned window
title=tk.StringVar()
title_entry = tk.Entry(paned_1, bg='lightblue',textvariable=title)
#pack the entry to the left
title_entry.pack(side=tk.LEFT, padx=35)
paned_1.pack( anchor=tk.NW, fill=tk.X)

#create a paned window widgets & add to the left-frame
paned_2 = tk.PanedWindow(left_frame)
#add a label to the paned window

desc_label = tk.Label(paned_2, text='Todo Description')
#pack the label to the left
desc_label.pack(side=tk.LEFT)
#add an entry to the paned window
desc_entry = tk.Text(paned_2, font=(16), height=10, width=50, bg='lightblue')
#pack the entry to the left

desc_entry.pack(side=tk.LEFT)
paned_2.pack(anchor=tk.NW, fill=tk.X)

#adding a list box
the_listbox_label = tk.Label(left_frame, text='All Todo')
the_listbox_label.pack(side=tk.LEFT)
the_list_box = tk.Listbox(left_frame, bg='lightblue',height=10, width=50)
the_list_box.pack(anchor=tk.NW,padx=43)


#add widgets to the right frame
view_all = tk.Button(right_frame, text='View all',command = display_todo).pack(pady=30)
update_todo = tk.Button(right_frame, text='Update Todo').pack(padx=100)
add_todo = tk.Button(right_frame, text='Add Todo',command= add_to_todo).pack(pady=30)
search_todo = tk.Button(right_frame, text='Search Todo',command=search_a_todo).pack()
delete_todo = tk.Button(right_frame, text='Delete Todo').pack(pady=30)

window.mainloop()


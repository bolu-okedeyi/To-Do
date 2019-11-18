import todo

print("welcom to the cli")
print("""
    select an option below
    1)view all todo
    2)search for todo 
    3)update a todo
    4)delete a todo
    5)exit
      """)
answer=int (input('choose a number:'))
if answer > 5 or answer < 1:
      print('invalid input')
elif answer==1:
      todo.view_all_todo()
elif answer==2:
      the_title=input('enter the title of the todo:')
      todo.search_todo(the_title)
elif answer==3:
      new_id=int(input('enter the new title:'))
      new_title=int('enter the new title')
      new_desc=int('enter the new description') 
      todo.update_todo(new_id,new_title,new_desc)
elif answer==4:
      Delete=input('enter the id:')
      todo.delete_todo(Delete)



input ('press enter to exit')
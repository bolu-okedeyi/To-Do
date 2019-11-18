import sqlite3
from datetime import datetime

connection=sqlite3.connect('todo.db')
cursor= connection.cursor()
user=cursor.execute


today = datetime.now()
date ="{}-{}-{}".format(today.day,today.month,today.year)


def createTable():
    sql="""
            create table todos(
            id integer primary key autoincrement unique,
            title text,
            description text,
            date text
            ) """
    cursor.execute(sql)
#view all for cli
def view_all_todo():
    sql='select * from todos'
    cursor.execute(sql)
    row_set= cursor.fetchall()
    for row in row_set:
        return row_set
#view all for gui
def gui_view_all_todo():
    sql='select * from todos'
    cursor.execute(sql)
    row_set= cursor.fetchall()
    return row_set


def add_todo( title,description):
    sql='''
        insert into todos
        (title, description, date)
        VALUES(?,?,?)
        '''
    cursor.execute(sql,(title,description,date))
    #this is used to write changes
    connection.commit()
    return('added successfully')


    
def search_todo(title="none"):
    the_title=title
    sql="select * from todos where title ='{}'".format(the_title)
    cursor.execute(sql)
    result=cursor.fetchall()
    if result==[]:
        return []
    else:
        return result


    
def update_todo(Id,title,desc):
    sel="update todo set title='{}', description='{}' where Id={}".format(title,decs,Id)
    cursor.execute(sql)
    connection.commit()
    print('updated sucessfilly')

def delete_todo(Id):
    sql='delete from todo where Id={}'.format(Id)
    cursor.execute(sql)
    connection.commit()
    print(f'todo with id {Id} deleted sucessfully')




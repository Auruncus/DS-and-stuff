from tkinter import *
from tkinter import messagebox
import db
import os

#создание базы данных
def create_database():
    db.initiate_database()
    print("Database created")

#удаление базы данных
def delete_database():
    db.del_database()
    print("Database deleted")

#функция вывода Самолетов
def show_planes():
    departure_list.delete(0, END)
    for row in db.show_airport_planes():
        departure_list.insert(END, row)
    print("Show") 

#функция вывода Рейсов
def show_flights():
    departure_list.delete(0, END)
    for row in db.show_airport_flights():
        departure_list.insert(END, row)
    print("Show") 

#функция вывода Вылетов
def show_departures():
    departure_list.delete(0, END)
    for row in db.show_airport_departures():
        departure_list.insert(END, row)
    print("Show")     

#функции поиска по значению
def check_index(element):
   try:
       index = []
       list_box = departure_list.get(0, END)
       element=int(element)
       for i, a in enumerate(list_box):
           if element in a:
               print('found {} in tuple {} at index {}'.format(element, i, a.index(element)))
               index.append(i)
       print(index)
       return index
   except ValueError:
       index = -1 
       return index

def search_value():
    print("in searching")
    find = search_text.get()
    index = check_index(find)
    if (index == -1):
        return 
    else:
        #print(index)
        founded =[]
        for i in index:
            founded.append(departure_list.get(i))
        departure_list.delete(0, END) 
        #print(founded) 
        for tup in founded:
            departure_list.insert(END, tup)
        print("FOUND")


#функции для удаления
def delete_planes():
    db.clear_airport_planes()        
    print("Planes deleted")

def delete_flights():
    db.clear_airport_flights()        
    print("Flights deleted")

def delete_departures():
    db.clear_airport_departures()        
    print("Departures deleted")    

def delete_all_data():
    db.clear_airport()        
    print("All deleted")    

def add_plane():
    print("plane added")


def select_item(event):
    print("select")



def clear_text():
    print("clear")
 


app = Tk()


# departure_listbox
departure_list = Listbox(app, height=8, width=50, border=0)
departure_list.grid(row=4, column=1, columnspan=3, rowspan=6, pady=20, padx=20)
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
departure_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=departure_list.yview)
departure_list.bind('<<ListboxSelect>>', select_item)

##################CREATE

create_btn = Button(app, text='Создать БД', width=15, command=create_database)
create_btn.grid(row=1, column=0, pady=10)

delete_btn = Button(app, text='Удалить БД', width=15, command=delete_database)
delete_btn.grid(row=1, column=1, pady=10)

##################SHOW

show_planes_btn = Button(app, text='Вывести Самолеты', width=15, command=show_planes)
show_planes_btn.grid(row=2, column=0, pady=10)

show_flights_btn = Button(app, text='Вывести Рейсы', width=15, command=show_flights)
show_flights_btn.grid(row=2, column=1, pady=10)

show_departures_btn = Button(app, text='Вывести Вылеты', width=15, command=show_departures)
show_departures_btn.grid(row=2, column=2, pady=10)

##################SEARCH

search_text = StringVar()
search_label = Label(app, text='Поиск по значению', font=('bold', 10), pady=20)
search_label.grid(row=0, column=5, sticky=W)
search_entry = Entry(app, textvariable=search_text)
search_entry.grid(row=1, column=6)

search_btn = Button(app, text='Найти', width=15, command=search_value)
search_btn.grid(row=1, column=5, pady=10)

##################ADD PLANE

plane_ID_text = StringVar()
plane_ID_label = Label(app, text='Plane_ID', font=('bold', 10), pady=20)
plane_ID_label.grid(row=4, column=6, sticky=W)
plane_ID_entry = Entry(app, textvariable=plane_ID_text)
plane_ID_entry.grid(row=4, column=7)

plane_TYPE_text = StringVar()
plane_TYPE_label = Label(app, text='Plane_TYPE', font=('bold', 10), pady=20)
plane_TYPE_label.grid(row=5, column=6, sticky=W)
plane_TYPE_entry = Entry(app, textvariable=plane_TYPE_text)
plane_TYPE_entry.grid(row=5, column=7)

plane_SEATS_text = StringVar()
plane_SEATS_label = Label(app, text='Plane_Seats', font=('bold', 10), pady=20)
plane_SEATS_label.grid(row=6, column=6, sticky=W)
plane_SEATS_entry = Entry(app, textvariable=plane_SEATS_text)
plane_SEATS_entry.grid(row=6, column=7)

plane_DIST_text = StringVar()
plane_DIST_label = Label(app, text='Plane_Distance', font=('bold', 10), pady=20)
plane_DIST_label.grid(row=7, column=6, sticky=W)
plane_DIST_entry = Entry(app, textvariable=plane_DIST_text)
plane_DIST_entry.grid(row=7, column=7)


plane_add_btn = Button(app, text='Добавить самолет', width=15, command=add_plane)
plane_add_btn.grid(row=8, column=7, pady=10)

##################DELETE

delete_planes_btn = Button(app, text='Удалить Самолеты', width=15, command=delete_planes)
delete_planes_btn.grid(row=4, column=5, pady=10)

delete_flights_btn = Button(app, text='Удалить Рейсы', width=15, command=delete_flights)
delete_flights_btn.grid(row=5, column=5, pady=10)

delete_departures_btn = Button(app, text='Удалить Вылеты', width=15, command=delete_departures)
delete_departures_btn.grid(row=6, column=5, pady=10)

delete_all_btn = Button(app, text='Удалить Все', width=15, command=delete_all_data)
delete_all_btn.grid(row=7, column=5, pady=10)
"""
_btn = Button(app, text='', width=15, command=)
_btn.grid(row=2, column=2, pady=10)

_btn = Button(app, text='', width=15, command=)
_btn.grid(row=2, column=2, pady=10)

_btn = Button(app, text='', width=15, command=)
_btn.grid(row=2, column=2, pady=10)

_btn = Button(app, text='', width=15, command=)
_btn.grid(row=2, column=2, pady=10)
"""


app.title('Aiprport Control App')
app.geometry('1200x600')
#show_planes()




app.mainloop()
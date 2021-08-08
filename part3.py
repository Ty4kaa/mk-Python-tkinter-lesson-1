import tkinter as tk
from tkinter.constants import RIGHT #модуль

y = 400   #высота
x = 600   #ширина
count = 0


def plus(): #просто посчитали и вывели в консоль
    c = y+x
    print(c)


def add_label(): #функция которая добовляет новый лэйбл (смотрите файл part2)
    label = tk.Label(gui, text='new label',
                    bg='black')
    label.pack()


def counter():
    global count #глобализируем переменную
    count+=1
    btn2['text'] = f'Счётчик: {count}'

gui = tk.Tk()
gui.title('Title text, тут мы можем писать что угодно') 
gui.geometry(f'{y}x{x}')
gui.config(bg = '#4D4D4D')

photo = tk.PhotoImage(file = 'icon.png')       
gui.iconphoto(False, photo)

btn = tk.Button(gui, text= 'Hello World!', #класс для создания кнопки
                command=plus,              #обращаемся к ней без вызова, без скобочек
                ) 

btn1 = tk.Button(gui, text='Add Label', #добавляем лэйбл с помощью кнопки
                command=add_label,
                )

btn2 = tk.Button(gui, text=f'Счётчик: {count}', #считаем сколько раз была нажата эта кнопка 
                command=counter,
                activebackground='red',
                bg='blue') 


btn.pack() #.pack() добавление элемента в наше приложение
btn1.pack()
btn2.pack()


gui.mainloop() #функция для запуска кода - mainloop()
import tkinter as tk
from tkinter.constants import RIGHT #модуль

y = 400   #высота
x = 600   #ширина

gui = tk.Tk()
gui.title('Title text, тут мы можем писать что угодно') 
gui.geometry(f'{y}x{x}')
gui.config(bg = '#4D4D4D')

photo = tk.PhotoImage(file = 'icon.png')       
gui.iconphoto(False, photo)

                                    #ТЕКСТ И ЕГО СТИЛИ
             #Label обязательно с большой буквы
label_1 = tk.Label(gui, text='''Hello World!\nНаша новая строка''', #label (визитка), в нашем случае просто класс label в который мы передаём текст (свойство text) 
                   bg = '#c4c4c4',           #задний фон (свойство bg)
                   fg = 'black',             #цвет текста (свойство fg)
                   font = ('Arial', 10, 'bold'),          #шрифт (свойство font в который передаём кортедж)
                   #название шрифта, размер, стиль шрифта

                   #отступы внитри label
                   padx = 10, #отступы по бокам
                   pady = 10, #отступы снизу и сверху

                   width= 50, #значение не в пикселях а в знаках (ширина)
                   height= 50, #(высота)

                   anchor = 'n', #прикрепление к одной из сторон 
                                #n - верх
                                #s - низ
                                #e - право
                                #w - лево
                                #так же есть ne, se, sw, nw, center

                    relief=tk.RAISED,
                                #с помощью этого свойства мы можем увидеть границы 
                    bd=10, #размер границы

                    justify= tk.LEFT #выравнивание текста, по дефолту center (работает только с многострочной строкой например: """Ваш текст""")
                                     #обязательно большими буквами
                   )        
label_1.pack() #.pack добавление элемента в наше приложение




gui.mainloop() #функция для запуска кода - mainloop()
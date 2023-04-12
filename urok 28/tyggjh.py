import tkinter as tk
root = tk.Tk()
root.title('пикабу бушидо халуин')
root.geometry('300x300')

# photokartochka = tk.PhotoImage(file='images/negr.png')
#
#
# lab1 = tk.Label(root, text='у мужлаан нет нет прав',
#                 image=photokartochka)
# lab1.pack()
#
# def hell_o(e):
#     print(e)
#     print('хеллоу пикабу бушида')
#
#
# btn = tk.Button(root)
# # btn['command'] = hell_o
# btn.bind('<Double-Button-1>', hell_o)
# btn['text'] = 'пока'
# btn['font'] = ('times new roman', 20, 'bold')
# btn['height'] = 64
# btn['width'] = 10
# btn['background'] = 'pink'
# btn['foreground'] = 'blue'
# btn.pack(anchor='e')

def s_m():
    a = ent.get()
    b = ent2.get(1.0, "end")
    ent.delete(0, 'end')
    ent2.delete(0.0, 'end')
    print(a, b)


label = tk.Label(text='адрес')
label2 = tk.Label(text='комментарий')
label.pack()
ent = tk.Entry(root)
conf = tk.Button(text='отправить',
                 command=s_m)
ent2 = tk.Text(root, width=20, height=10)
ent.pack()
label2.pack()
ent2.pack()
conf.pack()
root.mainloop()
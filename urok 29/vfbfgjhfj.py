from tkinter import *

root = Tk()
root.geometry('300x200')

# def isChecked(f):
#     print(cb_val.get())
#     cb.deselect()
#
#
# cb_val = BooleanVar()
# lab = Label(root, text=f'жесть: {cb_val.get()}')
# lab.pack()
# cb = Checkbutton(root,
#                  text='писка',
#                  variable=cb_val,
#                  onvalue=True,
#                  offvalue=False,)
#
# cb.bind('<Button-3>', isChecked)
# cb.pack()

# def getrb():
#     print(rb_val.get())
#
#
# rb_val = IntVar()
# print(rb_val.get())
# Radiobutton(root, variable=rb_val, text='1', value=505, command=getrb).pack()
# Radiobutton(root, variable=rb_val, text='2', value=525, command=getrb).pack()
# Radiobutton(root, variable=rb_val, text='3', value=545, command=getrb).pack()

# def pupu():
#     print(lst.curselection())
#
# ls = ['1', '2', '3']
# lst = Listbox(root, selectmode=EXTENDED)
# lst.pack()
# for i in ls:
#     lst.insert('end', i)
#
# Button(root, text='бам бам бам', command=pupu).pack()

# def getscale(g):
#     print(scal.get())
#     print(g)
#
# scal = Scale(root, from_=1, to=16, orient=HORIZONTAL, length=200,
#              tickinterval=15,
#              width=100,
#              command=getscale)
# scal.pack()

# def act():
#     if btn1['state'] == 'disabled':
#         btn1['state'] = 'normal'
#     else:
#         btn1['state'] = 'disabled'
#
#
# btn1 = Button(root, text='я писка')
# btn1.pack()
# btn2 = Button(root, text='я не писка', command=act)
# btn2.pack()

# def gh():
#     print(cb_val.get())
#     if cb_val.get() == False:
#         btn['text'] = 'неактивно'
#         btn['state'] = 'disabled'
#     elif cb_val.get() == True:
#         btn['text'] = 'активно'
#         btn['state'] = 'normal'
#
# cb_val = BooleanVar()
# cb = Checkbutton(root, text='активировать', variable=cb_val, onvalue=True, offvalue=False, command=gh)
# btn = Button(root, text='активно')
#
# cb.pack()
# btn.pack()

# def phg():
#     if rb_val.get() == 1:
#         a['text'] = 'Hello world'
#     elif rb_val.get() == 0:
#         a['text'] = 'Hello python'
#
#
#
# a = Label(root, text='Hello ...')
# a.pack()
# rb_val = IntVar()
# Radiobutton(root, text='world', variable=rb_val, value=1, command=phg).pack()
# Radiobutton(root, text='python', variable=rb_val, value=0, command=phg).pack()


# def bold():
#     if valbold.get():
#         lab['font'] += ' bold'
#     else:
#         lab['font'] = lab['font'].replace(' bold', '')
#
#
# def curs():
#     if valcurs.get():
#         lab['font'] += ' italic'
#     else:
#         lab['font'] = lab['font'].replace(' italic', '')
#
#
# def no():
#     if valno.get():
#         lab['font'] += ' underline'
#     else:
#         lab['font'] = lab['font'].replace(' underline', '')
#
# def yes():
#     if valyes.get():
#         lab['font'] += ' overstrike'
#     else:
#         lab['font'] = lab['font'].replace(' overstrike', '')
#
#
# lab = Label(root, text='я писка, а ты?', font='Arial 15')
# lab.pack()
#
# valbold = BooleanVar()
# valcurs = BooleanVar()
# valno = BooleanVar()
# valyes = BooleanVar()
# cb_bold = Checkbutton(root, text='жирный', command=bold, variable=valbold, onvalue=True, offvalue=False)
# cb_bold.pack()
# cb_curs = Checkbutton(root, text='курсив', command=curs, variable=valcurs, onvalue=True, offvalue=False )
# cb_curs.pack()
# cb_no = Checkbutton(root, text='зачеркнутый', command=no, variable=valno, onvalue=True, offvalue=False)
# cb_no.pack()
# cb_yes = Checkbutton(root, text='подчеркнутый', command=yes, variable=valyes, onvalue=True, offvalue=False)
# cb_yes.pack()
#
# lab.pack()


def ghg():
    en.insert('end', ', пожалуйста 🙏🙏🙏🙏')


en = Entry(root, width=40, bd=1)
en.pack()
btn = Button(root, text='добавить унижения', command=ghg)
btn.pack()
root.mainloop()
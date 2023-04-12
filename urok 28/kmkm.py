import tkinter as tk



root = tk.Tk()
root.geometry('300x300')
for row in range(3):
    for column in range(3):
        btn = tk.Button(text=f'{row},{column}')
        btn.grid(row=row, column=column)
root.mainloop()
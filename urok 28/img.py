import tkinter as tk
import urllib
root = tk.Tk()
root.geometry('1700x1700')
img = tk.PhotoImage(file='images/negr.png').subsample(2,2)
label = tk.Label(image=img)
label.pack()

img2 = img.zoom(8, 1)
label2 = tk.Label(image=img2)
label2.pack()

img3 = img.subsample(2, 2)
label3 = tk.Label(image=img3)
label3.pack()
imgurl = 'https://upload.wikimedia.org/wikipedia/commons/d/d0/Vladimir_Zhirinovsky_portrait.png'
root.mainloop()
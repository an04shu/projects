from tkinter import *
import random 
window=Tk()
window.minsize(650,650)
window.maxsize(650,650)
window.title("ROLL THE DICE")
label=Label(window,font=('noraml',400))
def roll():
    numbers=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.config(text=f'{random.choice(numbers)}')
    label.pack()
heading=Label(window,text='Roll the dice',font=('bold',50),bg='light cyan')
heading.pack(fill=X)
button=Button(window,text='Roll',font=('normal',30),command=lambda:roll())
button.pack()
window.mainloop()
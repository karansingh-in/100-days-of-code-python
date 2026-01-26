from tkinter import *

window = Tk()
window.minsize(200,100)
window.title('Miles to km coverter')

miles_label = Label(text='Miles')

input = Entry()
input.focus()

ans = Label(text='0')

def cal():
    miles = int(input.get())
    km = float(miles * 1.609)
    ans.config(text=km)
    
is_equal_to = Label(text='is equal to')
km_label = Label(text='km')
button = Button(text='Calculate', command=cal)

is_equal_to.grid(row=1, column=0)
input.grid(row=0, column=1)
ans.grid(row=1,column=1)
button.grid(row=2, column=1)
miles_label.grid(row=0,column=2)
km_label.grid(row=1,column=2)













window.mainloop()
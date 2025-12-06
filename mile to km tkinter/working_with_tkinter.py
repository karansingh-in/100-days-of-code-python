from tkinter import *

# main window GUI
window = Tk()
window.title('hello world')
window.minsize(500,300)

# label
my_label = Label(text='hellu hellu', font=('Segoe UI', 20, 'bold'))
my_label.grid(column=0,row=0)

def update_label():
    my_label.config(text=' i got clicked')

# button
my_button = Button()
my_button.config(text='click me', command=update_label)

#input text box
input = Entry()
input.grid(column=3, row=2)

# given = input.get()
# print(given)
# the code above will not work because it startes listerning for input even before the window is created it never catches the input

def update_entry():
    given = input.get()
    print(given)
    my_label.config(text=given)
    
my_button.config(command=update_entry)
my_button.grid(column=1,row=1)

# input text box with multiple lines
input_more = Text(height=5, width=8)
input_more.grid(column=4, row=4)
# add some text by default in the text box
input_more.insert(END, 'enter multiple lines here')

# focus on a particular box
input_more.focus()

# checkbox
var = IntVar()
def check_checkbox():
    print(var.get())
check = Checkbutton(text='is it working?', variable=var, command=check_checkbox)
check.grid(column=4, row=5)

# radiobutton
var1 = StringVar()
var1.set('none')
def check_radio():
    print(var1.get())
r1 = Radiobutton(text='option 1', value='option 1', variable=var1, command=check_radio)
r2 = Radiobutton(text='option 2', value='option 2', variable=var1, command=check_radio)
r1.grid(column=5,row=6)
r2.grid(column=4,row=7)


window.mainloop()

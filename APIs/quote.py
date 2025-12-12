import requests
from tkinter import *

def find():
    connection = requests.get('https://api.kanye.rest')
    data = connection.json()
    quote = data['quote']
    print(quote)
    text.config(text=quote, font=('Arial', 20, 'bold'))

window = Tk()
window.minsize(400,400)
window.title('quote machine')
text = Label(text='the quote will be shown here', font=('Arial', 20, 'bold'))
generate = Button(text='fetch quote', command=find)
text.pack()
generate.pack()


window.mainloop()
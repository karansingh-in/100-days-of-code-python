from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Segoe UI"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('pomodoro')
window.config(bg=YELLOW, padx=50, pady=50)

tomato = PhotoImage(file='tomato.png')
canv = Canvas(height=270, width=250, highlightthickness=0, bg=YELLOW)
canv.create_image(135,140, image=tomato)
canv.create_text(135,160, text='00:00', fill='white', font=(FONT_NAME, 18, 'bold'))

timer_label = Label(text='Pomodoro Timer', fg=GREEN, font=(FONT_NAME, 32, 'bold'), highlightthickness=0, bg=YELLOW)
start_button = Button(text='Start')
Reset_button = Button(text='Reset')

count = Label(text='✔️', bg=YELLOW)

timer_label.grid(row=0, column=1)
canv.grid(row=1, column=1)
start_button.grid(row=2, column=0)
Reset_button.grid(row=2, column=2)
count.grid(row=2, column=1)







window.mainloop()
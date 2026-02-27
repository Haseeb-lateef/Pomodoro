from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
tick = "✔"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#putting the tomato on the window
canvas = Canvas(width= 200,height= 224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=img)
canvas.create_text(100,130, fill="white", text="00:00", font=(FONT_NAME,35,"bold"))
canvas.grid(column=2, row=2)

#label for timer text
timer_label = Label(text="Timer", font=(FONT_NAME,35,"bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)


#start and reset button
start_btn = Button(text="Start")
reset_btn = Button(text="Reset")
start_btn.grid(column=1,row=3)
reset_btn.grid(column=3,row=3)


#code for Pomodoro checkmark
tick_label = Label(text=tick, fg= GREEN, bg=YELLOW, font=(FONT_NAME,15,"bold"))
tick_label.grid(column=2, row=4)







window.mainloop()

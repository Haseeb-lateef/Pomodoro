from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
tick = "✔"
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_countdown():
    global reps
    reps +=1
    l_break_sec = LONG_BREAK_MIN * 60
    s_break_sec = SHORT_BREAK_MIN * 60
    work_sec = WORK_MIN * 60

    if reps % 8 == 0:
        countdown(l_break_sec)
        timer_label.config(text="Break", fg=GREEN)



    elif reps % 2 == 0:
        countdown(s_break_sec)
        timer_label.config(text="Break", fg=GREEN)

    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=RED)







# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"



    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000,countdown,count-1)
    else:
        start_countdown()




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



#putting the tomato on the window
canvas = Canvas(width= 200,height= 224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=img)
timer_text = canvas.create_text(100,130, fill="white", text="00:00", font=(FONT_NAME,35,"bold"))
canvas.grid(column=2, row=2)

#label for timer text
timer_label = Label(text="Timer", font=(FONT_NAME,35,"bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)



#start and reset button
start_btn = Button(text="Start",command=start_countdown)
reset_btn = Button(text="Reset")
start_btn.grid(column=1,row=3)
reset_btn.grid(column=3,row=3)


#code for Pomodoro checkmark
tick_label = Label(text=tick, fg= GREEN, bg=YELLOW, font=(FONT_NAME,15,"bold"))
tick_label.grid(column=2, row=4)







window.mainloop()

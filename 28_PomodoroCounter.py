import math
from tkinter import *

# Constants
GREEN = "#9bdeac"
RED = "#e7385b"
YELLOW = "#f7f5dd"
FONT_NAME = "Helvetica"
PINK = "#e2979c"
WORK_MIN = 25
SHORT_BREAK = 5
LONG_BREAK = 20
REPS = 0
timer_time = None


# Timer reset
def reset_timer():
    global REPS
    REPS = 0
    window.after_cancel(timer_time)
    timer.config(text="Timer", fg="black")
    canvas.itemconfig(change_timer, text="00:00")
    count.config(text="")


# mechanism
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK * 60
    long_break = LONG_BREAK * 60

    if REPS % 8 == 0:
        count_down(long_break)
        timer.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)


# countdown
def count_down(count):
    global REPS
    minutes = math.floor(count / 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(change_timer, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer_time
        timer_time = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(REPS / 2)):
            mark += "🗸"
        count.config(text=mark)


# UI
window = Tk()
window.title("Pomodoro technique")
window.config(padx=100, pady=100)

canvas = Canvas(width=400, height=400)
change_timer = canvas.create_text(200, 200, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer = Label(text="Timer", font=(FONT_NAME, 38, "bold"))
timer.grid(column=1, row=0)

start = Button(text='Start', command=start_timer)
start.grid(column=0, row=2)

count = Label(text="", fg=GREEN, font=(FONT_NAME, 30, "bold"))
count.grid(column=1, row=3)

reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()

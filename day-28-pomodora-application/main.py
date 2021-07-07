from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    label_title.config(text="Timer", fg=GREEN)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="✔")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    # print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        label_title.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        label_title.config(text="Break", fg=RED)
        count_down(long_break_sec)
    else:
        label_title.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += " ✔"
        check_mark.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
canvas.grid(column=1, row=1)

# lable
label_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "normal"))
label_title.grid(column=1, row=0)
check_mark = Label(text="✔", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

# buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()

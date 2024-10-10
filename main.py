from tkinter import *
import math

# ---------------------------- CONSTANTS ----------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ---------------------------- #
def reset_timer():
    canvas.itemconfig(timer_count, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------ #
def start_timer():
    global reps
    count_down(1 * 60)
# ---------------------------- COUNTDOWN MECHANISM -------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 0:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW,
                    font=(FONT_NAME, 45, "bold"))
check_label = Label(text="✓", fg=GREEN, bg=YELLOW,
                    font=(FONT_NAME, 35, "bold"))
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_count = canvas.create_text(100, 130, text="00:00", fill="white",
                                 font=(FONT_NAME, 35, "bold"))

timer_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=3, column=0)
check_label.grid(row=4, column=1)
reset_button.grid(row=3, column=2)

window.mainloop()

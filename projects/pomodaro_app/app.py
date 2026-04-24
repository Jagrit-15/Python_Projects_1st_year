from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.15
reps = 0
timer = None

def count_down(count):
    global timer
    
    if count/60 <10 and count%60 < 10:
        canvas.itemconfig(timer_count , text = f"0{int(count/60)}:0{int(count%60)}")
    elif count/60 >=10 and count%60 < 10:
        canvas.itemconfig(timer_count , text = f"{int(count/60)}:0{int(count%60)}")
    elif count/60 <10 and count%60 >= 10:
        canvas.itemconfig(timer_count , text = f"0{int(count/60)}:{int(count%60)}")
    elif count/60 >=10 and count%60 >= 10:
        canvas.itemconfig(timer_count , text = f"{int(count/60)}:{int(count%60)}")

    if count>0 :
       timer = window.after(1000 ,count_down ,count-1)
    else:
        start_timer()
        marks =""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        check_mark.config(text=marks)
        
def reset_timer():
    global reps
    reps=0
    label1.config(text="Timer" , fg=GREEN)
    check_mark.config(text="")
    window.after_cancel(timer)
    canvas.itemconfig(timer_count , text ="25:00")


def start_timer():
    global reps
    reps +=1
    work_time = WORK_MIN * 60
    short_brk_time = SHORT_BREAK_MIN * 60
    long_brk_time = LONG_BREAK_MIN * 60

    if(reps % 8 == 0):
        count_down(long_brk_time)
        label1.config(text="Break" , fg=RED)
    elif(reps % 2 == 0):
        count_down(short_brk_time)
        label1.config(text="Break" , fg=PINK)
    else:
        count_down(work_time)
        label1.config(text="Work" , fg=GREEN)
    

window = Tk()
window.title("Pomodaro")
window.config(padx=100 , pady=100 , bg=YELLOW)

canvas = Canvas(width=202, height=224 , bg=YELLOW , highlightthickness=0)
tomato_img = PhotoImage(file=r"projects\pomodaro_app\tomato.png")
canvas.create_image(102,112,image=tomato_img)
timer_count = canvas.create_text(102,130,text="25:00",fill="white", font=(FONT_NAME , 25 , "bold"))
canvas.grid(row=1,column=1)
 
label1 = Label(text="Timer" , fg=GREEN , width=10 , bg=YELLOW , highlightthickness=0)
label1.configure(font=(FONT_NAME , 50 , "bold"))
label1.grid(row=0 , column=1)

reset = Button(text="Reset" , highlightthickness=0 , command=reset_timer)
reset.grid(row=2 , column=2)

check_mark = Label(text="" , fg=GREEN , bg=YELLOW , highlightthickness=0)
check_mark.grid(row=3 , column=1)

start = Button(text="Start" , highlightthickness=0 , command=start_timer)
start.grid(row=2 , column=0)


window.mainloop()
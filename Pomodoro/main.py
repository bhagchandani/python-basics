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
	window.after_cancel(timer)
	timerlable.config(text="Timer")
	canvas.itemconfig(timer_text, text="00:00")
	checklable.config(text="")
	global reps
	reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
	global reps
	reps += 1
	work_sec = WORK_MIN * 60
	short_break_sec = SHORT_BREAK_MIN * 60
	long_break_sec = LONG_BREAK_MIN * 60

	if(reps % 8 == 0):
		timerlable.config(text="Break", fg=RED)
		count_down(long_break_sec)
	elif(reps % 2 == 0):
		timerlable.config(text="Break", fg=PINK)
		count_down(short_break_sec)
	else:
		timerlable.config(text="Work", fg=GREEN)
		count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

#The window is the mail loop it runs in each mili second if we add another loop in that
# it won't run or execute the programm so when we use GUI programm we do not use timer class we use window.after
# it will call itself and it keeps running when we call start button
def count_down(count):
	global reps
	hour = math.floor(count / 60)
	minutes = count % 60

	if minutes < 10:
		minutes = f"0{minutes}"

	canvas.itemconfig(timer_text, text=f"{hour}:{minutes}")
	if count > 0:
		global timer
		timer = window.after(1000, count_down, count - 1)
	else:
		start_timer()
		marks = ""
		work_sessions = math.floor(reps/2)
		for _ in range(work_sessions):
			marks +=  "✓"
		
		checklable.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)



#we need to add the tomoto image in the window for which
#we can use the canvas widget of tkinter

timerlable = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 26, "bold"))
timerlable.grid(column=1, row=0)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
#canvas create image function only accept image from another class
#of tkinter which is PhotoImage
photo = PhotoImage(file='tomato.png')
#initial parameter is 100 and 112 to which specifiy as center 
canvas.create_image(105,112, image=photo)
timer_text = canvas.create_text(105,135, text="00:00",fill="white", font=(FONT_NAME, "24", "bold"))
canvas.grid(column=1, row=1)


#start button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

#Reset button
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

#Check Mark
checklable = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, "14", "bold"))
checklable.grid(column=1, row=3)



window.mainloop()
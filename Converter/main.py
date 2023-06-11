from tkinter import *

def miles_to_converter():	
	value = float(inputtext.get())
	kmconveted = value*1.609
	convertlabel.config(text=kmconveted)


window = Tk()
window.title("Mile to Km Converter")
#To add padding in the main window
window.config(padx=20, pady=20)

#Entry Or layman term it is textbox
inputtext = Entry(width=10)
inputtext.focus()
inputtext.grid(column=1, row=0)

#Label
milelabel = Label(text="Miles",font=("Arial", 14, "normal"))
milelabel.grid(column=2, row=0)
#Label
equallabel = Label(text="is equal to",font=("Arial", 14, "normal"))
equallabel.grid(column=0, row=1)

#Label
convertlabel = Label(text="0",font=("Arial", 14, "normal"))
convertlabel.grid(column=1, row=1)

kmlabel = Label(text="KM",font=("Arial", 14, "normal"))
kmlabel.grid(column=2, row=1)

#Button
button = Button(text="Calculate", command=miles_to_converter)
#button.pack()
button.grid(column=1, row=2)


window.mainloop()
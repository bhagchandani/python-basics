from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
	password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
	password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

	random.shuffle(password_list)

	password = "".join(password_list)

	passwordText.delete(0,'end')
	passwordText.insert(0,password)
	pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

	website = websiteText.get()
	email = emailuserText.get()
	password = passwordText.get()

	if(len(website) == 0 or len(password) == 0):	
		is_error = messagebox.showinfo(title="Oops", message="Please don't leave any field empty ")
	else:
		response = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password}\nIs it okay to save?")

		# test_to_write = website + " | " + email + " | " + password+ " \n"

		# file = open("data.txt", "a")
		# file.write(test_to_write)
		# file.close()

		#or
		if(response):
			with open("data.txt", "a") as data_file:
				data_file.write(f"{website} | {email} | {password}\n")

			websiteText.delete(0,'end')
			passwordText.delete(0,'end')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200,highlightthickness=0)
#of tkinter which is PhotoImage
photo = PhotoImage(file='logo.png')
#initial parameter is 100 and 112 to which specifiy as center 
canvas.create_image(100,100, image=photo)
canvas.grid(column=1, row=0)

#Website Label
websiteLable = Label(text="Website: ", font=(FONT_NAME, "10"))
websiteLable.grid(column=0, row=1)

#Website Input
websiteText = Entry(width=52)
websiteText.grid(column=1, row=1, columnspan=2)
websiteText.focus()

#Email/User Label
emailuserLable = Label(text="Email/Username: ", font=(FONT_NAME, "10"))
emailuserLable.grid(column=0, row=2)

#Website Input
emailuserText = Entry(width=52)
emailuserText.grid(column=1, row=2, columnspan=2)
#To auto fille the email address
emailuserText.insert(0,'beenatest@gmail.com')

#Password Label
passwordLable = Label(text="Password: ", font=(FONT_NAME, "10"))
passwordLable.grid(column=0, row=3)

#Password Input
passwordText = Entry(width=33)
passwordText.grid(column=1, row=3)

#Password Button
password_button = Button(text="Generate Password", command=password_generator)
password_button.grid(column=2, row=3)

#Password Button
add_button = Button(width=44,text="Add", command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

def save_details():
    website = web_entry.get().title()
    email = user_entry.get()
    password = password_entry.get()
    
    new_data = {
                    website :
                    {
                        "Email" : email,
                        "Password" : password
                    }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="OOPS" , message="Please enter all the fields")
    else:
        is_ok = messagebox.askokcancel(title=website , message=f"These are the details entered :\n"
                                    f"Email/Username : {email}\nPassword : {password}")

        if is_ok:
            try :
                with open(r"projects\password_manager\password.json" , "r") as data_file:
                    # Reading old data 
                    data = json.load(data_file)
                    # Updating old data with new data 
                    data.update(new_data)

            except(FileNotFoundError):
                with open(r"projects\password_manager\password.json" , "w") as data_file:
                    # saving updated data 
                    json.dump(new_data, data_file , indent=4)
                    web_entry.delete(0,END)
                    password_entry.delete(0,END)

            else:
                with open(r"projects\password_manager\password.json" , "w") as data_file:
                    # saving updated data 
                    json.dump(data, data_file , indent=4)
                    web_entry.delete(0,END)
                    password_entry.delete(0,END)
def search_details():
    try:
        with open(r"projects\password_manager\password.json" , "r") as data_file:
                    details = json.load(data_file)
        website = details[web_entry.get().title()]
        email = website["Email"]
        password = website["Password"]
        messagebox.showinfo(title=web_entry.get() , message=f"Email : {email}\nPassword : {password}")
        web_entry.delete(0,END)
        password_entry.delete(0,END)
    
    except(FileNotFoundError):
         messagebox.showerror(message="Website not added")

    except(KeyError):
         messagebox.showerror(message="Website not added")
    

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

window = Tk()
window.title("Password Manager")
window.config(padx=20 , pady=20)

logo_img = PhotoImage(file= r"projects\password_manager\logo.png")
canvas = Canvas(width=202 , height=192)
canvas.create_image(101 , 96 , image  = logo_img)
canvas.grid(row=0 , column=1)

web_label = Label(text="Website : ")
web_label.grid(row=1 , column=0 , sticky="e" , ipadx=5 , ipady=5)
web_entry = Entry(width=25)
web_entry.grid(row=1 , column=1 , sticky="e")
web_entry.focus()

user_label = Label(text="Email/Username : ")
user_label.grid(row=2 , column=0 , sticky="e", ipadx=5 , ipady=5)
user_entry = Entry(width = 44)
user_entry.grid(row=2 , column=1 , columnspan=2 , sticky="e")
user_entry.insert(0,"jagritpramanick@gmail.com")

password_label = Label(text="Password : ")
password_label.grid(row=3 , column=0 , sticky="e", ipadx=5 , ipady=5)
password_entry = Entry(width = 25)
password_entry.grid(row=3, column=1 , sticky="e")

generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3 , column=2 , ipadx=2)

add = Button(text="Add" , width=37 , command=save_details)
add.grid(row=4 , column=1 , columnspan=2, sticky="se")

search = Button(text = "Search" , command=search_details , width=13)
search.grid(row = 1 , column=2 , ipadx=2)
window.mainloop()


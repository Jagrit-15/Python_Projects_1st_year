from tkinter import *

window = Tk()
window.config(padx=5 , pady=10)
window.geometry("300x100")

for i in range(3):
    window.columnconfigure(i,weight=1,uniform="my_grid")
    window.rowconfigure(i,weight=1,uniform="my_grid")

def miles_to_km():
    mv = float(input_miles.get())
    km = 1.6*mv
    result.configure(text=f"{round(km,2)}")

input_miles = Entry(width=10 , justify="center")
input_miles.grid(column=1, row=0 , sticky="n")


miles = Label(text="Miles" , anchor="nw")
miles.grid(column=2, row=0,sticky="nw")

is_label = Label(text="is equal to" , anchor="e")
is_label.grid(column=0,row=1 , sticky="e")

result = Label(text = "0")
result.grid(column=1 , row=1)

km = Label(text="km", anchor="w")
km.grid(column=2,row=1 , sticky="w")

calculate = Button(text="Calculate" , command=miles_to_km)
calculate.grid(column=1 , row=2)

window.mainloop()
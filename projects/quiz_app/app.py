import requests
import json
from tkinter import *

score = 0
question_number = 1

parameters = {
    "amount" : 10,
    "category" : 22,
    "difficulty" : "easy",
    "type" : "boolean"
}

# CREATING THE API AND FETCHING QUESTIONS
response = requests.get(url ="https://opentdb.com/api.php" , params=parameters)
response.raise_for_status()
with open(r"projects\quiz_app\questions.json" , "w") as question_file:
    data = response.json()
    json.dump(data , question_file , indent=4)\
    
# CHECKING ANSWER
def check_correct():
    global score
    answer = response.json()["results"][question_number-1]["correct_answer"]
    if answer=="True":
        score+=1
        canvas.config(bg="#59C194")
        canvas.itemconfig(score_text , text=f"Score : {score}")
    else:
        canvas.config(bg="#F08060")
    
    window.after(1000,get_next_question)

def check_incorrect():
    global score
    answer = response.json()["results"][question_number-1]["correct_answer"]
    if answer=="False":
        score+=1
        canvas.config(bg="#59C194")
        canvas.itemconfig(score_text , text=f"Score : {score}")   
    else:
        canvas.config(bg="#F08060")

    window.after(1000,get_next_question)
   

# GETTING THE NEXT QUESTION 
def get_next_question():
    global question_number
    question_number+=1
    if question_number <=10:
        canvas.config(bg="white")
        canvas.itemconfig(question , text = response.json()["results"][question_number-1]["question"])
    else:
        canvas.config(bg="white")
        canvas.itemconfig(question , text = f"YOUR SCORE : {score}/10")
        correct.config(state="disabled")
        wrong.config(state="disabled")
    

# CREATING THE USER INTERFACE 
window = Tk()
window.title("Quiz")
window.config(padx=20 , pady=20 ,bg="black")

canvas = Canvas(width=400 , height=400)
question = canvas.create_text(200 , 200 ,text=response.json()["results"][0]["question"] , font = ("Courier New" , 24 , "bold"), justify="left" , width=400 , anchor="center")
canvas.grid(row=0 , column=0 , columnspan=3 , pady=(0,10))
score_text = canvas.create_text(360 , 10 , text="Score : 0" , font=("arial" , 10 , "bold"))

correct_img = PhotoImage(file=r"projects\quiz_app\true.png")
correct = Button(image=correct_img ,highlightthickness=0 ,command=check_correct)
correct.grid(row=1 , column=0)

wrong_img = PhotoImage(file=r"projects\quiz_app\false.png")
wrong = Button(image=wrong_img , highlightthickness=0 ,command=check_incorrect)
wrong.grid(row=1 , column=2)

window.mainloop()
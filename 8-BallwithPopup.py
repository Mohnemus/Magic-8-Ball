#This is a test to try out pop-up windows, just wanted to test this out! I think that this is a pretty fun little program haha


import tkinter as tk
from tkinter import simpledialog
import random

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
def runit():
    return(print("Let's run it again!"))
    

USER_INP = simpledialog.askstring(title="Name",
                                  prompt="Welcome to the Magic 8-Ball! What's your Name?")
name = USER_INP
USER_INP_2 = simpledialog.askstring(title="Question",
                                  prompt="Hello "+name+"! What is your Question?")
question = USER_INP_2
answer = ""
random_number = random.randint(1,9)
#print(random_number)
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is absolutely so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "I'm not too sure, try again."
elif random_number == 5:
  answer = "I'm thinking the answer is probably yes."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say probably not."
elif random_number == 8:
  answer = "The outlook isn't so good."
elif random_number == 9:
  answer = "Doubtful, sorry!"
else:
  answer = "Error"


# print(name + " Asks: " + question)
# print("Magic 8-Ball's answer: " + answer)
USER_Ans = simpledialog.askinteger(title="Q: "+question,prompt="Answer: "+answer+"        ....Please hit enter to end program, or 1 to ask another question")
if USER_Ans == 1:
    runit()


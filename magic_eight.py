
from random import randrange

result=[]
def ask(): 
    user_input = input("What is your name?")
    question = ""
    q_list = []
    while question != "quit":
        question = input("What's your question?(ends with '?')('quit' for quit)")
        if question[-1] == "?":
            print(pick_answer())
            q_list.append(question)
        elif question == "quit":
            break
        else:
            input("I'm sorry, I can only answer questions. Ask again.")

#person B
#In the magic_eight.py file add code to pick an answer at random from the 20 possible 8 ball answers.
import random
def pick_answer():
    answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

    return random.choice(answers)


ask_question()





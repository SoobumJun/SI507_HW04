#personA

from random import randrange

result=[]
def ask(): 
    user_input = input("What is your name?")

#person B
#In the magic_eight.py file add code to pick an answer at random from the 20 possible 8 ball answers.
    if user_input is "":
        answer = user_input
        answer = [
        'It is certain', 
        'It is decidedly so', 
        'Without a doubt', 
        'Yes definitely', 
        'You may rely on it',
        'As I see it, yes',
        'Most likely',
        'Outlook good',
        'Yes',
        'Signs point to yes',
        'Reply hazy try again',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again',
        "Don't count on it",
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'Very doubtful'
        ]

        random_index = randrange(0,len(answer))
        print (answer[random_index])
        result.append(answer)
    else:   
        result.append(answer)
    return(result)

ask()

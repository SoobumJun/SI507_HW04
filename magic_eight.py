result=[]
def ask(): 
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
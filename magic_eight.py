result=[]
def ask(): 
    user_input = input("What is your name?")
    result.append(user_input)
    return(result)

print(ask())
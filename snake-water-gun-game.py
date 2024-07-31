import random as r

def win_or_loss(value1 , value2):
    if(value1 == value2):
        print("Its a Draw!!")
    else:
        if(value1 == "snake" and value2 == "water"):
            print("Computer Win!!")
        elif(value1 == "snake" and value2 == "gun"):
            print("You Win!!")
        elif(value1 == "water" and value2 == "gun"):
            print("Computer Win!!")
        elif(value1 == "water" and value2 == "snake"):
            print("You Win!!") 
        elif(value1 == "gun" and value2 == "snake"):
            print("Computer Win!!")
        elif(value1 == "gun" and value2 == "water"):
            print("You Win!!")
        else:
            print("Invalid Input!!")

def code():
    userdict = {
            "snake":1,
            "water":-1,
            "gun":0
        }
    words = ["snake" , "water" , "gun"]
    computer_choice = r.choice(words).lower()
    comp_num = userdict[computer_choice] 
    user_input = input("Enter your choice: ").lower()
    your_num = userdict[user_input]
    print(f" YOUR CHOICE IS {user_input} AND COMPUTER CHOICE IS {computer_choice}")
    win_or_loss(computer_choice , user_input)


input(" Press enter to start the game.....")
print("\t\t WELCOME TO THE SANKE,WATER AND GUN GAMES!!!!!!")
code()

while(True):
    value = input("You want to Continou the Game!!! ").title()
    if(value=="Yes"):
        code()
    else:
        break    

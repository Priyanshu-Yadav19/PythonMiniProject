import random
def game():
    computer =random.choice (['rock', 'paper', 'scissor'])  
    user=input("enter your choice (rock,paper,scissor) : ").lower() # takes input from user 
    
    if user in (['rock', 'paper', 'scissor']):  
        print(f" computer choice : {computer}")
        print(f" you choice : {user}")
        if computer==user:
            print("its draw ! ")
        elif (computer=='rock' and user=='paper')or(computer=='paper' and user=='scissor')or(computer=='scissor' and user=='rock'):
            print("you win ")              
                                    
        else :
            print("you lose ! ")
    else :
        print("invalid choice")                                          

while True: 
    game() 
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay != 'yes': 
        break 
print("Thanks for playing!")
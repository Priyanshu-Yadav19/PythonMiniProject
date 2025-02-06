import random

def random_event():
    event = random.choice(["find treasure", "meet a stranger", "encounter danger","lost","devil"])
    if event == "find treasure":
        print("You found a hidden treasure!")
       
    elif event == "meet a stranger":
        print("You meet a friendly stranger who offers you help.")
    elif event == "encounter danger":
        print("Oh no! You encountered danger and lost life.")
        quit()
    elif event == "lost":
        print("Oh no! You  lost your closer one .")

  
while(True):
    a=input("want to play Yes or No ! ").lower()
    if(a=='yes'):
        userchoice=input("welcome ! : \n Where you want to go Left or rigth " ).lower()    
        if(userchoice=='left'):
               random_event()
               
        elif(userchoice=='right'):
              random_event()
        else:
            print("invalid choice : \t try again ")        
    else:    
         quit()     

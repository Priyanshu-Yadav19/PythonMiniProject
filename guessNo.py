import random
def guess():
    attemp=0
    # Generate a random number between 1 and 99
    computer=random.randint(1,99)
    while True:
        attemp+=1
            # Get the user's guess
        user=int(input("enter your guess number : "))
        if(user==computer):
            print(f"correct guess in {attemp} attemps ! ")
            break
        elif user < computer:
            print("The number is greater than your guess.")
        elif user > computer:
            print("The number is less than your guess.")
while True: 
    guess() 
    play = input("Do you want to play again? (yes/no): ").lower()
    if play != 'yes': 
        break 
print("Thanks for playing !")
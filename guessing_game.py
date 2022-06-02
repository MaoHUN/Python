import random
##Guessing game.
def my_game():
    print("Lets play a Game! guessing game. I think a number 1-100")
    pc_num = int(random.randrange(1,100))
    #Debugint uncomment this print()
    #print(pc_num)
      
    user_number = int(input("Give me a number Human!: "))
    while user_number == True:
             if user_number > pc_num:
                print("Too high. \n")
             elif user_number < pc_num :
                print("too low \n")
             else:
                print("Yes my number is: ", pc_num, "\n" )
                print("Do you want to play more? \n")
                False
            
                more = str(input("Yes or No \n"))
                more = str(input("Do You wanna play? Yes or No?\n"))
                while more == True:                    
                    if more == "y" :
                        my_game()
                    elif more == "yes" :
                        my_game()
                    elif more == "no" :
                        print("Thanks for the game")
                        False
                        break
                    elif more == "n" :
                        print("Thanks for the game")
                        False
                        break
                    else :
                        print("I dont understand.")        
                    break
                           
def start():
    while True:
        start = str(input("Do You wanna play? Yes or No?\n"))
        if start == "y" :
            my_game()
        elif start == "yes" :
            my_game()           
        elif start == "no" :
            print("Bye")
            False
            break
        elif start == ("n") :
            print("bye")
            False
            break
        else :
            print("I dont understand.")
            True

start()
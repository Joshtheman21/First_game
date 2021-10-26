print("Welcome to my first game")

name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10

if age >= 18:
    print(" You are old enough to play: ")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health")
        print("Let's play!")
        
        left_or_right = input("\nFirst choice....Left or Right(left or right)? ")
        if left_or_right == "left":
            
            ans = input("\nPerfect choice, you followed the path and now reach a lake. Do you swim across or go around? (across/around)")
            
            if ans == "around":
                print("\nYou're on a roll you made it to the other side.")
            
            elif ans == "across":
                print("\nWow you're brave! On your way across the lake a fish bit the back of your leg. You lost 5 health. " )
                health -= 5
            
            ans = input("You notice a house and river. Which do you go to? (river/house)")
            if ans == "house":
               print("\nYou go to the house and you are greeted by the one and only, Michael Myers. You lose 5 health.")
               health -= 5
                
               if health <= 0:
                    print("\nYou now have 0 health, and you lost the game.")
               else:
                    print("\nYou survived...not only did you get away from Michael, but you won the game! ")
                
            
            else:
                print("\nThe river was too deep...you lose")
        
        
        else:
            print("\nYou fell down and lost")
    
    else:
        print("\nOk, goodbye! ")

else:
    print("\nSorry, you aren't old enough to play...")
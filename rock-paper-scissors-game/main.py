import random

options = ["R", "P", "S"]

player_name = input("What name may I call you? ")
greeting = "Hi " + player_name + ", You're welcome to our game: Rock-Paper-Scissors(R-P-S). "  
instruction = "You will be playing against the CPU (i.e Computer). \n \n You will choose one option among R, P and S. \n While the CPU choose at random in return. \n \n Game rules: Rock beats Scissors; \t Paper beats Rock; \t Scissors beats Paper. \n Enjoy! Game starts"

print("\n" + greeting + "\n \n" + instruction)

def player():
    player_choice = input("Enter your choice- R or P or S: ").upper()
    print ("")

    if player_choice in options:
        return player_choice
    else:
        print ("Oops! wrong input- Try again \n")
        player()

def comp():
    cpu_choice = random.choice(options)
    return cpu_choice

def play_game():
    print ("")
    player_choice = player()
    cpu_choice = comp()

    while True:
        if player_choice == cpu_choice:
            print(player_name + " chose: " + player_choice)
            print("Computer chose: " + cpu_choice)
            print("It's a tie, computer and player pick same option. kindly Replay")
            play_game()
        elif player_choice == "R":
            if cpu_choice == "P":
                print("Player(Rock) : CPU(Paper)")
                print("CPU wins \n")
            elif cpu_choice == "S":
                print("Player(Rock) : CPU(Scissors)")
                print("Player wins \n")
        elif player_choice == "P":
            if cpu_choice == "R":
                print("Player(Paper) : CPU(Rock)")
                print("Player wins \n")
            elif cpu_choice == "S":
                print("Player(Paper) : CPU(Scissors)")
                print("CPU wins \n")
        elif player_choice == "S":
            if cpu_choice == "R":
                print("Player(Scissors) : CPU(Rock)")
                print("CPU wins \n")
            elif cpu_choice == "P":
                print("Player(Scissors) : CPU(Paper)")
                print("Player wins \n")
        break
    print ("Thanks for playing. Game is over.")

    player_choice = input("Reply to play again? (yes/no or y/n): ")
    if player_choice in [ "Y", "y", "yes", "Yes", "YES"]:
        play_game()
    elif player_choice in ["N", "n", "no", "No", "NO"]:
        print ("Bye " + player_name  + ". Come back later")
    else:
         print ("Hey " + player_name + "! You enter wrong response! Bye for now." )
         exit()
        
play_game()



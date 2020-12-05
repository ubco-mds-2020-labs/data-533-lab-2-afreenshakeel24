from .rpshelp_sheldon import rpshelp_sheldon
import time
import random
import os
class rpsgame_sheldon(rpshelp_sheldon):
    def __init__(self):
        rpshelp_sheldon.__init__(self)
    def display(self):
        rpshelp_sheldon.display(self)
    def game_rps_sheldon(self):
        print("\n \n Welcome to Sheldon's version of the GAME ")
        time.sleep(2)
        print("\n Ready... Steady... GO! \n")
        
        while True:
            ins = input("Do you want to see the instructions? Type yes or no :")
            if ins.lower() == "yes":
                print("Loading instructions...")
                time.sleep(3)
                rpshelp_sheldon.display(self)
            elif ins.lower() == "no":
                pass
            else: 
                print("YOU HAD ONE JOB \n")
                continue
                
            print("Enter \"Rock\",\"Paper\",\"Scissors\",\"Lizard\",\"Spock\" to play")
            print("Enter \"exit\" to quit")
            print("--------------------------------------")
            time.sleep(2)
            inp = input("Enter your move : ")
            if inp.lower() == "exit":
                break  
            elif inp.lower() == "rock":
                player_move = 0
            elif inp.lower() == "paper":
                player_move = 1    
            elif inp.lower() == "scissors":
                player_move = 2
            elif inp.lower() == "lizard":
                player_move = 3
            elif inp.lower() == "spock":
                player_move = 4
            
            else:
                print("\n \n IT IS NOT ROCKET SCIENCE. TYPE IT PROPERLY. \n \n") 
                continue
            print("Computer making a move...")
            time.sleep(2)
            comp_move = random.randint(0, 4)

            # Print the computer move
            if comp_move == 0: print("Computer chooses... Rock")
            elif comp_move == 1: print("Computer chooses... Paper")
            elif comp_move == 2: print("Computer chooses... Scissor")
            elif comp_move == 3: print("Computer chooses... Lizard")
            elif comp_move == 4: print("Computer chooses... Spock")
            
            print()
            
            if player_move == comp_move: print("IT'S A TIE! \n\n")
            elif player_move == 2 and comp_move == 1: print("PLAYER WINS \n\n")
            elif player_move == 1 and comp_move == 2: print("COMPUTER WINS \n\n")
            elif player_move == 1 and comp_move == 0: print("PLAYER WINS \n\n")
            elif player_move == 0 and comp_move == 1: print("COMPUTER WINS \n\n")
            elif player_move == 0 and comp_move == 3: print("PLAYER WINS \n\n")
            elif player_move == 3 and comp_move == 0: print("COMPUTER WINS \n\n")
            elif player_move == 3 and comp_move == 4: print("PLAYER WINS \n\n")
            elif player_move == 4 and comp_move == 3: print("COMPUTER WINS \n\n")
            elif player_move == 4 and comp_move == 2: print("PLAYER WINS \n\n")
            elif player_move == 2 and comp_move == 4: print("COMPUTER WINS \n\n")
            elif player_move == 2 and comp_move == 3: print("PLAYER WINS \n\n")
            elif player_move == 3 and comp_move == 2: print("COMPUTER WINS \n\n")
            elif player_move == 3 and comp_move == 1: print("PLAYER WINS \n\n")
            elif player_move == 1 and comp_move == 3: print("COMPUTER WINS \n\n")
            elif player_move == 1 and comp_move == 4: print("PLAYER WINS \n\n")
            elif player_move == 4 and comp_move == 1: print("COMPUTER WINS \n\n")
            elif player_move == 4 and comp_move == 0: print("PLAYER WINS \n\n")
            elif player_move == 0 and comp_move == 4: print("COMPUTER WINS \n\n")
            elif player_move == 0 and comp_move == 2: print("PLAYER WINS \n\n")
            elif player_move == 2 and comp_move == 0: print("COMPUTER WINS \n\n")
            else: print("Nothing \n\n")
            time.sleep(5)
            print()
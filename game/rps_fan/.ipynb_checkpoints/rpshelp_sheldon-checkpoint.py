class rpshelp_sheldon:
    def __init__(self):
        self.models = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    def display(self): 
        print('You have to choose from: ') 
        for model in self.models:
            print('%s ' % model)
        print("\n \n How does it work? \n \n")
        print("\n Scissors cuts Paper \n Paper covers Rock \n Rock crushes Lizard \n Lizard poisons Spock \n Spock smashes Scissors \n Scissors decapitates Lizard \n Lizard eats Paper \n Paper disproves Spock \n Spock vaporizes Rock \n Rock crushes Scissors")
        print("")
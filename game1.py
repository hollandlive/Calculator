#artem aksenov @hollandlive 26-02-2015
#my first python logical game
#that i borrowed from coursera
#here is description
#Scissors Cuts Paper 
#Covers Rock Crushes 
#Lizard Poisons Spock 
#Smashes Scissors Decapitates 
#Lizard Eats Paper 
#Disproves Spock Vaporizes 
#Rock Crushes Scissors
#there is one bug
#so you can
#debug it yoursel:)


import random

def name_to_number(name):
    if name == 'rock':
        name = 0
    elif name == 'Spock':
        name = 1
    elif name == 'paper':
        name = 2
    elif name == 'lizard':
        name = 3
    elif name == 'scissors':
        name = 4
    else:
        print 'only 5 words above'
    return name
#name = 'lizard'    
#print name_to_number(name)

def number_to_name(number):
    if number == 0:
        number = 'rock'
    elif number == 1:
        number = 'Spock'
    elif number == 2:
        number = 'paper'
    elif number == 3:
        number = 'lizard'
    elif number == 4:
        number = 'scissors'
    else:
        print 'only numbers 0 - 4'
    return number
#number = 3   
#print number_to_name(number)
    

def rpsls(player_name):
    
    print ''
    print 'Player chooses', player_name

    player_number = name_to_number(player_name)
    comp_number = random.randrange (0,5) 
    comp_name = number_to_name(comp_number)
    print 'Computer chooses', comp_name
    win_formula = (player_number + comp_number) % 4
    if comp_number == player_number:
        print 'Player and computer tie!'
    else:
        if win_formula == 3:
            print 'Player wins'
        else:
            print 'Computer wins'
    
    
print rpsls('rock')
print rpsls('Spock')
print rpsls('paper')
print rpsls('lizard')
print rpsls('scissors')
from IPython.display import clear_output
clear_output()


def display_game(p):
    print(p[0], '|', p[1], '|', p[2])
    print('----------')
    print(p[3], '|', p[4], '|', p[5])
    print('----------')
    print(p[6], '|', p[7], '|', p[8])


# Move assigner
def move_p1(n, p):
    if p[n] != '':
        return False
    else:
        p[n] = 'O'
        
def move_p2(n, p):
    if p[n] != '':
        return False
    else:
        p[n] = 'X'


def win_detect(p):
    # rows
    if (p[0:3] or p[3:6] or p[6:9]) == (['O', 'O', 'O'] or ['X', 'X', 'X']):
        print(1)
        return True
    
    # columns
    elif ([p[0], p[3], p[6]] or [p[1], p[4], p[7]] or [p[2], p[5], p[8]]) == (['O', 'O', 'O'] or ['X', 'X', 'X']):
        print(2)
        return True
        
    # diagonals
    elif ([p[0], p[4], p[8]] or [p[2], p[4], p[6]]) == (['O', 'O', 'O'] or ['X', 'X', 'X']):
        print(3)
        return True 
    
    else:
        return False


def position_choice():
    choice = 'wrong'

    while choice not in game_list:
        choice = input("Pick a position to replace (1, 2, ..., 9): ")
        if choice not in game_list:
            clear_output()
            print("Sorry, but you did not choose a valid position (0,1,2)")
    return int(choice)


# Variable to keep game playing
win = False

# First Game List
game_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

while win == False: 
    
    # Clear any historical output and show the board
    clear_output()
    display_game(game_list)
    
    # Have player choose position
    position = position_choice()
    
    # Rewrite that position and update game_list
    game_list = replacement_choice(game_list, position)
    print(game_list)
    
    # Clear Screen and show the updated game list
    clear_output()
    display_game(game_list)
    
    # Ask if you want to keep playing
    win = win_detect(game_list)

print('Congratulations! You have won!')

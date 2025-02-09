import pygame

pygame.init()
running = True
screen = pygame.display.set_mode(300, 300)

while running:
    

def create_game_state(board_size, token_max):
    '''
    this function takes two integers greater than 0, and creates a nim game board consisting of the the rows given by board_size.
    '''
    
    game_board = []
    #TODO: create a game board with token sizes increasing until token max is reached, each new line after that must be the max size, each line must increment one until max_size.
    for i in range(board_size):
        game_board.append(1)
        #loop through the list
        #add a token to each row in board_size
        # [1,1,1,1,1]
        
    for i in range (0, board_size):
        if i < token_max:
            game_board[i] = i + 1 
        elif i >= token_max:
            game_board[i] = token_max
            
    if board_size < 0:
        return []
    return game_board


def is_valid_move(game_state, row, takes):
    '''
    '''
    if  (row.isdigit() == True) and (takes.isdigit() == True):
        row = int(row)
        takes = int(takes)
    else:
        return False
        
    if  (len(game_state) < row) or (row < 1):
        return False
    if (3 < takes) or (takes < 1) or (game_state[row - 1] < takes):
        return False
    
    return True
    


def update(game_state, row, takes):
    '''
    '''
    result = game_state[:]

    result[row] = result[row] - takes 
    return result


def draw_game_state(game_state):
    print('=' * 20)
    count = 1
    for i in range(len(game_state)):
        print(f'{count} ', end='')
        print('#' * game_state[i])
        count += 1
    print('=' * 20)
    

def is_over(game_state):
    count = 0
    for i in range(len(game_state)):
        count += game_state[i]

    if count == 0:
        return True
    else:
        return False


    







if __name__ == '__main__':
    

    state = [5,4,3,4,1,0,0,9,1]
    print("before call")
    draw_game_state(state)
    print("after call")
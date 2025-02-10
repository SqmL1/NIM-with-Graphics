import pygame, sys
from nim_utils import create_game_state, is_over, is_valid_move, draw_game_state, update

board_size = create_game_state(4,4)
pygame.init()
pygame.display.set_caption('Nim With Graphics')

screen_width = 600
screen_height = 600


white = 255, 255, 255
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
framerate_cap = 60

game_board = create_game_state(5,5)


game_piece = pygame.image.load('piece.png').convert()
game_piece.set_colorkey(0,0)
pygame.transform.scale(game_piece, (60, 60))
game_piece_width = game_piece.get_width()
game_piece_height = game_piece.get_height()


piece_spacing = 10

game_board = create_game_state(5,5)
pygame.mouse.set_cursor(*pygame.cursors.diamond)

running = True
while running:
    
    
    clock.tick(framerate_cap)
    screen.fill(white)
    #for i in range(3):
    #    screen.blits([(game_piece, 100,100), (game_piece, (100,100))])
    #    y += 1
    for row, pieces in enumerate(game_board):
        for number_of_pieces in range(pieces):
            x = (screen_width // 2) - (pieces * (game_piece_width + piece_spacing)) // 2 + number_of_pieces * (game_piece_height + piece_spacing)
            y = screen_height // 3 + row * (game_piece_height + piece_spacing) 
            screen.blit((game_piece), ((x), (y)))
    

        
        
        
        


    #screen.blits(((game_piece, (50,200)), (game_piece, (50,100))))

    
    #screen.blits((game_piece), ((x), (y)))


    






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
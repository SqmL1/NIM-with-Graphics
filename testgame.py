import pygame, sys
from nim_utils import create_game_state, is_over, is_valid_move, draw_game_state, update

board_size = create_game_state(4,4)
pygame.init()

white = 255, 255, 255
screen = pygame.display.set_mode((300, 300))

game_piece = pygame.image.load('piece.png').convert()
x = 10
y = 
running = True
while running:
    
    screen.fill(white)
    for i in range(board_size):
        screen.blit((game_piece), (x, 100))
    


    






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
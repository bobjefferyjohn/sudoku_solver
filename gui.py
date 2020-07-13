import pygame, sys
from pygame.locals import *
from gui_objects import Grid, SolveButton, ResetButton
import gui_functions as gf
pygame.init()
pygame.font.init()

# Setting the colours
black = pygame.Color(0, 0, 0)         # Black
white = pygame.Color(255, 255, 255)   # White
grey = pygame.Color(128, 128, 128)   # Grey
red = pygame.Color(255, 0, 0)       # Red

# Setting up the screen
screen = pygame.display.set_mode((600, 650))
FPS = pygame.time.Clock()
FPS.tick(30)
pygame.display.set_caption("Sudoku solver")
def draw_screen(screen):
    screen.fill(white)
    grid.draw(screen)

# Initialising stuff
grid = Grid(600, 600)
solve_button = SolveButton(screen)
reset_button = ResetButton(screen)

while True:
    draw_screen(screen)
    solve_button.draw()
    reset_button.draw()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            gf.mouse_click(grid, reset_button, solve_button)

        if event.type == pygame.KEYDOWN:
            gf.keydown(event, grid, screen)




import pygame
from pygame.locals import *
from gui_objects import Grid, Cube, SolveButton, ResetButton

def mouse_click(grid, reset_button, solve_button):
    pos = pygame.mouse.get_pos()
    grid.clicked(pos)
    if reset_button.rect.collidepoint(pos[0], pos[1]):
        reset_button.clicked(grid)
    if solve_button.rect.collidepoint(pos[0], pos[1]):
        solve_button.clicked(grid)

def keydown(event, grid, screen):
    key = get_key(event)
    if grid.selected:
        if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
            grid.cubes[grid.selected[0]][grid.selected[1]].set_val(0)
        if event.key == pygame.K_DOWN:
            if grid.selected[0] != grid.rows - 1:
                grid.select(grid.selected[0]+1, grid.selected[1])
        if event.key == pygame.K_UP:
            if grid.selected[0] != 0:
                grid.select(grid.selected[0]-1, grid.selected[1])
        if event.key == pygame.K_LEFT:
            if grid.selected[1] != 0:
                grid.select(grid.selected[0], grid.selected[1]-1)
        if event.key == pygame.K_RIGHT:
            if grid.selected[1] != grid.cols - 1:
                grid.select(grid.selected[0], grid.selected[1]+1)
        elif key:
            grid.cubes[grid.selected[0]][grid.selected[1]].set_val(int(key))

def get_key(event):
    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
        return 1
    if event.key == pygame.K_2 or event.key == pygame.K_KP2:
        return 2
    if event.key == pygame.K_3 or event.key == pygame.K_KP3:
        return 3
    if event.key == pygame.K_4 or event.key == pygame.K_KP4:
        return 4
    if event.key == pygame.K_5 or event.key == pygame.K_KP5:
        return 5
    if event.key == pygame.K_6 or event.key == pygame.K_KP6:
        return 6
    if event.key == pygame.K_7 or event.key == pygame.K_KP7:
        return 7
    if event.key == pygame.K_8 or event.key == pygame.K_KP8:
        return 8
    if event.key == pygame.K_9 or event.key == pygame.K_KP9:
        return 9
    else:
        return False
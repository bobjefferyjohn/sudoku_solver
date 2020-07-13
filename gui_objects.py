import pygame
import functions as fn
from pygame.locals import *
from solver import solve
import functions as fn

# Setting the colours
black = pygame.Color(0, 0, 0)         # Black
white = pygame.Color(255, 255, 255)   # White
grey = pygame.Color(128, 128, 128)   # Grey
red = pygame.Color(255, 0, 0)       # Red

class Grid:
    """Simulates a grid for sudoku"""
    def __init__(self, width, height):
        self.rows = 9
        self.cols = 9
        self.width = width
        self.height = height
        self.selected = None
        self.puzzle = [[0]*9]*9
        self.cubes = [[Cube(self.puzzle, row, col, self.width, self.height) for col in range(self.cols)] for row in range(self.rows)]

    def draw(self, screen):
        """Draws the grid"""
        gap = self.width/9
        for i in range(self.rows + 1):
            if i % 3 == 0:
                thickness = 3
            else:
                thickness = 1
            pygame.draw.line(screen, black, (0, i*gap), (self.width, i*gap), thickness)
            pygame.draw.line(screen, black, (i*gap, 0), (i*gap, self.height), thickness)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(screen)

    def select(self, row, col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False
        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clicked(self, pos):
        """Returns the (row, col) clicked"""
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            self.select(int(y), int(x))
        else:
            return None

    def reset(self):
        self.cubes = [[Cube(self.puzzle, row, col, self.width, self.height) for col in range(self.cols)] for row in range(self.rows)]

    def get_sudoku_grid(self):
        self.sudoku_grid = [[cube.value for cube in cubelist] for cubelist in self.cubes]
        return self.sudoku_grid

class Cube:
    """The cubes that are responsible for entering numbers"""
    def __init__(self, puzzle, row, col, width, height):
        self.puzzle = puzzle
        self.row = row
        self.col = col
        self.value = self.puzzle[row][col]
        self.width = width
        self.height = height
        self.selected = False
        self.hand_drawn = True

    def draw(self, screen):
        font = pygame.font.SysFont("arial", 40)
        gap = self.width / 9
        x = self.col*gap
        y = self.row*gap

        if self.value != 0 and self.hand_drawn:
            text = font.render(str(self.value), 1, black)
            screen.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))
        elif self.value != 0 and not self.hand_drawn:
            text = font.render(str(self.value), 1, grey)
            screen.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        if self.selected:
            pygame.draw.rect(screen, red, (x, y, gap, gap), 3)

    def set_val(self, value):
        self.value = value

class SolveButton:
    """Clicking this button solves the sudoku"""
    def __init__(self, screen):
        self.font = pygame.font.SysFont("arial", 30)
        self.text = "Solve!"
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.width = 200
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = 1.5*self.screen_rect.centerx
        self.rect.centery = 625
        self.prep_msg(self.text)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, white, black)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(black, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def clicked(self, grid):
        sudoku_grid = grid.get_sudoku_grid()
        if fn.test_board(sudoku_grid):
            empty_grid = fn.generate_empty_list(sudoku_grid)
            solved_grid = solve(sudoku_grid)
            for i in range(grid.rows):
                for j in range(grid.cols):
                    grid.cubes[i][j].value = solved_grid[i][j]
                    if [i, j] in empty_grid:
                        grid.cubes[i][j].hand_drawn = False

class ResetButton:
    """Clicking this button solves the sudoku"""
    def __init__(self, screen):
        self.font = pygame.font.SysFont("arial", 30)
        self.text = "Reset"
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.width = 200
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = 0.5*self.screen_rect.centerx
        self.rect.centery = 625

        self.prep_msg(self.text)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, white, black)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(black, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def clicked(self, grid):
        grid.reset()

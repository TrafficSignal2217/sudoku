import pygame



class Board_Render:
    '''
    The board is just an abstract 2D list of numbers. Board_Render renders the board to the screen with a grid of lines and numbers inbetween.

	Parameters:
    self.left - the x position that the left side of the board is rendered at
    self.top - the y position that the top of the board is rendered at
    self.cell_size - the size in pixels of each cell between the lines
    self.line_color - the color of the lines of the grid used to make the sudoku board
    '''
    def __init__(self, left_pos, top_pos, cell_size, line_color):
        self.left = left_pos
        self.top = top_pos
        self.cell_size = cell_size
        self.line_color = line_color


    '''
    This method draws the sudoku board grid lines and numbers in each cell.

	Parameters:
    surface - the pygame surface being drawn to. You dont need to understand this, we will just pass the screen variable in for this argument
    board - the 2D list that contains the numbers of the sudoku board

	Return:
	None
    '''
    def draw(self, surface, board=[]):
        # Draw vertical lines
        for x in range(10):
            # Use thicker line for every third grid line to represent the boxes
            if x % 3 == 0:
                thickness = 3
            else:
                thickness = 1
                
            pygame.draw.line(surface, self.line_color, (self.left + x * self.cell_size, self.top), (self.left + x * self.cell_size, self.top + self.cell_size * 9), thickness)

        # Draw horizontal lines
        for y in range(10):
            # Use thicker line for every third grid line to represent the boxes
            if y % 3 == 0:
                thickness = 3
            else:
                thickness = 1
                
            pygame.draw.line(surface, self.line_color, (self.left, self.top + y * self.cell_size), (self.left + 9 * self.cell_size, self.top + y * self.cell_size), thickness)


        # TODO: Add code in this method to draw the numbers in the board (For debugging purposes, draw zeros for empty cells)


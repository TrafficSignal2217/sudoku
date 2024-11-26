import pygame
import sudoku_generator



class Board:
    '''
    This class represents an entire Sudoku board. A Board object has 81 Cell objects.

	Parameters:
    screen - the pygame window being drawn to. You dont need to understand this, we will just pass the screen variable in for this argument
    difficulty - variable to indicate if the user chose easy medium, or hard.
    '''
    def __init__(self, screen, difficulty):
        self.screen = screen
        self.difficulty = difficulty
        #self.board = sudoku_generator.generate_sudoku()


    '''
    This method draws the sudoku board grid lines and numbers in each cell.

	Parameters:
    left_pos - the x position that the left side of the board is rendered at
    top_pos - the y position that the top of the board is rendered at
    cell_size - the size in pixels of each cell between the lines

	Return:
	None
    '''
    def draw(self, left_pos, top_pos, cell_size):
        # Draw vertical lines
        for x in range(10):
            # Use thicker line for every third grid line to represent the boxes
            if x % 3 == 0:
                thickness = 3
            else:
                thickness = 1
                
            pygame.draw.line(self.screen, "black", (left_pos + x * cell_size, top_pos), (left_pos + x * cell_size, top_pos + cell_size * 9), thickness)

        # Draw horizontal lines
        for y in range(10):
            # Use thicker line for every third grid line to represent the boxes
            if y % 3 == 0:
                thickness = 3
            else:
                thickness = 1
                
            pygame.draw.line(self.screen, "black", (left_pos, top_pos + y * cell_size), (left_pos + 9 * cell_size, top_pos + y * cell_size), thickness)


        # TODO #5: Add code in this method to draw the numbers in the board


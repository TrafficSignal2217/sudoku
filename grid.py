import pygame



class Grid:
    def __init__(self, left_pos, top_pos, box_size, line_color):
        self.left = left_pos
        self.top = top_pos
        self.box_size = box_size
        self.line_color = line_color

    # surface: the screen being rendered to
    def draw(self, surface):
        # Draw vertical lines
        for x in range(10):
            # Use thicker line for every third grid line
            if x % 3 == 0:
                thickness = 3
            else:
                thickness = 1
                
            pygame.draw.line(surface, self.line_color, (self.left + x * self.box_size, self.top), (self.left + x * self.box_size, self.top + self.box_size * 9), thickness)

        # Draw horizontal lines
        for y in range(10):
            # Use thicker line for every third grid line
            if y % 3 == 0:
                thickness = 3
            else:
                thickness = 1
                
            pygame.draw.line(surface, self.line_color, (self.left, self.top + y * self.box_size), (self.left + 9 * self.box_size, self.top + y * self.box_size), thickness)


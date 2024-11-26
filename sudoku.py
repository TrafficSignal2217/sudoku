import pygame
from main_menu import *
from board import Board
from sudoku_generator import *



def main():
    ### pygame setup ###
    pygame.init()
    clock = pygame.time.Clock()

    ### Setup the display ###
    screen_info = pygame.display.Info()  # We will get the user's resolution and use it for the games resolution
    screen_width, screen_height = screen_info.current_w, screen_info.current_h
    screen = pygame.display.set_mode((screen_width, screen_height))

    ### Game Variables ###
    states = {
        "main_menu" : 0,
        "playing" : 1,
        "win" : 2,
        "lose" : 3
    }
    game_state = states["playing"]
    difficulties = {
        "easy" : 0,
        "medium" : 1,
        "hard" : 2,
    }

    ### Load images, fonts, and everything else that will be rendered ###
    fonts = {
        "header":pygame.font.Font(None, 80),  # None font is freesansbold, the default pygame font
        "subheader":pygame.font.Font(None, 70),
        "body":pygame.font.Font(None, 50),
    }
    main_menu_backdrop = pygame.image.load('project_image.png')
    background_color = "blanchedalmond"
    # For now, create a board to start with. Later we will delete this line because the board will be generated once the player selects the difficulty
    board = Board(screen, difficulties["easy"])


    running = True
    while running:
        ### poll for events ###
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Press escape to exit the game
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                running = False


        ### Render the game ###
        if game_state == states["main_menu"]:
            main_menu(screen, screen_width, screen_height, main_menu_backdrop, fonts)
        elif game_state == states["playing"]:
            screen.fill(background_color)
            board.draw(left_pos=128, top_pos=96, cell_size=128)
        # TODO #1: Add win game state and screen with play again and exit buttons
        # TODO #2: Add lose game state and screen with play again and exit buttons


        # This draws what was rendered to the screen
        pygame.display.flip()
        # limit FPS to 60
        clock.tick(60)

    pygame.quit()




if __name__ == "__main__":
    main()




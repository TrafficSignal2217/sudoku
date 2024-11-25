import pygame
from Sudoku_start_screen import *
from grid import Grid
from sudoku_generator import *




def main():
    # pygame setup
    pygame.init()
    clock = pygame.time.Clock()

    # Setup the display
    screen_info = pygame.display.Info()
    screen_width, screen_height = screen_info.current_w, screen_info.current_h
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Game Variables
    states = {
        "main_menu" : 0,
        "playing" : 1,
        "win" : 2,
        "lose" : 3
    }
    game_state = states["main_menu"]

    grid = Grid(128, 96, 128, "black")
    backdrop_color = "blanchedalmond"


    running = True
    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Press escape to exit the game
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                running = False


        # Render the game
        if game_state == states["main_menu"]:
            start_screen()
            screen.fill("black")
        elif game_state == states["playing"]:
            screen.fill(backdrop_color)
            grid.draw(screen)


        # This draws what was rendered to the screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    pygame.quit()






if __name__ == "__main__":
    main()

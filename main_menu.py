import pygame

def main_menu(screen, screen_width, screen_height, backdrop, fonts):
    backdrop = pygame.image.load('project_image.png')
    screen.blit(backdrop, (0, 0))

    header_text = "Welcome to Sudoku"
    header_surf = fonts["header"].render(header_text, 1, "black")
    header_rect = header_surf.get_rect(center=(screen_width // 2, 280))
    screen.blit(header_surf, header_rect)

    subheader_text = "Select Game Mode: "
    subheader_surf = fonts["subheader"].render(subheader_text, 1, "black")
    subheader_rect = subheader_surf.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(subheader_surf, subheader_rect)

    pygame.draw.rect(screen, "green", [700, 700, 150, 50])
    pygame.draw.rect(screen, "orange", [900, 700, 150, 50])
    pygame.draw.rect(screen, "red", [1100, 700, 150, 50])
    button1 = "Easy"
    button2 = "Medium"
    button3 = "Hard"
    button1_surf = fonts["body"].render(button1, 1, "white")
    button2_surf = fonts["body"].render(button2, 1, "white")
    button3_surf = fonts["body"].render(button3, 1, "white")
    button1_rect = button1_surf.get_rect(center=(775, 725))
    button2_rect = button2_surf.get_rect(center=(975, 725))
    button3_rect = button3_surf.get_rect(center=(1175, 725))
    screen.blit(button1_surf, button1_rect)
    screen.blit(button2_surf, button2_rect)
    screen.blit(button3_surf, button3_rect)
    
    # TODO #4: Add clickable buttons with the Button class

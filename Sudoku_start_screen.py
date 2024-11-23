import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
def start_screen():
    start_image = pygame.image.load('project_image.png')
    start_font = pygame.font.Font(None, 80)
    screen.blit(start_image, (0, 0))
    start_text = "Welcome to Sudoku"
    start_surf = start_font.render(start_text, 1, "black")
    start_rect = start_surf.get_rect(center=(1920 // 2, 280))
    screen.blit(start_surf, start_rect)
    start2_font = pygame.font.Font(None, 70)
    start2_text = "Select Game Mode: "
    start2_surf = start2_font.render(start2_text, 1, "black")
    start2_rect = start2_surf.get_rect(center=(1920 // 2, 1080 // 2))
    screen.blit(start2_surf, start2_rect)
    pygame.draw.rect(screen, "orange", [700, 700, 150, 50])
    pygame.draw.rect(screen, "orange", [900, 700, 150, 50])
    pygame.draw.rect(screen, "orange", [1100, 700, 150, 50])
    button_font = pygame.font.Font(None, 50)
    button1 = "Easy"
    button2 = "Medium"
    button3 = "Hard"
    button1_surf = button_font.render(button1, 1, "white")
    button2_surf = button_font.render(button2, 1, "white")
    button3_surf = button_font.render(button3, 1, "white")
    button1_rect = button1_surf.get_rect(center=(775, 725))
    button2_rect = button2_surf.get_rect(center=(975, 725))
    button3_rect = button3_surf.get_rect(center=(1175, 725))
    screen.blit(button1_surf, button1_rect)
    screen.blit(button2_surf, button2_rect)
    screen.blit(button3_surf, button3_rect)

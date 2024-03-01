import sys
import pygame
import random

def show_popup(points):
    popup_width = 400
    popup_height = 150
    popup_color = (250, 178, 133)
    popup_x = (screen_width - popup_width) // 2
    popup_y = (screen_height - popup_height) // 2

    font = pygame.font.Font(None, 36)
    message = "Game over! Your score is: " + str(points)
    text = font.render(message, True, (255, 255, 255))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(screen_color)

        pygame.draw.rect(screen, popup_color, (popup_x, popup_y, popup_width, popup_height))

        text_rect = text.get_rect(center=(popup_x + popup_width // 2, popup_y + popup_height // 2))
        screen.blit(text, text_rect)

        pygame.display.flip()


pygame.init()
screen_width = 500
screen_height = 500
size = (width, height) = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
screen_color = (135, 206, 250)
pygame.display.set_caption('Snow is falling')

snowflake = pygame.image.load('snowflake.png')
delay_time = 1000  # 1000 ms = 1 second

clock = pygame.time.Clock()
snowflakes = []
last_snowflake_time = pygame.time.get_ticks()
points = 0
accelerator = 0.5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            for idx, (x, y) in enumerate(snowflakes):
                if x <= mouse_x <= x + snowflake.get_width() and y <= mouse_y <= y + snowflake.get_height():
                    points += 1
                    del snowflakes[idx]
                    
                    if points % 10 == 0:
                        accelerator += 0.5

                    if points % 10 == 0 and y >= screen_height - 50:
                        show_popup(points)

                    break

    current_time = pygame.time.get_ticks()

    if current_time - last_snowflake_time > 500:
        x_position = random.randint(0, screen_width - 50)
        y_position = -50
        snowflakes.append((x_position, y_position))
        last_snowflake_time = current_time

    screen.fill(screen_color)

    for idx, (x, y) in enumerate(snowflakes):
        y += accelerator
        if y >= screen_height - 50:
            show_popup(points)
        snowflakes[idx] = (x, y)
        screen.blit(snowflake, (x, y))
        

    snowflakes = [(x, y) for x, y in snowflakes if y < screen_height]
    print("Number of snowflakes on screen: ", len(snowflakes))

    click = pygame.mouse.get_pos()

    pygame.display.flip()

    clock.tick(30)
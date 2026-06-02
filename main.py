import pygame

pygame.init()

# init screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frostforge")

# rectangle
rect_x = 100
rect_y = 100
rect_width = 50
rect_height = 50

running = True
while running:
    # process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # process key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: # W
        rect_y -= 5
    if keys[pygame.K_s]: # S
        rect_y += 5
    if keys[pygame.K_a]: # A
        rect_x -= 5
    if keys[pygame.K_d]: # D
        rect_x += 5


    # background
    screen.fill((20, 20, 20))

    # draw rect
    pygame.draw.rect(
        screen,
        (128, 0, 255), # purple
        (rect_x, rect_y, rect_width, rect_height)
    )

    pygame.display.flip()

pygame.quit()
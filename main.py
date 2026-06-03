import pygame

# CLASSES

# Asset -- image, drawing, etc
# class Asset: -- BACKBURNER FOR NOW

# GameObject -- anything that renders into play
class GameObject:
    def __init__(self, x=0, y=0, assetType=None, image=None, shape="rect", dimensions=(0,0), color=(0,0,0)):
        self.x = x
        self.y = y
        self.assetType = assetType
        self.image = image
        self.shape = shape
        self.dimensions = dimensions
        self.color = color
    
    def render(self):
        if self.assetType == None:
            return
        if self.assetType == "shape": # ADD MORE SHAPES AS NEEDED
            if self.shape == "rect":
                pygame.draw.rect(screen, self.color, (self.x, self.y, *self.dimensions))
            if self.shape == "circle":
                pygame.draw.circle(screen, self.color, (self.x, self.y), self.dimensions[0])
        
        # add here render image, or draw picture
                
pygame.init()

# init screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frostforge")

# rectangle
player = GameObject(x=100, y=100, assetType="shape", dimensions=(50,50))

running = True
while running:
    # process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # process key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: # W
        player.y -= 5
    if keys[pygame.K_s]: # S
        player.y += 5
    if keys[pygame.K_a]: # A
        player.x -= 5
    if keys[pygame.K_d]: # D
        player.x += 5


    # background
    screen.fill((20, 20, 20))

    # draw rect
    player.render()

    pygame.display.flip()

pygame.quit()
import pygame

# CLASSES

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

class Template:
    def __init__(self, assetType=None, image=None, shape="rect", size=100, color=(0,0,0)):
        self.assetType = assetType
        self.image = image
        self.shape = shape
        self.size = size
        self.color = color
                
pygame.init()

# AESTHETICS

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GRAY = (20, 20, 20)
GRAY = (35, 35, 35)
PURPLE = (128, 0, 128)
ICE_BLUE = (100, 200, 255)
FROST_BLUE = (150, 220, 255)
ARCANE_PURPLE = (140, 60, 255)

# Fonts
body = pygame.font.SysFont(None, 30)
title = pygame.font.SysFont(None, 40)

# Text
# COMING SOON

# LAYOUT SECTIONS

# Screen -- 1920x1080, 1280x720... make it scalable?
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # pygame.RESIZABLE
pygame.display.set_caption("Frostforge")
BORDER = HEIGHT // 36

# Visual (Space for Grid)
VISUAL_BORDER_SIZE = BORDER // 5
VISUAL_DIM = (HEIGHT * 5 // 6) + 2 * VISUAL_BORDER_SIZE
VISUAL_BACKGROUND_COLOR = WHITE
VISUAL_BORDER_COLOR = BLACK
VISUAL_X = WIDTH - VISUAL_DIM - BORDER # 650 from border
VISUAL_Y = HEIGHT - VISUAL_DIM - BORDER # 650 from border

# Grid
GRID_SIZE = 10
CELL_SIZE = (VISUAL_DIM - 2 * VISUAL_BORDER_SIZE) // GRID_SIZE
CELL_BORDER_SIZE = 1
CELL_COLOR = PURPLE
CELLS = []

for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        CELLS.append(pygame.Rect(VISUAL_X + VISUAL_BORDER_SIZE + CELL_SIZE * col, VISUAL_Y + VISUAL_BORDER_SIZE + CELL_SIZE * row, CELL_SIZE, CELL_SIZE))

# Left Panel(s)
LEFT_PANEL_X = BORDER
LEFT_PANEL_Y = BORDER
LEFT_PANEL_WIDTH = VISUAL_X - LEFT_PANEL_X - BORDER
LEFT_PANEL_HEIGHT = HEIGHT - 2 * BORDER
LEFT_PANEL = pygame.Rect(LEFT_PANEL_X, LEFT_PANEL_Y, LEFT_PANEL_WIDTH, LEFT_PANEL_HEIGHT)

# Grid Buttons
BUTTON_HEIGHT = (VISUAL_Y - BORDER) // 2

# OBJECTS

GameObjects = []
player = GameObject(x=100, y=100, assetType="shape", dimensions=(50,50))
GameObjects.append(player)

# LOGIC

# Grid Logic
GRID = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Cell Selection
SELECTED = None # (X, Y)

running = True
while running:
    # process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
            # if mouse is within visual
            if MOUSE_X >= VISUAL_X + VISUAL_BORDER_SIZE and MOUSE_X <= VISUAL_X + VISUAL_DIM - VISUAL_BORDER_SIZE and MOUSE_Y >= VISUAL_Y + VISUAL_BORDER_SIZE and MOUSE_Y <= VISUAL_Y + VISUAL_DIM - VISUAL_BORDER_SIZE:
                SELECTED = ((MOUSE_X - VISUAL_X - VISUAL_BORDER_SIZE) // CELL_SIZE, (MOUSE_Y - VISUAL_Y - VISUAL_BORDER_SIZE) // 60) # SELECTED = Cell (X, Y) -- X left to right, Y top to bottom

    # process key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: # W
        player.y -= 1
    if keys[pygame.K_s]: # S
        player.y += 1
    if keys[pygame.K_a]: # A
        player.x -= 1
    if keys[pygame.K_d]: # D
        player.x += 1

    # DRAW

    # background
    screen.fill(DARK_GRAY)

    # left panel
    pygame.draw.rect(screen, GRAY, LEFT_PANEL)
    pygame.draw.rect(screen, ARCANE_PURPLE, LEFT_PANEL, 3)

    # buttons
    pygame.draw.rect(screen, ICE_BLUE, (VISUAL_X, BORDER, VISUAL_DIM, BUTTON_HEIGHT))

    # properties


    # visual
    VISUAL = pygame.Rect(VISUAL_X, VISUAL_Y, VISUAL_DIM, VISUAL_DIM)
    pygame.draw.rect(screen, VISUAL_BACKGROUND_COLOR, VISUAL)
    pygame.draw.rect(screen, VISUAL_BORDER_COLOR, VISUAL, VISUAL_BORDER_SIZE)

    # grid
    for c, CELL in enumerate(CELLS):
        X = c % GRID_SIZE
        Y = c // GRID_SIZE
        if SELECTED and SELECTED == (X, Y):
            pygame.draw.rect(screen, ICE_BLUE, CELL, CELL_BORDER_SIZE)
        else:
            pygame.draw.rect(screen, CELL_COLOR, CELL, CELL_BORDER_SIZE)

    # game objects
    for object in GameObjects:
        object.render()

    # TEXT

    # properties
    if SELECTED:
        properties = body.render(f"Cell: {SELECTED}   Template: {GRID[SELECTED[1]][SELECTED[0]]}", True, FROST_BLUE)
        screen.blit(properties, (VISUAL_X + VISUAL_BORDER_SIZE, BORDER + BUTTON_HEIGHT + (BUTTON_HEIGHT + VISUAL_BORDER_SIZE - properties.get_height()) // 2))

    pygame.display.flip()

pygame.quit()
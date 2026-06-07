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

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GRAY = (20, 20, 20)
GRAY = (35, 35, 35)
PURPLE = (128, 0, 128)
ICE_BLUE = (100, 200, 255)
FROST_BLUE = (150, 220, 255)
ARCANE_PURPLE = (140, 60, 255)

# LAYOUT SECTIONS

# Screen -- 1920x1080, 1280x720... make it scalable?
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frostforge")
BORDER = 30

# Visual (Space for Grid)
VISUAL_DIM = 620
VISUAL_BORDER_SIZE = BORDER // 3
VISUAL_BACKGROUND_COLOR = WHITE
VISUAL_BORDER_COLOR = BLACK
VISUAL_X = 630 # 650 from border
VISUAL_Y = 70 # 650 from border

# Grid
GRID_SIZE = 10
CELL_SIZE = 600 // 10 # THE FIRST BOX IS LINE_WIDTH PIXELS BIGGER BECAUSE THE LINE ISN'T DRAWN INTRUDING INTO COLUMN 1 -- IDEA: MAKE LIST OF CELLS AS RECTS, DRAW EACH CELL, AND DRAW A 1PX BORDER IN THE CELL IT OWNS ITS OWN SPACE, WILL DRAW ALONG BORDER BUT OK
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
PANEL_GAP = BORDER // 2
TOP_PANEL_HEIGHT = int(LEFT_PANEL_HEIGHT * 0.3)
MIDDLE_PANEL_HEIGHT = int(LEFT_PANEL_HEIGHT * 0.4)
BOTTOM_PANEL_HIEGHT = LEFT_PANEL_HEIGHT - TOP_PANEL_HEIGHT - MIDDLE_PANEL_HEIGHT - 2 * PANEL_GAP

# Future Training Section --> Left Panel: Top
TOP_RECT = pygame.Rect(LEFT_PANEL_X, LEFT_PANEL_Y, LEFT_PANEL_WIDTH, TOP_PANEL_HEIGHT)

# Future Template Section --> Left Panel: Middle
MIDDLE_Y = LEFT_PANEL_Y + PANEL_GAP + TOP_PANEL_HEIGHT
MIDDLE_RECT = pygame.Rect(LEFT_PANEL_X, MIDDLE_Y, LEFT_PANEL_WIDTH, MIDDLE_PANEL_HEIGHT)

# Properties --> Left Panel: Bottom
BOTTOM_Y = MIDDLE_Y + PANEL_GAP + MIDDLE_PANEL_HEIGHT
BOTTOM_RECT = pygame.Rect(LEFT_PANEL_X, BOTTOM_Y, LEFT_PANEL_WIDTH, BOTTOM_PANEL_HIEGHT)

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
                print(SELECTED)

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

    # left panel top
    pygame.draw.rect(screen, GRAY, TOP_RECT)
    pygame.draw.rect(screen, PURPLE, TOP_RECT, 3)

    # left panel middle
    pygame.draw.rect(screen, GRAY, MIDDLE_RECT)
    pygame.draw.rect(screen, PURPLE, MIDDLE_RECT, 3)

    # left panel bottom
    pygame.draw.rect(screen, GRAY, BOTTOM_RECT)
    pygame.draw.rect(screen, PURPLE, BOTTOM_RECT, 3)

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

    pygame.display.flip()

pygame.quit()
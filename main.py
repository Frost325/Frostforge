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
GRAY = (20, 20, 20)
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

# Visual
VISUAL_DIM = 620
VISUAL_BORDER_SIZE = 10
VISUAL_BACKGROUND_COLOR = WHITE
VISUAL_BORDER_COLOR = BLACK
VISUAL_X = 630 # 550 from border
VISUAL_Y = 70 # 550 from border

# Grid
GRID_SIZE = 10
CELL_SIZE = 600 // 10 # THE FIRST BOX IS LINE_WIDTH PIXELS BIGGER BECAUSE THE LINE ISN'T DRAWN INTRUDING INTO COLUMN 1 -- IDEA: MAKE LIST OF CELLS AS RECTS, DRAW EACH CELL, AND DRAW A 1PX BORDER IN THE CELL IT OWNS ITS OWN SPACE, WILL DRAW ALONG BORDER BUT OK
CELL_BORDER_SIZE = 1
CELL_COLOR = PURPLE
CELLS = []

for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        CELLS.append(pygame.Rect(VISUAL_X + VISUAL_BORDER_SIZE + CELL_SIZE * col, VISUAL_Y + VISUAL_BORDER_SIZE + CELL_SIZE * row, CELL_SIZE, CELL_SIZE))

# objects
GameObjects = []
player = GameObject(x=100, y=100, assetType="shape", dimensions=(50,50))
GameObjects.append(player)

# LOGIC

# Grid Logic
GRID = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
print(GRID)

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
    screen.fill(GRAY)

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
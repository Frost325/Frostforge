import pygame
from backend.colors import *
from backend.objects import GameObject, Template
from backend.ui import Button, Dropdown, Page
from backend.TemplatePage import TemplatesPage
from backend.save import save, load

pygame.init()

# AESTHETICS

# Fonts
body = pygame.font.SysFont(None, 30)
title = pygame.font.SysFont(None, 40)

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
LEFT_PANEL_BORDER = BORDER // 10

# Grid Editing Buttons
BUTTONS = 5
BUTTON_HEIGHT = (VISUAL_Y - BORDER) // 2
BUTTON_WIDTH = VISUAL_DIM // BUTTONS
PLACE = Button(VISUAL_X, BORDER, BUTTON_WIDTH, BUTTON_HEIGHT, "Place", ICE_BLUE, FROST_BLUE)
DELETE = Button(VISUAL_X + BUTTON_WIDTH, BORDER, BUTTON_WIDTH, BUTTON_HEIGHT, "Delete", ICE_BLUE, FROST_BLUE)
SAVE = Button(VISUAL_X + 2 * BUTTON_WIDTH, BORDER, BUTTON_WIDTH, BUTTON_HEIGHT, "Save", ICE_BLUE, FROST_BLUE)
LOAD = Button(VISUAL_X + 3 * BUTTON_WIDTH, BORDER, BUTTON_WIDTH, BUTTON_HEIGHT, "Load", ICE_BLUE, FROST_BLUE)
EXPORT = Button(VISUAL_X + 4 * BUTTON_WIDTH, BORDER, BUTTON_WIDTH, BUTTON_HEIGHT, "Export", ICE_BLUE, FROST_BLUE)

# Left Panel Tabs
TABS = 3
TAB_Y = LEFT_PANEL_Y + LEFT_PANEL_BORDER
TAB_WIDTH = (LEFT_PANEL_WIDTH - 2 * LEFT_PANEL_BORDER) // TABS
TAB_HEIGHT = BUTTON_HEIGHT - 2 * LEFT_PANEL_BORDER
TAB_UNDERLINE = pygame.Rect(LEFT_PANEL_X, LEFT_PANEL_Y + BUTTON_HEIGHT - LEFT_PANEL_BORDER, LEFT_PANEL_WIDTH, LEFT_PANEL_BORDER)
TEMPLATE_TAB = Button(LEFT_PANEL_X + LEFT_PANEL_BORDER, TAB_Y, TAB_WIDTH, TAB_HEIGHT, "Templates", ICE_BLUE, FROST_BLUE)
EMPTY_TAB = Button(TEMPLATE_TAB.x + TAB_WIDTH, TAB_Y, TAB_WIDTH, TAB_HEIGHT, "EMPTY", ICE_BLUE, FROST_BLUE) # CHANGE THIS
SETTINGS_TAB = Button(EMPTY_TAB.x + TAB_WIDTH, TAB_Y, TAB_WIDTH, TAB_HEIGHT, "Settings", ICE_BLUE, FROST_BLUE)

# LOGIC

# Grid Logic
GRID = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Cell Selection
SELECTED = None # (X, Y)

# Templates
TEMPLATES = {}
SELECTED_TEMPLATE = "Blank" # current selected template for placing

# Blank/Default Template
TEMPLATES["Blank"] = Template("Blank")
TEMPLATES["Wall"] = Template("Wall", color=PURPLE)

# Pages
PAGE_X = BORDER + LEFT_PANEL_BORDER
PAGE_Y = LEFT_PANEL_Y + BUTTON_HEIGHT # Button Height = Tab Height + Left Panel Border
PAGE_WIDTH = LEFT_PANEL_WIDTH - 2 * LEFT_PANEL_BORDER
PAGE_HEIGHT = LEFT_PANEL_HEIGHT - LEFT_PANEL_BORDER - BUTTON_HEIGHT # Button Height = Tab Height + Left Panel Border
PAGE_BOX = pygame.Rect(PAGE_X, PAGE_Y, PAGE_WIDTH, PAGE_HEIGHT)
PAGES = {}
PAGES["Templates"] = TemplatesPage(PAGE_X, PAGE_Y , PAGE_WIDTH, PAGE_HEIGHT, body, title, BORDER, TEMPLATES)
PAGES["EMPTY"] = Page(PAGE_X, PAGE_Y , PAGE_WIDTH, PAGE_HEIGHT, body, title, BORDER)
PAGES["Settings"] = Page(PAGE_X, PAGE_Y, PAGE_WIDTH, PAGE_HEIGHT, body, title, BORDER)
CURRENT_PAGE = "Templates"

running = True
while running:
    # process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # mouse clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()

            # if mouse is within visual, update selected
            if MOUSE_X >= VISUAL_X + VISUAL_BORDER_SIZE and MOUSE_X <= VISUAL_X + VISUAL_DIM - VISUAL_BORDER_SIZE and MOUSE_Y >= VISUAL_Y + VISUAL_BORDER_SIZE and MOUSE_Y <= VISUAL_Y + VISUAL_DIM - VISUAL_BORDER_SIZE:
                NEW_SELECTED = ((MOUSE_X - VISUAL_X - VISUAL_BORDER_SIZE) // CELL_SIZE, (MOUSE_Y - VISUAL_Y - VISUAL_BORDER_SIZE) // CELL_SIZE) # SELECTED = Cell (X, Y) -- X left to right, Y top to bottom
                if NEW_SELECTED[0] >= GRID_SIZE or NEW_SELECTED[0] < 0 or NEW_SELECTED[1] >= GRID_SIZE or NEW_SELECTED[1] < 0:
                    SELECTED = None
                elif SELECTED and NEW_SELECTED == SELECTED:
                    SELECTED = None
                else:
                    SELECTED = NEW_SELECTED
            
            # if a tile is selected, check for button clicks
            if SELECTED:
                x, y = SELECTED

                # place blank button clicked
                if PLACE.is_clicked(event.pos):
                    GRID[y][x] = TEMPLATES[SELECTED_TEMPLATE]
                    SELECTED = None
            
                # place selected button clicked
                if DELETE.is_clicked(event.pos):
                    GRID[y][x] = None
                    SELECTED = None
            
            # save/load
            if SAVE.is_clicked(event.pos):
                save(GRID, TEMPLATES, SELECTED_TEMPLATE)
            if LOAD.is_clicked(event.pos):
                GRID, TEMPLATES, SELECTED_TEMPLATE = load()
                PAGES["Templates"].load(TEMPLATES, SELECTED_TEMPLATE)

            # export - COMING SOON
            if EXPORT.is_clicked(event.pos):
                pass

            # check for tab click
            if TEMPLATE_TAB.is_clicked(event.pos):
                CURRENT_PAGE = "Templates"
            if EMPTY_TAB.is_clicked(event.pos):
                CURRENT_PAGE = "EMPTY"
            if SETTINGS_TAB.is_clicked(event.pos):
                CURRENT_PAGE = "Settings"
            # more tabs go here ---------------

            # click within page
            # if PAGE_BOX.collidepoint(event.pos):
            if CURRENT_PAGE == "Templates":
                TEMPLATES, SELECTED_TEMPLATE = PAGES[CURRENT_PAGE].handle_click(event.pos, SELECTED_TEMPLATE)
            else:
                PAGES[CURRENT_PAGE].handle_click(event.pos) # add more pages as needed
        
        # key pressed
        if event.type == pygame.KEYDOWN:
            if CURRENT_PAGE == "Templates":
                TEMPLATES, SELECTED_TEMPLATE = PAGES[CURRENT_PAGE].handle_key(event, SELECTED_TEMPLATE)
            else:
                pass

    # process key presses
    keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]: # W
    #     player.y -= 1

    # DRAW

    # background
    screen.fill(DARK_GRAY)

    # left panel
    pygame.draw.rect(screen, GRAY, LEFT_PANEL)
    pygame.draw.rect(screen, ARCANE_PURPLE, LEFT_PANEL, LEFT_PANEL_BORDER)
    pygame.draw.rect(screen, ARCANE_PURPLE, TAB_UNDERLINE)

    # active page
    PAGES[CURRENT_PAGE].render(screen)

    # tabs
    TEMPLATE_TAB.render(screen, body)
    EMPTY_TAB.render(screen, body)
    SETTINGS_TAB.render(screen, body)

    # grid buttons
    PLACE.render(screen, body)
    DELETE.render(screen, body)
    SAVE.render(screen, body)
    LOAD.render(screen, body)
    EXPORT.render(screen, body)

    # visual
    VISUAL = pygame.Rect(VISUAL_X, VISUAL_Y, VISUAL_DIM, VISUAL_DIM)
    pygame.draw.rect(screen, VISUAL_BACKGROUND_COLOR, VISUAL)
    pygame.draw.rect(screen, VISUAL_BORDER_COLOR, VISUAL, VISUAL_BORDER_SIZE)

    # grid
    for c, CELL in enumerate(CELLS):
        X = c % GRID_SIZE
        Y = c // GRID_SIZE
        # draw object template if availible
        template = GRID[Y][X]
        if template:
            template.render(screen, CELL)
        if SELECTED and SELECTED == (X, Y):
            pygame.draw.rect(screen, ICE_BLUE, CELL, CELL_BORDER_SIZE)
        else:
            pygame.draw.rect(screen, CELL_COLOR, CELL, CELL_BORDER_SIZE)

    # TEXT

    # properties
    if SELECTED:
        template = GRID[SELECTED[1]][SELECTED[0]]
        template_name = template.name if template else None
        properties = body.render(f"Cell: {SELECTED}   Template: {template_name}", True, FROST_BLUE)
        screen.blit(properties, (VISUAL_X + VISUAL_BORDER_SIZE, BORDER + BUTTON_HEIGHT + (BUTTON_HEIGHT + VISUAL_BORDER_SIZE - properties.get_height()) // 2))
    
    placing = body.render(f"Placing: {SELECTED_TEMPLATE}", True, FROST_BLUE)
    screen.blit(placing, (LOAD.x + VISUAL_BORDER_SIZE, BORDER + BUTTON_HEIGHT + (BUTTON_HEIGHT + VISUAL_BORDER_SIZE - placing.get_height()) // 2))

    pygame.display.flip()

pygame.quit()
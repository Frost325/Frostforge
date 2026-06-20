import pygame
from backend.ui import Button, Dropdown, Page, Textbox
from backend.objects import Template
from backend.colors import *

class SettingsPage(Page):
    def __init__(self, x, y, width, height, body, title, border):
        super().__init__(x, y, width, height, body, title, border)

        # GRID SETTINGS - width, height, background color, line color, show lines, background image

        self.grid_title = title.render("Grid", True, FROST_BLUE)
        self.button_width = width // 9
        self.button_height = self.button_width // 2

        # size
        self.grid_width = body.render("Width: 10", True, FROST_BLUE)
        self.grid_height = body.render("Height: 10", True, FROST_BLUE)
        self.width_minus = Button(x + border, y + 2 * border + self.grid_title.get_height(), self.button_height, self.button_height, "-", ICE_BLUE, FROST_BLUE)
        self.width_plus = Button(x, y, self.button_height, self.button_height, "-", ICE_BLUE, FROST_BLUE)
        self.height_minus = Button(x, y, self.button_height, self.button_height, "-", ICE_BLUE, FROST_BLUE)
        self.height_plus = Button(x, y, self.button_height, self.button_height, "-", ICE_BLUE, FROST_BLUE)



        # background color
        self.background_color_text = body.render("Background Color:", True, FROST_BLUE)
        self.background_red_text = body.render("R:", True, FROST_BLUE)
        self.background_green_text = body.render("G:", True, FROST_BLUE)
        self.background_blue_text = body.render("B:", True, FROST_BLUE)
        self.background_red_box = Textbox(x + 4 * border + self.background_red_text.get_width(), y + 5 * border, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, "0", size_limit=3, num_only=True) # r
        self.background_green_box = Textbox(self.background_red_box.x + self.button_width + 2 * border + self.background_green_text.get_width(), self.background_red_box.y, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, "0", size_limit=3, num_only=True) # g
        self.background_blue_box = Textbox(self.background_green_box.x + self.button_width + 2 * border + self.background_blue_text.get_width(), self.background_red_box.y, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, "0", size_limit=3, num_only=True) # b

        # line color
        self.line_color_text = body.render("Background Color:", True, FROST_BLUE)
        self.line_red_text = body.render("R:", True, FROST_BLUE)
        self.line_green_text = body.render("G:", True, FROST_BLUE)
        self.line_blue_text = body.render("B:", True, FROST_BLUE)
        self.line_red_box = Textbox(x, y, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, "0", size_limit=3, num_only=True) # r
        self.line_green_box = Textbox(x, y, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, "0", size_limit=3, num_only=True) # g
        self.line_blue_box = Textbox(x, y, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, "0", size_limit=3, num_only=True) # b

        # image
        # COMING SOON

        # SHOW GRID LINES - MAKE A CHECK BOX
        # FINISH
    
    def render(self, screen):
        super().render(screen)

        # GRID SETTINGS
        screen.blit(self.grid_title, (self.x + self.border, self.y + self.border))

        # size
        self.width_minus.render(screen, self.body)

        # background color
        screen.blit(self.background_color_text, (self.x + 2 * self.border, self.y + 600)) # FINISH

        screen.blit(self.background_red_text, (self.x + 3 * self.border, self.background_red_box.y + (self.background_red_box.height - self.background_red_text.get_height()) // 2))
        self.background_red_box.render(screen, self.body)
        screen.blit(self.background_green_text, (self.background_red_box.x + self.button_width + self.border, self.background_green_box.y + (self.background_green_box.height - self.background_green_text.get_height()) // 2))
        self.background_green_box.render(screen, self.body)
        screen.blit(self.background_blue_text, (self.background_green_box.x + self.button_width + self.border, self.background_blue_box.y + (self.background_blue_box.height - self.background_blue_text.get_height()) // 2))
        self.background_blue_box.render(screen, self.body)

        # line color


        # image


        # show grid lines


    def handle_click(self, pos):
        return super().handle_click(pos)
    
    def handle_key(self, event):
        return super().handle_key(event)
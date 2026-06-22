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
        self.vertical_gap = border // 2

        # size
        self.width_text = body.render("Width:", True, FROST_BLUE)
        self.height_text = body.render("Height:", True, FROST_BLUE)
        self.grid_width = body.render("10", True, FROST_BLUE)
        self.grid_height = body.render("10", True, FROST_BLUE)
        self.grid_range = body.render("(2 - 20)", True, FROST_BLUE)
        self.width_minus = Button(x + 3 * border + self.height_text.get_width(), y + border + self.grid_title.get_height() + self.vertical_gap, self.button_height, self.button_height, "-", ICE_BLUE, FROST_BLUE)
        self.width_plus = Button(self.width_minus.x + self.button_height + self.grid_width.get_width() + 2 * border, self.width_minus.y, self.button_height, self.button_height, "+", ICE_BLUE, FROST_BLUE)
        self.height_minus = Button(self.width_minus.x, self.width_minus.y + self.button_height + self.vertical_gap, self.button_height, self.button_height, "-", ICE_BLUE, FROST_BLUE)
        self.height_plus = Button(self.width_plus.x, self.height_minus.y, self.button_height, self.button_height, "+", ICE_BLUE, FROST_BLUE)

        # background color
        self.background_color_text = body.render("Background Color:", True, FROST_BLUE)
        self.background_red_text = body.render("R:", True, FROST_BLUE)
        self.background_green_text = body.render("G:", True, FROST_BLUE)
        self.background_blue_text = body.render("B:", True, FROST_BLUE)
        self.background_red_box = Textbox(x + 4 * border + self.background_red_text.get_width(), self.height_minus.y + self.button_height + self.background_color_text.get_height() + 2 * self.vertical_gap, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, "255", size_limit=3, num_only=True) # r
        self.background_green_box = Textbox(self.background_red_box.x + self.button_width + 2 * border + self.background_green_text.get_width(), self.background_red_box.y, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, "255", size_limit=3, num_only=True) # g
        self.background_blue_box = Textbox(self.background_green_box.x + self.button_width + 2 * border + self.background_blue_text.get_width(), self.background_red_box.y, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, "255", size_limit=3, num_only=True) # b

        # line color
        self.line_color_text = body.render("Grid Line Color:", True, FROST_BLUE)
        self.line_red_text = body.render("R:", True, FROST_BLUE)
        self.line_green_text = body.render("G:", True, FROST_BLUE)
        self.line_blue_text = body.render("B:", True, FROST_BLUE)
        self.line_red_box = Textbox(x + 4 * border + self.line_red_text.get_width(), self.background_red_box.y + self.button_height + self.line_color_text.get_height() + 2 * self.vertical_gap, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, "128", size_limit=3, num_only=True) # r
        self.line_green_box = Textbox(self.line_red_box.x + self.button_width + 2 * border + self.line_green_text.get_width(), self.line_red_box.y, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, "0", size_limit=3, num_only=True) # g
        self.line_blue_box = Textbox(self.line_green_box.x + self.button_width + 2 * border + self.line_blue_text.get_width(), self.line_red_box.y, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, "128", size_limit=3, num_only=True) # b

        # image
        self.image_text = body.render("Background Image:", True, FROST_BLUE)
        self.image_button = Button(x + 3 * border + self.image_text.get_width(), self.line_red_box.y + self.button_height + self.vertical_gap, self.button_width, self.button_height, "None", ICE_BLUE, FROST_BLUE)

        # SHOW GRID LINES - MAKE A CHECK BOX
        # FINISH

        # NEXT SECTION

        self.empty = title.render("Coming Soon", True, FROST_BLUE)
    
    def render(self, screen):
        super().render(screen)

        # GRID SETTINGS
        screen.blit(self.grid_title, (self.x + self.border, self.y + self.border))

        # size
        screen.blit(self.width_text, (self.x + 2 * self.border, self.width_minus.y + (self.button_height - self.width_text.get_height()) // 2))
        screen.blit(self.height_text, (self.x + 2 * self.border, self.height_minus.y + (self.button_height - self.height_text.get_height()) // 2))
        screen.blit(self.grid_width, (self.width_minus.x + self.button_height + self.border, self.width_minus.y + (self.button_height - self.grid_width.get_height()) // 2))
        screen.blit(self.grid_height, (self.height_minus.x + self.button_height + self.border, self.height_minus.y + (self.button_height - self.grid_height.get_height()) // 2))
        self.width_minus.render(screen, self.body)
        self.width_plus.render(screen, self.body)
        self.height_minus.render(screen, self.body)
        self.height_plus.render(screen, self.body)
        screen.blit(self.grid_range, (self.width_plus.x + self.button_height + 2 * self.border, self.width_plus.y + (2 * self.button_height + self.vertical_gap - self.grid_range.get_height()) // 2))

        # background color
        screen.blit(self.background_color_text, (self.x + 2 * self.border, self.height_minus.y + self.button_height + self.vertical_gap))
        screen.blit(self.background_red_text, (self.x + 3 * self.border, self.background_red_box.y + (self.background_red_box.height - self.background_red_text.get_height()) // 2))
        self.background_red_box.render(screen, self.body)
        screen.blit(self.background_green_text, (self.background_red_box.x + self.button_width + self.border, self.background_green_box.y + (self.background_green_box.height - self.background_green_text.get_height()) // 2))
        self.background_green_box.render(screen, self.body)
        screen.blit(self.background_blue_text, (self.background_green_box.x + self.button_width + self.border, self.background_blue_box.y + (self.background_blue_box.height - self.background_blue_text.get_height()) // 2))
        self.background_blue_box.render(screen, self.body)

        # line color
        screen.blit(self.line_color_text, (self.x + 2 * self.border, self.background_red_box.y + self.button_height + self.vertical_gap))
        screen.blit(self.line_red_text, (self.x + 3 * self.border, self.line_red_box.y + (self.line_red_box.height - self.line_red_text.get_height()) // 2))
        self.line_red_box.render(screen, self.body)
        screen.blit(self.line_green_text, (self.line_red_box.x + self.button_width + self.border, self.line_green_box.y + (self.line_green_box.height - self.line_green_text.get_height()) // 2))
        self.line_green_box.render(screen, self.body)
        screen.blit(self.line_blue_text, (self.line_green_box.x + self.button_width + self.border, self.line_blue_box.y + (self.line_blue_box.height - self.line_blue_text.get_height()) // 2))
        self.line_blue_box.render(screen, self.body)

        # image
        screen.blit(self.image_text, (self.x + 2 * self.border, self.image_button.y + (self.button_height - self.image_text.get_height()) // 2))
        self.image_button.render(screen, self.body)

        # show grid lines
        # FINISH


    def handle_click(self, pos):
        super().handle_click(pos)




    
    def handle_key(self, event):
        super().handle_key(event)



        
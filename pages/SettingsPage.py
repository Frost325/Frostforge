import pygame
from backend.ui import Button, Dropdown, Page, Textbox, Checkbox
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
        self.gw = 10
        self.gh = 10
        self.width_text = body.render("Width:", True, FROST_BLUE)
        self.height_text = body.render("Height:", True, FROST_BLUE)
        self.grid_width = body.render(str(self.gw), True, FROST_BLUE)
        self.grid_height = body.render(str(self.gh), True, FROST_BLUE)
        self.grid_range = body.render("(2 - 20)", True, FROST_BLUE)
        self.width_minus = Button(x + 3 * border + self.height_text.get_width(), y + border + self.grid_title.get_height() + self.vertical_gap, self.button_height, self.button_height, "-", ICE_BLUE, FROST_BLUE)
        self.width_plus = Button(self.width_minus.x + self.button_height + self.grid_width.get_width() + 2 * border, self.width_minus.y, self.button_height, self.button_height, "+", ICE_BLUE, FROST_BLUE)
        self.height_minus = Button(self.width_minus.x, self.width_minus.y + self.button_height + self.vertical_gap, self.button_height, self.button_height, "-", ICE_BLUE, FROST_BLUE)
        self.height_plus = Button(self.width_plus.x, self.height_minus.y, self.button_height, self.button_height, "+", ICE_BLUE, FROST_BLUE)

        # background color
        self.background_color = (255, 255, 255)
        self.background_color_text = body.render("Background Color:", True, FROST_BLUE)
        self.background_red_text = body.render("R:", True, FROST_BLUE)
        self.background_green_text = body.render("G:", True, FROST_BLUE)
        self.background_blue_text = body.render("B:", True, FROST_BLUE)
        self.background_red_box = Textbox(x + 4 * border + self.background_red_text.get_width(), self.height_minus.y + self.button_height + self.background_color_text.get_height() + 2 * self.vertical_gap, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, "255", size_limit=3, num_only=True) # r
        self.background_green_box = Textbox(self.background_red_box.x + self.button_width + 2 * border + self.background_green_text.get_width(), self.background_red_box.y, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, "255", size_limit=3, num_only=True) # g
        self.background_blue_box = Textbox(self.background_green_box.x + self.button_width + 2 * border + self.background_blue_text.get_width(), self.background_red_box.y, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, "255", size_limit=3, num_only=True) # b

        # line color
        self.line_color = (128, 0, 128)
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

        # show grid lines
        self.show_lines_text = body.render("Show Grid Lines:", True, FROST_BLUE)
        self.show_lines = Checkbox(x + 3 * border + self.show_lines_text.get_width(), self.image_button.y + self.button_height + self.vertical_gap, self.button_height, self.button_height, ICE_BLUE, FROST_BLUE)

        # underline
        self.grid_underline = pygame.Rect(x + border, self.show_lines.y + self.button_height + border, width - 2 * border, border // 10)

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
        screen.blit(self.show_lines_text, (self.x + 2 * self.border, self.show_lines.y + (self.button_height - self.show_lines_text.get_height()) // 2))
        self.show_lines.render(screen, self.title)

        # grid underline
        pygame.draw.rect(screen, PURPLE, self.grid_underline)

        # NEXT SECTION
        screen.blit(self.empty, (self.x + self.border, self.grid_underline.bottom + self.border))


    def handle_click(self, pos):
        super().handle_click(pos)

        # width
        new_width = None
        if self.width_minus.is_clicked(pos) and self.gw > 2:
            self.gw -= 1
            self.grid_width = self.body.render(str(self.gw), True, FROST_BLUE)
            new_width = self.gw
        if self.width_plus.is_clicked(pos) and self.gw < 20:
            self.gw += 1
            self.grid_width = self.body.render(str(self.gw), True, FROST_BLUE)
            new_width = self.gw

        # height
        new_height = None
        if self.height_minus.is_clicked(pos) and self.gh > 2:
            self.gh -= 1
            self.grid_height = self.body.render(str(self.gh), True, FROST_BLUE)
            new_height = self.gh
        if self.height_plus.is_clicked(pos) and self.gh < 20:
            self.gh += 1
            self.grid_height = self.body.render(str(self.gh), True, FROST_BLUE)
            new_height = self.gh

        # background color
        (r, g, b) = self.background_color
        change = False
        if self.background_red_box.is_clicked(pos): # True means box is inactive
            if self.background_red_box.text != "":
                r = int(self.background_red_box.text)
            change = True
        if self.background_green_box.is_clicked(pos): # True means box is inactive
            if self.background_green_box.text != "":
                g = int(self.background_green_box.text)
            change = True
        if self.background_blue_box.is_clicked(pos): # True means box is inactive
            if self.background_blue_box.text != "":
                b = int(self.background_blue_box.text)
            change = True
        new_background_color = None
        if change:
            self.background_color = (min(r, 255), min(g, 255), min(b, 255))
            new_background_color = self.background_color

        # line color
        (r, g, b) = self.background_color
        change = False
        if self.line_red_box.is_clicked(pos): # True means box is inactive
            if self.line_red_box.text != "":
                r = int(self.line_red_box.text)
            change = True
        if self.line_green_box.is_clicked(pos): # True means box is inactive
            if self.line_green_box.text != "":
                g = int(self.line_green_box.text)
            change = True
        if self.line_blue_box.is_clicked(pos): # True means box is inactive
            if self.line_blue_box.text != "":
                b = int(self.line_blue_box.text)
            change = True
        new_line_color = None
        if change:
            self.line_color = (min(r, 255), min(g, 255), min(b, 255))
            new_line_color = self.line_color

        # show lines checkbox button
        self.show_lines.is_clicked(pos)
        show = self.show_lines.get_state()

        # New Stuff Put Here

        return new_width, new_height, new_background_color, new_line_color, show
    
    def handle_key(self, event):
        super().handle_key(event)

        # background color
        (r, g, b) = self.background_color
        change = False
        if self.background_red_box.key_pressed(event):
            if self.background_red_box.text != "":
                r = int(self.background_red_box.text)
            change = True
        if self.background_green_box.key_pressed(event):
            if self.background_green_box.text != "":
                g = int(self.background_green_box.text)
            change = True
        if self.background_blue_box.key_pressed(event):
            if self.background_blue_box.text != "":
                b = int(self.background_blue_box.text)
            change = True
        new_background_color = None
        if change:
            self.background_color = (min(r, 255), min(g, 255), min(b, 255))
            new_background_color = self.background_color
            self.update()

        # line color
        (r, g, b) = self.line_color
        change = False
        if self.line_red_box.key_pressed(event):
            if self.line_red_box.text != "":
                r = int(self.line_red_box.text)
            change = True
        if self.line_green_box.key_pressed(event):
            if self.line_green_box.text != "":
                g = int(self.line_green_box.text)
            change = True
        if self.line_blue_box.key_pressed(event):
            if self.line_blue_box.text != "":
                b = int(self.line_blue_box.text)
            change = True
        new_line_color = None
        if change:
            self.line_color = (min(r, 255), min(g, 255), min(b, 255))
            new_line_color = self.line_color
            self.update()

        return new_background_color, new_line_color
    
    def handle_scroll(self, scroll_up):
        return super().handle_scroll(scroll_up)

    def update(self):
        self.background_red_box.text = str(self.background_color[0])
        self.background_green_box.text = str(self.background_color[1])
        self.background_blue_box.text = str(self.background_color[2])
        self.line_red_box.text = str(self.line_color[0])
        self.line_green_box.text = str(self.line_color[1])
        self.line_blue_box.text = str(self.line_color[2])
    
    def load(self, grid_width, grid_height, background_color, line_color, show_lines):
        self.gw = grid_width
        self.gh = grid_height
        self.grid_width = self.body.render(str(self.gw), True, FROST_BLUE)
        self.grid_height = self.body.render(str(self.gh), True, FROST_BLUE)
        self.background_color = background_color
        self.line_color = line_color
        self.update()
        self.show_lines.set_state(show_lines)
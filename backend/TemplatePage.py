import pygame
from backend.ui import Button, Dropdown, Page
from backend.objects import Template
from backend.colors import *

class TemplatesPage(Page):
    def __init__(self, x, y, width, height, body, title, border, templates):
        super().__init__(x, y, width, height, body, title, border)

        # left side template selection
        self.list_header = title.render(f"Templates", True, BLACK)
        self.list_gap = self.list_header.get_width() //  8
        self.template_list = pygame.Rect(x, y, self.list_header.get_width() + 2 * self.list_gap, height)
        self.header_underline = pygame.Rect(x, y + self.list_header.get_height() + self.list_gap, self.template_list.width, border // 10)
        self.right_border = pygame.Rect(x + self.template_list.width, y, border // 10, height)
        
        # template buttons
        self.templates = templates
        self.selected_template = "Blank"
        self.template_buttons = []
        self.button_y = self.header_underline.y + self.header_underline.height
        self.button_height = (self.header_underline.y - y) * 3 // 4
        for name in templates.keys():
            button = Button(x, self.button_y, self.template_list.width, self.button_height, name, ICE_BLUE, FROST_BLUE)
            self.template_buttons.append(button)
            self.button_y += self.button_height
        
        # new template button
        self.new_template = Button(x, 2 * y + height - self.header_underline.y, self.template_list.width, self.header_underline.y - y, "New Template", SLATE_GRAY, SILVER)
    
    def render(self, screen):
        super().render(screen)

        # header
        pygame.draw.rect(screen, LESS_DARK_GRAY, self.template_list)
        pygame.draw.rect(screen, SLATE_GRAY, (self.x, self.y, self.template_list.width, self.header_underline.y - self.y))
        screen.blit(self.list_header, (self.x + self.list_gap, self.y + self.list_gap // 2))
        pygame.draw.rect(screen, PURPLE, self.header_underline)
        pygame.draw.rect(screen, PURPLE, self.right_border)

        # template buttons
        for button in self.template_buttons:
            button.render(screen, self.body, self.selected_template == button.text)

        # new template
        self.new_template.render(screen, self.body)

    def handle_click(self, pos, SELECTED_TEMPLATE):
        super().handle_click(pos)

        # check for template button clicks
        for button in self.template_buttons:
            if button.is_clicked(pos):
                SELECTED_TEMPLATE = button.text
                self.selected_template = SELECTED_TEMPLATE

        # create new blank template: "Temp X"
        if self.new_template.is_clicked(pos):
            SELECTED_TEMPLATE = f"Temp {len(self.templates)}"
            self.templates[SELECTED_TEMPLATE] = Template(name=SELECTED_TEMPLATE)
            self.selected_template = SELECTED_TEMPLATE
            # create new button
            button = Button(self.x, self.button_y, self.template_list.width, self.button_height, SELECTED_TEMPLATE, ICE_BLUE, FROST_BLUE)
            self.template_buttons.append(button)
            self.button_y += self.button_height

        return self.templates, SELECTED_TEMPLATE
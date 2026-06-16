import pygame
from backend.ui import Button, Dropdown, Page, Textbox
from backend.objects import Template
from backend.colors import *

class TemplatesPage(Page):
    def __init__(self, x, y, width, height, body, title, border, templates):
        super().__init__(x, y, width, height, body, title, border)

        # TEMPLATE SELECTION

        # list and header
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
        self.new_template_overline = pygame.Rect(x, self.new_template.y - self.header_underline.height, self.template_list.width, self.header_underline.height)

        # TEMPALTE PROPERTIES PANEL --- REPOSITION EVERYTHING ONCE IT ALL EXISTS

        # cords
        self.text_x = self.right_border.x + self.right_border.width + border
        self.text_gap = height // 16
        self.text_y = y + self.text_gap

        # name
        self.properties_title = title.render(f"{self.selected_template} Properties", True, FROST_BLUE) # gap 0
        self.name_text = body.render("Name:", True, FROST_BLUE)
        self.name_box = Textbox(self.text_x + self.name_text.get_width() + border, self.text_y + self.properties_title.get_height() + self.text_gap, self.template_list.width, self.button_height, ICE_BLUE, FROST_BLUE, self.selected_template)

        # image
        self.image_text = body.render("Image:", True, FROST_BLUE)
        self.image_button = Button(self.text_x + self.image_text.get_width() + border, self.name_box.y + self.name_box.height + self.text_gap, self.template_list.width, self.button_height, "None", ICE_BLUE, FROST_BLUE)

        # shapes dropdown
        self.shape_text = body.render("Shape:", True, FROST_BLUE)
        self.shape_drop = Dropdown(self.text_x + self.shape_text.get_width() + border, self.image_button.y + self.image_button.height + self.text_gap, self.template_list.width, self.button_height, ICE_BLUE, FROST_BLUE, ["rect", "circle"], selected=self.templates[self.selected_template].shape)

        # color
        self.color_text = body.render("Color:", True, FROST_BLUE)
        # text box

        # size
        self.size_text = body.render("Size:", True, FROST_BLUE)
        # text box

    
    def render(self, screen):
        super().render(screen)

        # TEMPLATE LIST

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
        pygame.draw.rect(screen, PURPLE, self.new_template_overline)

        # TEMPALTE PROPERTIES
        
        # title and name
        screen.blit(self.properties_title, (self.text_x, self.text_y))
        screen.blit(self.name_text, (self.text_x, self.name_box.y + (self.name_box.height - self.name_text.get_height()) // 2))
        self.name_box.render(screen, self.body)

        # image
        screen.blit(self.image_text, (self.text_x, self.image_button.y + (self.image_button.height - self.image_text.get_height()) // 2))
        self.image_button.render(screen, self.body)

        # shape dropdown
        screen.blit(self.shape_text, (self.text_x, self.shape_drop.y + (self.shape_drop.height - self.shape_text.get_height()) // 2))
        self.shape_drop.render(screen, self.body)

        # color
        screen.blit(self.color_text, (self.text_x, self.text_y + 8 * self.text_gap))
        # text boxes

        # size
        screen.blit(self.size_text, (self.text_x, self.text_y + 9 * self.text_gap))
        # text boxes

    def handle_click(self, pos, SELECTED_TEMPLATE):
        super().handle_click(pos)

        # check for template button clicks
        for button in self.template_buttons:
            if button.is_clicked(pos):
                SELECTED_TEMPLATE = button.text
                self.selected_template = SELECTED_TEMPLATE
                self.update(SELECTED_TEMPLATE)

        # create new blank template: "Blank X"
        if self.new_template.is_clicked(pos) and len(self.templates) < 16: # Eventually support more than 16 !!!
            SELECTED_TEMPLATE = f"Blank {len(self.templates)}"
            self.templates[SELECTED_TEMPLATE] = Template(name=SELECTED_TEMPLATE)
            self.selected_template = SELECTED_TEMPLATE
            # create new button
            button = Button(self.x, self.button_y, self.template_list.width, self.button_height, SELECTED_TEMPLATE, ICE_BLUE, FROST_BLUE)
            self.template_buttons.append(button)
            self.button_y += self.button_height
            self.update(SELECTED_TEMPLATE)
        
        # TEMPALTE PROPERTIES

        # name
        if self.name_box.is_clicked(pos): # if True, means box is inactive, can update template name
            NEW_NAME = self.name_box.text
            self.templates[SELECTED_TEMPLATE].name = NEW_NAME
            self.templates[NEW_NAME] = self.templates.pop(SELECTED_TEMPLATE)
            # update template button
            for button in self.template_buttons:
                if button.text == SELECTED_TEMPLATE:
                    button.text = NEW_NAME
            SELECTED_TEMPLATE = NEW_NAME # FINISH SOME WAY TO UPDATE GRID
            self.selected_template = SELECTED_TEMPLATE

        # random dropdown
        self.templates[self.selected_template].shape = self.shape_drop.is_clicked(pos)

        return self.templates, SELECTED_TEMPLATE #, True -- make this some way of meaning to update the grid tempalte names 
    
    def handle_key(self, event, SELECTED_TEMPLATE):
        # name
        if self.name_box.key_pressed(event): # if True, means box is inactive, can update template name
            NEW_NAME = self.name_box.text
            self.templates[SELECTED_TEMPLATE].name = NEW_NAME
            self.templates[NEW_NAME] = self.templates.pop(SELECTED_TEMPLATE)
            # update template button
            for button in self.template_buttons:
                if button.text == SELECTED_TEMPLATE:
                    button.text = NEW_NAME
            SELECTED_TEMPLATE = NEW_NAME # FINISH SOME WAY TO UPDATE GRID
            self.selected_template = SELECTED_TEMPLATE
        return self.templates, SELECTED_TEMPLATE

    # update properties to show current template
    def update(self, template):
        # FINISH
        self.properties_title = self.title.render(f"{self.templates[template].name} Properties", True, FROST_BLUE)
        self.name_box.text = self.templates[template].name
        self.shape_drop.selected = self.templates[template].shape
import pygame
from backend.ui import Button, Dropdown, Page, Textbox
from backend.objects import Template
from backend.colors import *

class TemplatesPage(Page):
    def __init__(self, x, y, width, height, body, title, border, templates, selected_template="Blank"):
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
        self.selected_template = selected_template
        self.template_buttons = []
        self.button_y = self.header_underline.y + self.header_underline.height
        self.button_width = self.template_list.width
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
        self.name_box = Textbox(self.text_x + self.name_text.get_width() + border, self.text_y + self.properties_title.get_height() + self.text_gap, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, self.selected_template, size_limit=10)

        # image
        self.image_text = body.render("Image:", True, FROST_BLUE)
        self.image_button = Button(self.text_x + self.image_text.get_width() + border, self.name_box.y + self.name_box.height + self.text_gap, self.button_width, self.button_height, "None", ICE_BLUE, FROST_BLUE)

        # shapes dropdown
        self.shape_text = body.render("Shape:", True, FROST_BLUE)
        self.shape_drop = Dropdown(self.text_x + self.shape_text.get_width() + border, self.image_button.y + self.image_button.height + self.text_gap, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, ["rect", "circle"], selected=self.templates[self.selected_template].shape)

        # color
        self.color_text = body.render("Color:", True, FROST_BLUE)
        self.red_text = body.render("R:", True, FROST_BLUE)
        self.green_text = body.render("G:", True, FROST_BLUE)
        self.blue_text = body.render("B:", True, FROST_BLUE)
        self.red_box = Textbox(self.shape_drop.x + self.button_width // 4, self.shape_drop.y + self.shape_drop.height + 1.5 * self.text_gap, self.button_width // 2, self.button_height, ICE_BLUE, FROST_BLUE, str(self.templates[self.selected_template].color[0]), size_limit=3, num_only=True) # r
        self.green_box = Textbox(self.shape_drop.x + self.button_width // 4, self.red_box.y + self.red_box.height + 0.5 * self.text_gap, self.button_width // 2, self.button_height, ICE_BLUE, FROST_BLUE, str(self.templates[self.selected_template].color[1]), size_limit=3, num_only=True) # g
        self.blue_box = Textbox(self.shape_drop.x + self.button_width // 4, self.green_box.y + self.green_box.height + 0.5 * self.text_gap, self.button_width // 2, self.button_height, ICE_BLUE, FROST_BLUE, str(self.templates[self.selected_template].color[2]), size_limit=3, num_only=True) # b

        # size
        self.size_text = body.render("Size:", True, FROST_BLUE)
        self.large_minus = Button(self.shape_drop.x, self.blue_box.y + self.blue_box.height + self.text_gap, self.button_width // 4, self.button_height, "-10", ICE_BLUE, FROST_BLUE)
        self.small_minus = Button(self.large_minus.x + self.large_minus.width + border, self.large_minus.y, self.large_minus.width, self.button_height, "-1", ICE_BLUE, FROST_BLUE)
        self.size_display = body.render("100", True, FROST_BLUE)
        self.small_plus = Button(self.small_minus.x + self.small_minus.width + 2 * border + self.size_display.get_width(), self.large_minus.y, self.large_minus.width, self.button_height, "+1", ICE_BLUE, FROST_BLUE)
        self.large_plus = Button(self.small_plus.x + self.small_plus.width +  border, self.large_minus.y, self.large_minus.width, self.button_height, "+10", ICE_BLUE, FROST_BLUE)

        # sample
        self.dim = self.green_box.height + 0.5 * self.text_gap
        self.sample = pygame.Rect((x + width - self.green_box.x - self.green_box.width - self.dim) // 2 + self.green_box.x + self.green_box.width, self.green_box.y - 0.25 * self.text_gap, self.dim, self.dim)
    
    def render(self, screen):
        super().render(screen)

        # TEMPLATE LIST

        # header
        pygame.draw.rect(screen, LESS_DARK_GRAY, self.template_list)
        pygame.draw.rect(screen, SLATE_GRAY, (self.x, self.y, self.button_width, self.header_underline.y - self.y))
        screen.blit(self.list_header, (self.x + self.list_gap, self.y + self.list_gap // 2))
        pygame.draw.rect(screen, PURPLE, self.header_underline)
        pygame.draw.rect(screen, PURPLE, self.right_border)

        # template buttons
        for button in self.template_buttons:
            button.render(screen, self.body, self.selected_template == button.text)

        # new template
        self.new_template.render(screen, self.body)
        pygame.draw.rect(screen, PURPLE, self.new_template_overline)

        # TEMPLATE PROPERTIES
        
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
        screen.blit(self.color_text, (self.text_x, self.shape_drop.y + self.shape_drop.height + self.text_gap + (self.shape_drop.height - self.shape_text.get_height()) // 2))
        screen.blit(self.red_text, (self.red_box.x - self.red_text.get_width() - self.border, self.red_box.y + (self.red_box.height - self.red_text.get_height()) // 2))
        screen.blit(self.green_text, (self.green_box.x - self.green_text.get_width() - self.border, self.green_box.y + (self.green_box.height - self.green_text.get_height()) // 2))
        screen.blit(self.blue_text, (self.blue_box.x - self.blue_text.get_width() - self.border, self.blue_box.y + (self.blue_box.height - self.blue_text.get_height()) // 2))
        self.red_box.render(screen, self.body)
        self.green_box.render(screen, self.body)
        self.blue_box.render(screen, self.body)

        # size
        screen.blit(self.size_text, (self.text_x, self.small_minus.y + (self.small_minus.height - self.size_display.get_height()) // 2))
        self.large_minus.render(screen, self.body)
        self.small_minus.render(screen, self.body)
        screen.blit(self.size_display, (self.small_minus.x + self.small_minus.width + self.border, self.small_minus.y + (self.small_minus.height - self.size_display.get_height()) // 2))
        self.small_plus.render(screen, self.body)
        self.large_plus.render(screen, self.body)

        # sample
        pygame.draw.rect(screen, BLACK, ((self.x + self.width - self.green_box.x - self.green_box.width - self.dim) // 2 + self.green_box.x + self.green_box.width, self.green_box.y - 0.25 * self.text_gap, self.dim, self.dim), 1)
        new_dim = (self.green_box.height + 0.5 * self.text_gap) * (self.templates[self.selected_template].size / 100)
        self.sample = pygame.Rect((self.x + self.width - self.green_box.x - self.green_box.width - new_dim) // 2 + self.green_box.x + self.green_box.width, self.green_box.y - 0.25 * self.text_gap + (self.dim - new_dim) // 2, new_dim, new_dim)
        match self.templates[self.selected_template].shape:
            case "rect":
                pygame.draw.rect(screen, self.templates[self.selected_template].color, self.sample)
            case "circle":
                pygame.draw.circle(screen, self.templates[self.selected_template].color, self.sample.center, min(self.sample.width, self.sample.height) //2)
            case _:
                pygame.draw.rect(screen, RED, self.sample) # Invalid Shape -- Draw Big Red Box

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
            button = Button(self.x, self.button_y, self.button_width, self.button_height, SELECTED_TEMPLATE, ICE_BLUE, FROST_BLUE)
            self.template_buttons.append(button)
            self.button_y += self.button_height
            self.update(SELECTED_TEMPLATE)
        
        # TEMPLATE PROPERTIES

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
            self.properties_title = self.title.render(f"{self.selected_template} Properties", True, FROST_BLUE)

        # image -- coming soon

        # shape dropdown
        self.templates[self.selected_template].shape = self.shape_drop.is_clicked(pos)

        # color boxes
        (r, g, b) = self.templates[SELECTED_TEMPLATE].color
        change = False
        if self.red_box.is_clicked(pos): # True means box is inactive
            if self.red_box.text != "":
                r = int(self.red_box.text)
            change = True
        if self.green_box.is_clicked(pos): # True means box is inactive
            if self.green_box.text != "":
                g = int(self.green_box.text)
            change = True
        if self.blue_box.is_clicked(pos): # True means box is inactive
            if self.blue_box.text != "":
                b = int(self.blue_box.text)
            change = True
        if change:
            self.templates[SELECTED_TEMPLATE].color = (min(r, 255), min(g, 255), min(b, 255))
            self.update(SELECTED_TEMPLATE)

        # size buttons
        size = self.templates[SELECTED_TEMPLATE].size
        if self.large_minus.is_clicked(pos):
            size -= 10
        if self.small_minus.is_clicked(pos):
            size -= 1
        if self.small_plus.is_clicked(pos):
            size += 1
        if self.large_plus.is_clicked(pos):
            size += 10
        self.templates[SELECTED_TEMPLATE].size = max(10, (min(100, size)))
        self.size_display = self.body.render(str(self.templates[self.selected_template].size), True, FROST_BLUE)

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
            self.properties_title = self.title.render(f"{self.selected_template} Properties", True, FROST_BLUE)
        
        # color
        (r, g, b) = self.templates[SELECTED_TEMPLATE].color
        change = False
        if self.red_box.key_pressed(event):
            if self.red_box.text != "":
                r = int(self.red_box.text)
            change = True
        if self.green_box.key_pressed(event):
            if self.green_box.text != "":
                g = int(self.green_box.text)
            change = True
        if self.blue_box.key_pressed(event):
            if self.blue_box.text != "":
                b = int(self.blue_box.text)
            change = True
        if change:
            self.templates[SELECTED_TEMPLATE].color = (min(r, 255), min(g, 255), min(b, 255))
            self.update(SELECTED_TEMPLATE)

        return self.templates, SELECTED_TEMPLATE

    # update properties to show current template
    def update(self, template):
        # FINISH
        self.properties_title = self.title.render(f"{self.templates[template].name} Properties", True, FROST_BLUE)
        self.name_box.text = self.templates[template].name
        self.shape_drop.selected = self.templates[template].shape
        self.red_box.text = str(self.templates[template].color[0])
        self.green_box.text = str(self.templates[template].color[1])
        self.blue_box.text = str(self.templates[template].color[2])
    
    def load(self, templates, selected_template):
        self.templates = templates
        self.selected_template = selected_template
        self.update(selected_template)

        # template buttons
        self.template_buttons = []
        self.button_y = self.header_underline.y + self.header_underline.height
        for name in templates.keys():
            button = Button(self.x, self.button_y, self.template_list.width, self.button_height, name, ICE_BLUE, FROST_BLUE)
            self.template_buttons.append(button)
            self.button_y += self.button_height

# IMPORTANT NOTE: SHAPE DROPDOWN KIDNA IMPEDES ON RED BOX A LITTLE, AND IF MORE OPTIONS ARE ADDED IT WILL DEFINITLY COVER RED BOX AND NEED TO BE HANDLED SO WHEN OPEN UNDERLYING BOXES ARE COVERED AND NOT CLICKED
import pygame
#define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
OFFWHITE = (245, 245, 245)
GREY = (100, 100, 100)

class Button:
    def __init__(self, text, position, selected, font):
        self.text = text# the text displayed
        self.position = position# the position (x,y) of top left corner of button
        self.selected = selected# if button is selected
        self.surface = font.render(text, False, BLACK)
    
    def toString(self):
        return self.text

    def display(self, destination_surface):
        linecolor = BLACK
        if self.selected == True:
            linecolor = BLUE
        pygame.draw.rect(destination_surface, linecolor, ((self.position[0] - 5, self.position[1]), (self.surface.get_width() + 10, self.surface.get_height())), 2)
        destination_surface.blit(self.surface, self.position) 
    
    def isSelected(self):
        if self.selected == True:
            return True
        else:
            return False
    def checkPoint(self, point):
        x = point[0]
        y = point[1]
        

class Case:
    def __init__(self, case_number, labor, timestamp):
        self.case_number = case_number
        self.labor = labor
        self.timestamp = timestamp
    
    def store_to_json(self):
        tostore = f"[({self.case_number})({self.labor})({self.timestamp})]"
        return tostore

'''
app functions

'''

def initUI(size, font):
    Elements = []
    #initalizes the static UI elements and returns them as list
    submit_button = Button("Submit", ((size[0] / 2), (300)), False, font)
    Elements.append(submit_button)
    new_case_button = Button("New", ((size[0] / 4), (300)), True, font)
    Elements.append(new_case_button)
    #Elements.append(pygame.Surface([size[0] / 2, size[1] / 2]))
    if len(Elements) <= 0:
        return 0
        print("debug: no elements generated")
    else:
        return Elements

def main():
    pygame.init()#init pygame module
    pygame.font.init()#init font modules
    pygame.display.set_caption("New Labor Tracker")#set app window title
    textfont = pygame.font.SysFont('Comic Sans MS', 20)#set font style
    size = (400,400)#set size for screen
    screen = pygame.display.set_mode(size)#init screen
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(GREY)
    running = True
    UIElements = initUI(size, textfont)
    cursorpos = (0,0)
    clicked = False

    #run loop
    while running:
        #get events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cursorpos = pygame.mouse.get_pos()
                clicked = True
        
        #check clicked position for buttons
        for e in UIElements:
            if
        #blitting
        screen.blit(background, (0,0))
        for e in UIElements:
            e.display(screen)
        pygame.display.flip()
        pygame.time.wait(100)

main()

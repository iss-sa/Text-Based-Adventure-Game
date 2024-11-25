import pygame 
import pygame_textinput
from class_Person import Person # own class
import sys

import ctypes  # these lines might have to be commented out (e.g. Linux had issues)
ctypes.windll.user32.SetProcessDPIAware() # to avoid any bugs with the wrong screen size (Windows only solution)

pygame.init()


def get_name():
    """ Function to get the name, age and gender of the player, and store it in the Person class"""

    # screen
    info = pygame.display.Info()
    width = info.current_w 
    height = info.current_h - 30
    background = (223,215,200) # Background color

    # create screen
    screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)

    # screen icon
    icon = pygame.image.load("adventure.png")
    pygame.display.set_icon(icon)

    # Create TextInput-object
    textinput = pygame_textinput.TextInputVisualizer()
    questioning = 0  # to have one question after the other
    correct_answer = False # to check if the answer input was correct
    running = True  # for while loop
    

    while running:

        # screen caption in loop, so that it can be changed later
        pygame.display.set_caption("Before We Start")

        #textinput.value = ""
        answer = textinput.value
        screen.fill(background)

        events = pygame.event.get() # get all events happening on screen

        textinput.update(events)  # put every event into textinput
        screen.blit(textinput.surface, (90, 100))

        

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and correct_answer == True:
                questioning += 1
                textinput.value = ""
                

        text1 = "Before we start the game, please input your name."
        text2 = "Great! Hi {}! Now please enter your age."
        text3 = "Lastly, please input your gender (exactly as they are written here): Woman; Man; Non-conforming"

        # to write texts in a specific font in specific sizes and render them
        new_text1 = pygame.font.SysFont('Gabriola', 45).render(text1, True, "black", background)
        new_text3 = pygame.font.SysFont('Gabriola', 45).render(text3, True, "black", background)

        new_text1_rect = new_text1.get_rect()  # rectangular object for the text surface object
        new_text3_rect = new_text3.get_rect()

        if questioning == 0:
            screen.blit(new_text1, new_text1_rect) # putting text on screen
            if answer != "":
                correct_answer = True # any name is acceptable, except no answer at all
                name = answer
                text2 = text2.format(name)  # text2 has to be done here due to the formatting of the name (which you don't have before)
                new_text2 = pygame.font.SysFont('Gabriola', 45).render(text2, True, "black", background)
                new_text2_rect = new_text2.get_rect()
            
            
        
        if questioning == 1:
            correct_answer = False # correct_answer has to be false again, so that answer given can be checked again
            screen.blit(new_text2, new_text2_rect) # putting text on screen
            if answer.isdigit(): # so that only digits are given
                correct_answer = True
                age = answer
                

        if questioning == 2:
            correct_answer = False
            screen.blit(new_text3, new_text3_rect) # putting text on screen
            # to check that one of the options was taken:
            if answer.upper() == "WOMAN" or answer.upper() == "MAN" or answer.upper() == "NON-CONFORMING": 
                correct_answer = True
                gender = answer

        if questioning == 3:
            user = Person(name, gender, age) # saving all given answers in variable user and with class Person
            return user # return object so that they can be used throghout the whole game

        pygame.display.update()


#get_name()
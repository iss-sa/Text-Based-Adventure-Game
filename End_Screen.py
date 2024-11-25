import pygame, sys
from class_Button import Button
from def_save_stats import save_stats

pygame.init() # initialize pygame module

# get width and hight from screen info
info = pygame.display.Info()
width =  info.current_w 
height = info.current_h - 45
screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
pygame.display.set_caption("End Screen")

background = pygame.image.load("stuff_for_buttons_on_screen/background.png")
background=pygame.transform.scale(background,(width,height))
size = 45


def get_font(size): 
    """function to be able to decide the fontsize"""
    return pygame.font.SysFont('Gabriola', size)

def map(user, item, time_start, time_end):
    """ function for the map screen"""

    while True: 
        # new screen caption to nothing
        pygame.display.set_caption("The Map and Your Updated Character") 

        mouse_pos = pygame.mouse.get_pos() # get mouse position

        # Add one picture, then map on top of that
        bg = pygame.image.load("stuff_for_buttons_on_screen/background_scroll.jpg")
        bg = pygame.transform.scale(bg,(width,height))
        screen.blit(bg, (0,0))

        map = pygame.image.load("stuff_for_buttons_on_screen/map_picture.png")
        map_rect = map.get_rect(center=(width/2 , height/2 ))
        screen.blit(map, map_rect)

        # add resized character on the map
        resized_character = pygame.image.load("avatar_resized.png")
        screen.blit(resized_character, (50, height-220)) 

        # settings for button to back to the end screen 
        map_back = Button(image=None, pos=(width-100, height-100), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Black")
        map_back.changeColor(mouse_pos)
        map_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if map_back.checkForInput(mouse_pos):  # if back button pressed
                    end_screen(user, item, time_start, time_end) # back to end screen

        pygame.display.update()
    
def stats(user, item, time_start, time_end):
    """function for the statistics screen"""

    total_time_played = int(time_end - time_start)
    same_name, average_age, average_time_played, same_item = save_stats(user, total_time_played, item)
    while True:
        # new screen caption to nothing
        pygame.display.set_caption("Your Statistics") 

        mouse_pos = pygame.mouse.get_pos() # get mouse position

        screen.fill("black")
        stat = pygame.image.load("stuff_for_buttons_on_screen/stat_picture.png")
        stat=pygame.transform.scale(stat,(width,height))
        screen.blit(stat, (0, 0))
        screen_rect = screen.get_rect()

        # HERE STATISTICS WOULD GO
        if item == "": # check if item empty
            EndItem1 = "You didn't acquire an item on your journey."
            EndItem1_text = get_font(size).render(EndItem1, True, "White")
            EndItem1_rect = EndItem1_text.get_rect(center=(screen_rect.centerx, 50))
            screen.blit(EndItem1_text, EndItem1_rect)

        else: # if you got an item, it is printed on the screen
            EndItem1 = "You acquired an item on your journey."
            EndItem1_text = get_font(size).render(EndItem1, True, "White")
            EndItem1_rect = EndItem1_text.get_rect(center=(screen_rect.centerx, 50)) 
            screen.blit(EndItem1_text, EndItem1_rect)

            EndItem2 = "You got "+str(item)+" as an item! Congratulations!!!"
            EndItem2_text = get_font(size).render(EndItem2, True, "White")
            EndItem2_rect = EndItem2_text.get_rect(center=(screen_rect.centerx, 150)) 
            screen.blit(EndItem2_text, EndItem2_rect)

            if same_item == 1:
                item_text = "Good Job! You are the only Player who found that item!"
            else: item_text = str(same_item - 1) + "Players have found this item before you."
            item_text_t = get_font(size).render(item_text, True, "White")
            item_text_r = item_text_t.get_rect(center=(screen_rect.centerx, 650))
            screen.blit(item_text_t, item_text_r)

        # print on screen the time played 
        TimePlayed = "You Played for " + str("%.2f" %((total_time_played)/60)) + " minutes."
        TimePlayed_text = get_font(size).render(TimePlayed, True, "White")
        TimePlayed_rect = TimePlayed_text.get_rect(center=(screen_rect.centerx, 250))
        screen.blit(TimePlayed_text, TimePlayed_rect)

        if same_name == 1:
            text_name = "You are the first \"" + user.name + "\" playing this game!"
        else:
            text_name = "There have been " + str(same_name - 1) + " other characters with the same name as you."
        text_name_t = get_font(size).render(text_name, True, "White")
        text_name_r = text_name_t.get_rect(center=(screen_rect.centerx, 300))
        screen.blit(text_name_t, text_name_r)

        average_a = "The average age of all players is: " + str(average_age) + " years"
        average_a_t = get_font(size).render(average_a, True, "White")
        average_a_r = average_a_t.get_rect(center=(screen_rect.centerx, 450))
        screen.blit(average_a_t, average_a_r)

        average_time = "The average time played of all players is: " + str(average_time_played) + " minutes."
        average_time_t = get_font(size).render(average_time, True, "White")
        average_time_r = average_time_t.get_rect(center=(screen_rect.centerx, 500))
        screen.blit(average_time_t, average_time_r)


        # settings for button to back to the end screen
        stats_back = Button(image=None, pos=(width-100, height-100), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Black")
        stats_back.changeColor(mouse_pos)
        stats_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if stats_back.checkForInput(mouse_pos):  # if back button pressed
                    end_screen(user, item, time_start, time_end)  # back to end screen

        pygame.display.update()

def end_screen(user, item="", time_start=0, time_end=0):
    """ function for the end screen"""

    while True:
        screen.blit(background, (0, 0)) # display background

        # new screen caption to nothing
        pygame.display.set_caption("Before You Quit") 

        menu_mouse_pos = pygame.mouse.get_pos() # get mouse position

        # for End Screen text
        es_text = get_font(100).render("END SCREEN", True, "Black")
        es_rect = es_text.get_rect(center=(width/2, 100))

        # settings fo each available button
        map_button = Button(image=pygame.image.load("stuff_for_buttons_on_screen/map_rect.png"), pos=(width/2, 300), 
                            text_input="MAP", font=get_font(75), base_color="Black", hovering_color="White")
        stats_button = Button(image=pygame.image.load("stuff_for_buttons_on_screen/stats_rect.png"), pos=(width/2, 500), 
                            text_input="STATISTICS", font=get_font(75), base_color="Black", hovering_color="White")
        QUIT_button = Button(image=pygame.image.load("stuff_for_buttons_on_screen/quit_rect.png"), pos=(width/2, 700), 
                            text_input="QUIT", font=get_font(75), base_color="Black", hovering_color="White")

        screen.blit(es_text, es_rect) # blt text 

        for button in [map_button, stats_button, QUIT_button]:
            button.changeColor(menu_mouse_pos)  # change color if mouse hovers on any of the buttons
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if map_button.checkForInput(menu_mouse_pos): # if map button clicked
                    map(user, item, time_start, time_end)   # go to map
                if stats_button.checkForInput(menu_mouse_pos):  # if stats button clicked
                    stats(user, item, time_start, time_end)  # go to stats 
                if QUIT_button.checkForInput(menu_mouse_pos):  # if quit button clicked
                    pygame.quit()  # quit loop, exit screen
                    sys.exit()

        pygame.display.update()


import pygame
import sys
from pygame.locals import *
from class_Person import Person # own class
import pygame_textinput
from def_get_name import get_name



pygame.init() # initialize pygame



# for screen
info = pygame.display.Info()
width =  info.current_w 
height = info.current_h - 30
BACKGROUND = (223,215,200)  # Background color

# create screen
screen_created = pygame.display.set_mode((width, height), RESIZABLE)


# Create TextInput-object
textinput = pygame_textinput.TextInputVisualizer()

# for placement of character picture
charX = width/2 - 400
charY = height/2 - 300

# Name, Gender and age of the user
player = Person("", "", 0)

# all the color palettes user can choose from {"Color": RGB_value, ...}
skin_p = {"Dark Brown": (70, 42, 18), "Brown": (98, 59, 25), "Mid Brown": (152, 102, 57), "Light Brown": (163, 118, 79),"Tanned White": (241, 194, 125), "White": (255, 219, 172), "Pinkish": (244, 208, 205)}
eye_p = {"Blue": (46, 83, 111), "Grey Blue": (152, 175, 199), "Brown": (99, 78, 52), "Black Brown": (25, 16, 7), "Green": (61, 103, 29), "Grey Green": (73, 118, 101)}
n_hair_p = {"Blonde": (250, 240, 130), "Dirty Blonde": (223, 195, 147), "Orange": (231, 151, 13), "Ginger": (202, 116, 0), "Light Brown": (137, 85, 57), "Dark Brown": (100, 47, 12), "Black": (10, 5, 0), "Grey": (145, 145, 145), "White": (240, 247, 255) }
u_hair_p = {"Red": (168, 0, 0), "Purple": (155, 70, 170), "Blue": (75, 89, 170), "Green": (109, 165, 44), "Coral": (249, 139, 136), "Pink": (255, 105, 180), "Bright Red": (254, 32, 32)}
cl_neutrals = {"Green": (190, 186, 152), "Grey": (199, 199, 199), "Beige": (196, 177, 160), "Brown": (156, 132, 124), "Blue": (157, 173, 193), "Dirty Pink": (193, 157, 173), "Violet": (177, 157, 193), "Turquoise": (157, 191, 193), "Khaki": (177, 139, 103)}
cl_dark_c = {"Black": (39, 39, 39), "Grey": (82, 84, 86), "Brown": (52, 32, 29), "Blue": (26, 54, 97), "Green": (19, 69, 50), "Red": (111, 0, 0), "Violet": (72, 0, 103), "Turquoise": (29, 96, 108), "Orange": (213, 84, 41)}
cl_light_c = {"Green": (176, 229, 31), "Yellow": (243, 231, 95), "Hot Pink": (243, 68, 182), "Blue": (1, 176, 221), "Bright Red": (245, 1, 0), "Violet": (225, 184, 245), "Turquoise": (133, 209, 188), "Light Orange": (247, 175, 54), "Baby Pink": (234, 166, 179), "Baby Blue": (149, 204, 213)}

# for base character displayed at the beginning
hair_c = n_hair_p["Black"] # Hair color
skin_c = skin_p["Light Brown"] # Skin color
blush = (skin_c[0], skin_c[1] - 34, skin_c[2]) # blushies 
jack_c = cl_dark_c["Black"] # Jacket color
tsirt_c = cl_light_c["Baby Pink"] # T-shirt color
pants_c = cl_neutrals["Grey"] # pants (/skirt) color
shoes_c = cl_dark_c["Brown"] # shoe color
eye_c = eye_p["Black Brown"] # Eye color 
hair_s = "short" # hairstyle (short, long, ponytail)
pants_l = True  # long pants 
pants_s = False # short pants
skirt_l = False # long skirt
skirt_s = False # short skirt
item_name = "" # item empty for now

# All questions and answers listed here
t = ["Hello {}! This is where you generate your character! Press ENTER to continue.", 
    ["Here is your character. What would you like to change? (Please write the corresponding number)", 
        "1) Nothing;  2) Skin Color;  3) Eye Color;  4) Hairstyle;  5) Hair Color;  6) Outfit pieces;  7) Outfit color"], 
    ["Please choose which color you want. (Please write the color exactly as written)", 
        ";  ".join(list(skin_p.keys())), ";  ".join(list(eye_p.keys())), 
        ";  ".join(list(n_hair_p.keys())), ";  ".join(list(u_hair_p.keys())), 
        ";  ".join(list(cl_neutrals.keys())), ";  ".join(list(cl_light_c.keys())), ";  ".join(list(cl_dark_c.keys()))],
    ["Chose which of these you want (Please write the corresponding number)", 
        "1) Natural hair color; 2) Artificial hair color", 
        "1) A ponytail; 2) Short Hair; 3) Long Hair", 
        "1) Long Pants; 2) Short Pants; 3) Long Skirt; 4) Short Skirt; 5) Long Dress; 6) Short Dress",
        "1) Neutral Clothing colors, 2) Light Clothing Colors, 3) Dark clothing colors"],  
    ["Of which piece do you want to change the color? (Please write the corresponding number)", 
        "1) Jacket, 2) T-shirt; 3) Pants/Skirt, 4) Shoes", "1) Jacket 2) Dress, 3) Shoes "],
    ["Wow, {}! You look great! Are you ready for your adventure?", "1) Yes; 2) No"]]


def display_text_character(user, text1, text2, hr, sk, jk, ts, ps, sh, ey, hairstyle, pants_long, pants_short, 
                            skirt_long, skirt_short, item, screen, x, y):

    """ to display the given strings and the generated character on the screen"""
    text_color = (0, 0, 0) # black
    background = (223,215,200) # Background color
    text1 = text1.format(user.name)

    while True:
        screen.fill(background)

        events = pygame.event.get() # get all events happening on screen

        textinput.update(events)  # put every event into textinput
        screen.blit(textinput.surface, (90, 200))

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # after you press enter 
                answer = textinput.value # returns the answer you typed 
                textinput.value = ""
                return answer


        new_text1 = pygame.font.SysFont('Gabriola', 45).render(text1, True, text_color, background)
        new_text2 = pygame.font.SysFont('Gabriola', 45).render(text2, True, text_color, background)

        new_text1_rect = new_text1.get_rect()  # rectangular object for the text surface object
        screen.blit(new_text1, new_text1_rect)
        screen.blit(new_text2, (0, 75)) 

        # generate new character, save the picture, blit picture onto the screen
        pixels = user.build_character(hr, sk, jk, ts, ps, sh, ey, hairstyle, pants_long, pants_short, 
                                        skirt_long, skirt_short, item)
        user.save_character_pic(pixels)
        user.show_avatar_on_screen("avatar.png", screen, x, y)

        pygame.display.update()


def clothing_palette_color_chose(user, text, clothing_neutrals, clothing_light_colors, clothing_dark_colors,
                                     hr, sk, jk, ts, ps, sh, ey, hairstyle, pants_long, pants_short, skirt_long, 
                                        skirt_short, item, screen, charX, charY):

    """ function to make main_char_gen code shorter"""
    # display available choices for the clothing palettes (neutral, dark, light)
    o_palette = display_text_character(user, text[3][0], text[3][4], hr, sk, jk, ts, ps, sh, ey, 
                                        hairstyle, pants_long, pants_short, skirt_long, skirt_short, 
                                            item, screen, charX, charY)
    
    if o_palette == "1": # neutral colors chosen
        o_color = display_text_character(user, text[2][0], text[2][5], hr, sk, jk, ts, ps, sh, ey, 
                                            hairstyle, pants_long, pants_short, skirt_long, skirt_short, 
                                                item, screen, charX, charY)
        try:
            return clothing_neutrals[o_color]
        except:
            return False # if name entered wrongly, False is returned

    elif o_palette == "2": #  light colors chosen
        o_color = display_text_character(user, text[2][0], text[2][6], hr, sk, jk, ts, ps, sh, ey, 
                                            hairstyle, pants_long, pants_short, skirt_long, skirt_short, 
                                                item, screen, charX, charY)
        try: 
            return clothing_light_colors[o_color]
        except:
            return False # if name entered wrongly, False is returned

    elif o_palette == "3": # dark colors chosen
        o_color = display_text_character(user, text[2][0], text[2][7], hr, sk, jk, ts, ps, sh, ey, 
                                            hairstyle, pants_long, pants_short, skirt_long, skirt_short, 
                                                item, screen, charX, charY)
        try:
            return clothing_dark_colors[o_color]
        except:
            return False # if name entered wrongly, False is returned
    
    else:
        return False # if wrong number entered, False is returned


def main_char_gen(user=player, text=t, hr=hair_c, sk=skin_c, jk=jack_c, ts=tsirt_c, ps=pants_c, sh=shoes_c, 
                    ey=eye_c, hairstyle=hair_s, pants_long=pants_l, pants_short=pants_s, skirt_long=skirt_l, 
                        skirt_short=skirt_s, item=item_name, screen=screen_created, skin_palette=skin_p, 
                        eye_palette=eye_p, natural_hair_palette=n_hair_p, unnatural_hair_palette=u_hair_p, 
                            clothing_neutrals=cl_neutrals, clothing_light_colors=cl_light_c, clothing_dark_colors=cl_dark_c):
    
    """ function for the main part of the character generator"""

    running = True  # for game loop
    questioning = 0  # variable to begin the questioning 
    dress = False # initiating variable for dress 


    while running:
        screen.fill(BACKGROUND) # fill background

        # to keep new screen caption
        pygame.display.set_caption("Character Generator") # captions


        if questioning == 0:  # before enter is pressed display this:
            user = get_name() # to get name, age and gender

            # to immeditaley update screen caption and icon
            pygame.display.set_caption("Character Generator") # captions

            display_text_character(user, text[0], '', hr, sk, jk, ts, ps, sh, ey, hairstyle, pants_long, 
                                    pants_short, skirt_long, skirt_short, item, screen, charX, charY)
            questioning = 1


        if questioning == 1: # main questions start 

            # what do you want to change question
            opt_chosen = display_text_character(user, text[1][0], text[1][1], hr, sk, jk, ts, ps, sh, ey, 
                                                hairstyle, pants_long, pants_short, skirt_long, skirt_short, 
                                                    item, screen, charX, charY)

            if opt_chosen == "1": 
                # nothing to change
                end = display_text_character(user, text[5][0], text[5][1], hr, sk, jk, ts, ps, sh, ey, 
                                                hairstyle, pants_long, pants_short, skirt_long, skirt_short, 
                                                    item, screen, charX, charY)

                if end == "1": 
                    # continue to game
                    # return all variables needed later
                    return user 
                      
                
                
            elif opt_chosen == "2":
                # skin color change
                sk_color = display_text_character(user, text[2][0], text[2][1], hr, sk, jk, ts, ps, sh, ey, 
                                                    hairstyle, pants_long, pants_short, skirt_long, skirt_short, 
                                                        item, screen, charX, charY)
                try: 
                    sk = skin_palette[sk_color]
                except:
                    continue # if name entered wrongly, go back to first question (what do you want to change question)


            elif opt_chosen == "3":
                # exe clor to change
                ey_color = display_text_character(user, text[2][0], text[2][2], hr, sk, jk, ts, ps, sh, ey, 
                                                    hairstyle, pants_long, pants_short, skirt_long, skirt_short, 
                                                        item, screen, charX, charY)
                try:
                    ey = eye_palette[ey_color]
                except:
                    continue # if name entered wrongly, go back to first question (what do you want to change question)

            elif opt_chosen == "4":
                #hairstyle to change
                hs_opt = display_text_character(user, text[3][0], text[3][2], hr, sk, jk, ts, ps, sh, ey, 
                                                    hairstyle, pants_long, pants_short, skirt_long, skirt_short, 
                                                        item, screen, charX, charY)

                if hs_opt == "1":
                    hairstyle = "ponytail"
                elif hs_opt == "2":
                    hairstyle = "short"
                elif hs_opt == "3":
                    hairstyle = "long"
            
            elif opt_chosen == "5":
                #haircolor to change
                hs_col_opt = display_text_character(user, text[3][0], text[3][1], hr, sk, jk, ts, ps, sh, ey, 
                                                        hairstyle, pants_long, pants_short, skirt_long, skirt_short, 
                                                            item, screen, charX, charY)
                if hs_col_opt == "1": # natural hair palette chosen
                    hs_color = display_text_character(user, text[2][0], text[2][3], hr, sk, jk, ts, ps, sh, ey, 
                                                        hairstyle, pants_long, pants_short, skirt_long, skirt_short, 
                                                            item, screen, charX, charY)
                    try: 
                        hr = natural_hair_palette[hs_color]
                    except:
                        continue # if name entered wrongly, go back to first question (what do you want to change question)

                elif hs_col_opt == "2": # artificial har palette chosen
                    hs_color = display_text_character(user, text[2][0], text[2][4], hr, sk, jk, ts, ps, sh, ey, 
                                                        hairstyle, pants_long, pants_short, skirt_long, skirt_short, 
                                                            item, screen, charX, charY)
                    try:
                        hr = unnatural_hair_palette[hs_color]
                    except:
                        continue # if name entered wrongly, go back to first question (what do you want to change question)
            
            elif opt_chosen == "6":
                #outfit to change
                o_opt = display_text_character(user, text[3][0], text[3][3], hr, sk, jk, ts, ps, sh, ey, 
                                                hairstyle, pants_long, pants_short, skirt_long, skirt_short, 
                                                    item, screen, charX, charY)

                if o_opt == "1": # long pants = True, everything else False
                    pants_long, pants_short, skirt_long, skirt_short = True, False, False, False
                    dress = False
                elif o_opt == "2": # short pants = True, everything else False
                    pants_long, pants_short, skirt_long, skirt_short = False, True, False, False
                    dress = False
                elif o_opt == "3": # long skirt = True, everything else False
                    pants_long, pants_short, skirt_long, skirt_short = False, False, True, False
                    dress = False
                elif o_opt == "4": # short skirt = True, everything else False
                    pants_long, pants_short, skirt_long, skirt_short = False, False, False, True
                    dress = False
                elif o_opt == "5": # long dress (long_skirt=True)
                    pants_long, pants_short, skirt_long, skirt_short = False, False, True, False
                    ps = ts  # skirt will have same color as tshirt
                    dress = True
                elif o_opt == "6": # short dress (short_skirt=True)
                    pants_long, pants_short, skirt_long, skirt_short = False, False, False, True
                    ps = ts  # skirt will have same color as tshirt
                    dress = True

            elif opt_chosen == "7":
                # outfit color to change
                if dress == True:
                    o_piece = display_text_character(user, text[4][0], text[4][2], hr, sk, jk, ts, ps, sh, ey, 
                                                        hairstyle, pants_long, pants_short, skirt_long, skirt_short, 
                                                            item, screen, charX, charY)
                else:
                    o_piece = display_text_character(user, text[4][0], text[4][1], hr, sk, jk, ts, ps, sh, ey, 
                                                        hairstyle, pants_long, pants_short, skirt_long, skirt_short, 
                                                            item, screen, charX, charY)

                # variable to check if input was correct
                check = clothing_palette_color_chose(user, text, clothing_neutrals, clothing_light_colors, 
                                                        clothing_dark_colors, hr, sk, jk, ts, ps, sh, ey, hairstyle,
                                                             pants_long, pants_short, skirt_long, skirt_short, item, 
                                                                screen, charX, charY) 
                if o_piece == "1": # jacket color to change
                    if not(check == False):
                        jk = check

                elif o_piece == "2": # either dress or tshirt color to change
                    if dress == True:
                        if not(check == False):
                            ts, ps = check, check
                    else:
                        if not(check == False):
                            ts = check

                elif o_piece == "3": # either shoes(dress=True) or pants/skirt to change
                    if dress == True:
                        if not(check == False):
                            sh = check
                    else:
                        if not(check == False):
                            ps = check
                elif o_piece == "4": # either nothing (dress=True) or shows to change
                    if not(check == False):
                        sh = check


#player = main_char_gen()

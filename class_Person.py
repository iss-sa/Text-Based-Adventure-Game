from PIL import Image
import numpy as np
import pygame



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Person:
    """ class to pool all the information from the user: Name, Gender, Age, and then it also saves how the chracter looks.
        It also builds a character with the given input from the character generator, and then saves 2 pictures of the 
        character (in bigger and smaller)
        The last function prints the character on a given pygame screen"""

    def __init__(self, name, gender, age):
        self.name = name
        self. gender = gender
        self.age = age

    def build_character(self, hr, sk, jk, ts, ps, sh, ey, hairstyle, pants_long, pants_short, skirt_long, skirt_short, item=""):
        """ To generate the character you want, by creating a pixel list for the character: 
        hr = hair color (rgb)
        sk = skin color (rgb)
        jk = jacket color (rgb)
        ts = tshirt color (rgb)
        ps = pants color (rgb)
        sh = shoe color (rgb)
        ey = eye color (rgb)
        hairstyle = short, long or ponytail
        pants_long = True or False
        pants_short = True or False
        skirt_long = True or False
        skirt_short = True or False
        item = wizard staff or knifes or medic robe or wizard robe or spear
        """
        self.hr = hr
        self.sk = sk 
        self.jk = jk
        self.ts = ts
        self.ps = ps
        self.sh = sh
        self.ey = ey
        self.hairstyle = hairstyle 
        self.pants_long = pants_long 
        self.pants_short = pants_short
        self.skirt_long = skirt_long
        self.skirt_short = skirt_short
        self.item = item

        bg = (223,215,200) # Background color
        bl = (sk[0], sk[1] - 34, sk[2]) # blushies
        ew = (255,255,255) # Eye white
        bd = (0, 0, 0) # Borders (black)

        avatarB = False # to check if changes has been done to the base character (pixels_list_A)

        # base character: short hair, long pants
        pixels_list_A = [  
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, hr, hr, hr, hr, hr, hr, hr, hr, bd, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bd, bd, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, bd, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bd, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, bd, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bd, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, bd, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bd, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, bd, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bd, hr, hr, hr, hr, hr, hr, hr, sk, sk, sk, sk, sk, hr, hr, hr, bd, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bd, hr, hr, hr, hr, sk, sk, sk, sk, sk, sk, sk, sk, sk, hr, hr, bd, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bd, hr, hr, hr, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, bd, bd, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bd, sk, hr, hr, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, bd, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bd, sk, sk, sk, sk, sk, ew, ey, sk, sk, sk, ew, ey, sk, sk, bd, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bd, sk, sk, sk, sk, ew, ey, sk, sk, sk, ew, ey, sk, sk, bd, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bd, sk, sk, bl, bl, sk, sk, sk, sk, sk, sk, sk, bl, bl, bd, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bd, bd, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, bd, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bd, jk, jk, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bd, jk, jk, jk, jk, jk, jk, ts, ts, ts, jk, jk, bd, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bd, jk, jk, jk, jk, jk, jk, jk, ts, ts, ts, jk, jk, bd, bd, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bd, jk, jk, bd, jk, jk, jk, jk, ts, ts, ts, jk, jk, bd, jk, bd, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bd, sk, sk, bd, jk, jk, jk, jk, ts, ts, ts, jk, jk, bd, sk, bd, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bd, bd, bd, bd, ps, ps, ps, ps, ps, ps, ps, ps, ps, bd, bd, bd, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bd, ps, bd, bd, bd, bd, bd, bd, bd, ps, bd, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bd, ps, bd, bg, bg, bg, bg, bg, bd, ps, bd, bg, bg, bg, bg, bg, bg, bg, bg],        
                [bg, bg, bg, bg, bg, bg, bg, bg, bd, sh, sh, bd, bg, bg, bg, bg, bd, sh, sh, bd, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            ]  


        if hairstyle == "short" and pants_long == True and item == "": # base character: short hair, long pants and no item
            return pixels_list_A
        else:
            pixels_list_B = pixels_list_A  # to record changes
                

        if hairstyle == "long": # changes needed for long hair

            pixels_list_B[2] = [bg, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg]
            pixels_list_B[3] = [bg, bg, bg, bg, bg, bg, bg, bd, bd, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, bd, bg, bg, bg, bg, bg, bg]
            pixels_list_B[4] = [bg, bg, bg, bg, bg, bg, bd, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, bd, bg, bg, bg, bg, bg, bg]
            pixels_list_B[5] = [bg, bg, bg, bg, bg, bg, bd, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, bd, bg, bg, bg, bg, bg]
            pixels_list_B[6] = [bg, bg, bg, bg, bg, bd, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, bd, bg, bg, bg, bg, bg]
            pixels_list_B[7] = [bg, bg, bg, bg, bg, bd, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, sk, hr, hr, bd, bg, bg, bg, bg, bg]
            pixels_list_B[8] = [bg, bg, bg, bg, bg, bd, hr, hr, hr, hr, hr, hr, hr, sk, hr, hr, hr, sk, sk, sk, hr, bd, bg, bg, bg, bg, bg]
            pixels_list_B[9] = [bg, bg, bg, bg, bg, bd, hr, hr, hr, hr, hr, hr, sk, sk, hr, hr, sk, sk, sk, sk, hr, bd, bg, bg, bg, bg, bg]
            pixels_list_B[10] =[bg, bg, bg, bg, bd, hr, hr, hr, hr, hr, hr, hr, sk, hr, hr, sk, sk, sk, sk, sk, bd, bd, bg, bg, bg, bg, bg]
            pixels_list_B[11] =[bg, bg, bg, bg, bd, hr, sk, hr, hr, hr, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, bd, bg, bg, bg, bg, bg, bg]
            pixels_list_B[12] =[bg, bg, bg, bd, hr, hr, sk, hr, hr, hr, sk, ew, ey, sk, sk, sk, ew, ey, sk, sk, bd, bg, bg, bg, bg, bg, bg]
            pixels_list_B[13] =[bg, bd, bd, hr, hr, hr, hr, hr, hr, sk, sk, ew, ey, sk, sk, sk, ew, ey, sk, sk, bd, bg, bg, bg, bg, bg, bg]
            pixels_list_B[14] =[bg, bd, hr, hr, hr, hr, hr, hr, hr, bl, bl, sk, sk, sk, sk, sk, sk, sk, bl, bl, bd, bg, bg, bg, bg, bg, bg]
            pixels_list_B[15] =[bg, bg, bd, bd, hr, hr, hr, bd, bd, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, bd, bg, bg, bg, bg, bg, bg, bg]
            pixels_list_B[16] =[bg, bg, bg, bg, bd, bd, bd, jk, jk, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg]

            avatarB = True


        if hairstyle == "ponytail": #changes needed for ponytail

            pixels_list_B[1] = [bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
            pixels_list_B[2] = [bg, bg, bg, bg, bd, hr, hr, hr, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg]
            pixels_list_B[3] = [bg, bg, bg, bd, hr, hr, hr, hr, bd, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, bd, bg, bg, bg, bg, bg, bg, bg]
            pixels_list_B[4] = [bg, bd, bg, bd, hr, hr, bd, bd, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, bd, bg, bg, bg, bg, bg, bg]
            pixels_list_B[5] = [bd, hr, bd, hr, hr, bd, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, bd, bg, bg, bg, bg, bg]
            pixels_list_B[6] = [bd, hr, hr, hr, hr, bd, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, hr, bd, bg, bg, bg, bg, bg]
            pixels_list_B[7] = [bd, hr, hr, hr, hr, bd, hr, hr, hr, hr, hr, hr, sk, sk, hr, hr, hr, hr, hr, hr, hr, bd, bg, bg, bg, bg, bg]
            pixels_list_B[8] = [bg, bd, hr, hr, hr, bd, hr, hr, hr, hr, hr, sk, sk, sk, hr, hr, hr, hr, hr, hr, hr, bd, bg, bg, bg, bg, bg]
            pixels_list_B[9] = [bg, bg, bd, bd, bd, bd, hr, hr, hr, hr, sk, sk, sk, sk, sk, hr, hr, hr, hr, hr, hr, bd, bg, bg, bg, bg, bg]
            pixels_list_B[10] =[bg, bg, bg, bg, bg, bd, hr, hr, sk, sk, sk, sk, sk, sk, sk, sk, sk, hr, hr, hr, bd, bd, bg, bg, bg, bg, bg]
            pixels_list_B[11] =[bg, bg, bg, bg, bg, bd, sk, hr, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, bd, bg, bg, bg, bg, bg, bg]

            avatarB = True

        if pants_short == True: #changes needed for short pants

            pixels_list_B[22] = [bg, bg, bg, bg, bg, bg, bg, bg, bd, ps, bd, bd, bd, bd, bd, bd, bd, ps, bd, bg, bg, bg, bg, bg, bg, bg, bg]
            pixels_list_B[23] = [bg, bg, bg, bg, bg, bg, bg, bg, bd, sk, bd, bg, bg, bg, bg, bg, bd, sk, bd, bg, bg, bg, bg, bg, bg, bg, bg]        

            avatarB = True


        if skirt_long == True: # changes needed for long skirt

            pixels_list_B[22] = [bg, bg, bg, bg, bg, bg, bg, bg, bd, ps, ps, ps, ps, ps, ps, ps, ps, ps, bd, bg, bg, bg, bg, bg, bg, bg, bg]
            pixels_list_B[23] = [bg, bg, bg, bg, bg, bg, bg, bg, bd, ps, ps, ps, ps, ps, ps, ps, ps, ps, bd, bg, bg, bg, bg, bg, bg, bg, bg]        
            pixels_list_B[24] = [bg, bg, bg, bg, bg, bg, bg, bg, bd, sh, sh, bd, bd, bd, bd, bd, bd, sh, sh, bd, bg, bg, bg, bg, bg, bg, bg]

            avatarB = True

        if skirt_short == True: # changes needed for short skirt

            pixels_list_B[22] = [bg, bg, bg, bg, bg, bg, bg, bg, bd, ps, ps, ps, ps, ps, ps, ps, ps, ps, bd, bg, bg, bg, bg, bg, bg, bg, bg]
            pixels_list_B[23] = [bg, bg, bg, bg, bg, bg, bg, bg, bd, sk, bd, bd, bd, bd, bd, bd, bd, sk, bd, bg, bg, bg, bg, bg, bg, bg, bg]        
            
            avatarB = True


        # changes needed if character has an item (not done yet)
        # items one can get: "wizard's staff", "knifes", "medic's robe", "wizard's robe", "spear"

        if item == "wizard's staff": 
            # colors
            br = (150, 108, 108) # brown for wizard staff
            bs = (125, 212, 202) # brownish for staff
            bu = (115, 255, 241) # blue magic
            db = (153, 241, 227) # dispersed magic
            gr = (138, 255, 189) # green magic
            wh = (200, 254, 242) # bright centre

            # staff
            pixels_list_B[23][19] = br
            pixels_list_B[22][19] = br
            pixels_list_B[22][20] = br
            pixels_list_B[21][20] = br
            pixels_list_B[20][20] = br
            pixels_list_B[20][21] = br
            pixels_list_B[19][21] = br
            pixels_list_B[18][21] = br
            pixels_list_B[18][22] = br
            pixels_list_B[17][22] = br
            pixels_list_B[16][22] = br
            pixels_list_B[15][22] = br
            pixels_list_B[15][23] = br
            # staff
            pixels_list_B[14][23] = bs

            # blue magic
            pixels_list_B[14][24] = bu
            pixels_list_B[13][25] = bu
            pixels_list_B[13][23] = bu
            pixels_list_B[13][21] = bu
            pixels_list_B[12][22] = bu
            pixels_list_B[11][21] = bu
            pixels_list_B[11][25] = bu
            pixels_list_B[10][22] = bu
            pixels_list_B[10][24] = bu
            pixels_list_B[9][23] = bu
            pixels_list_B[8][24] = bu
            # bluish magic
            pixels_list_B[7][23] = db
            pixels_list_B[7][25] = db
            pixels_list_B[8][21] = db
            pixels_list_B[9][21] = db
            pixels_list_B[9][22] = db
            pixels_list_B[9][24] = db
            pixels_list_B[9][25] = db
            pixels_list_B[11][26] = db
            pixels_list_B[13][22] = db
            pixels_list_B[13][26] = db
            pixels_list_B[14][20] = db
            pixels_list_B[15][25] = db
            # green magic
            pixels_list_B[13][24] = gr
            pixels_list_B[12][23] = gr
            pixels_list_B[12][25] = gr
            pixels_list_B[11][24] = gr
            pixels_list_B[11][22] = gr
            pixels_list_B[10][23] = gr
            # white centre
            pixels_list_B[11][23] = wh
            pixels_list_B[12][24] = wh

            avatarB = True


        if item == "knifes":
            # metal part of dagger left
            pixels_list_B[14][7] = (163, 173, 194)
            pixels_list_B[15][7] = (163, 173, 194)
            pixels_list_B[16][7] = (163, 173, 194)
            pixels_list_B[17][7] = (163, 173, 194)
            pixels_list_B[18][7] = (163, 173, 194)
            # metal part of dagger right
            pixels_list_B[14][20] = (163, 173, 194)
            pixels_list_B[15][20] = (163, 173, 194)
            pixels_list_B[16][20] = (163, 173, 194)
            pixels_list_B[17][20] = (163, 173, 194)
            pixels_list_B[18][20] = (163, 173, 194)

            # gold part of dagger left
            pixels_list_B[19][6] = (224, 178, 69)
            pixels_list_B[19][7] = (224, 178, 69)
            pixels_list_B[19][8] = (224, 178, 69)
            # gold part of dagger right
            pixels_list_B[19][19] = (224, 178, 69)
            pixels_list_B[19][20] = (224, 178, 69)
            pixels_list_B[19][21] = (224, 178, 69)

            # brown handle left
            pixels_list_B[20][7] = (211, 97, 60)
            pixels_list_B[21][7] = (211, 97, 60)
            # brown handle right
            pixels_list_B[20][20] = (211, 97, 60)
            pixels_list_B[21][20] = (211, 97, 60)

            avatarB = True
        

        if item == "medic's robe":
            mr = (255, 255, 255) # medic robe 
            rc = (255, 0, 0) # red (medic) cross

            r = -1
            for row in pixels_list_B:
                r += 1
                c = -1
                for color in row:
                    c += 1
                    if color == jk:
                        pixels_list_B[r][c] = mr  # to change all instances of the jacket to the medic robe

        
            pixels_list_B[18][10] = rc
            pixels_list_B[20][10] = rc
            pixels_list_B[19][9] = rc
            pixels_list_B[19][10] = rc
            pixels_list_B[19][11] = rc
            # white robe left (extended jacket)
            pixels_list_B[21][9] = mr
            pixels_list_B[22][9] = mr
            pixels_list_B[23][9] = mr

            pixels_list_B[21][10] = mr
            pixels_list_B[22][10] = mr
            pixels_list_B[23][10] = mr

            pixels_list_B[21][11] = mr
            pixels_list_B[22][11] = mr
            pixels_list_B[23][11] = mr

            pixels_list_B[21][12] = mr
            pixels_list_B[22][12] = mr
            pixels_list_B[23][12] = mr

            #white robe right (extended jacket)
            pixels_list_B[21][16] = mr
            pixels_list_B[22][16] = mr
            pixels_list_B[23][16] = mr

            pixels_list_B[21][17] = mr
            pixels_list_B[22][17] = mr
            pixels_list_B[23][17] = mr

            avatarB = True

        if item == "wizard's robe":
            wr = (66, 65, 134) # blue wizard robe
            st = (251, 183, 82) # yellow stars on robe (individual pixels)  
            ur = (33, 38, 84) # dark blue underrobe
            ps = ur 

            r = -1
            for row in pixels_list_B:
                r += 1
                c = -1
                for color in row:
                    c += 1
                    if color == jk:
                        pixels_list_B[r][c] = wr  # to change all instances of the jacket to the wizard robe
                    elif color == ts:
                        pixels_list_B[r][c] = ur  # t change all instances of the tshirt to the underrobe

            # for a long underrobe
            pixels_list_B[21] = [bg, bg, bg, bg, bg, bd, bd, bd, bd, ps, ps, ps, ps, ps, ps, ps, ps, ps, bd, bd, bd, bg, bg, bg, bg, bg, bg]
            pixels_list_B[22] = [bg, bg, bg, bg, bg, bg, bg, bg, bd, ps, ps, ps, ps, ps, ps, ps, ps, ps, bd, bg, bg, bg, bg, bg, bg, bg, bg]
            pixels_list_B[23] = [bg, bg, bg, bg, bg, bg, bg, bg, bd, ps, ps, ps, ps, ps, ps, ps, ps, ps, bd, bg, bg, bg, bg, bg, bg, bg, bg]        
            pixels_list_B[24] = [bg, bg, bg, bg, bg, bg, bg, bg, bd, sh, sh, bd, bd, bd, bd, bd, bd, sh, sh, bd, bg, bg, bg, bg, bg, bg, bg]
        
            # blue robe left (extended jacket)
            pixels_list_B[21][9] = wr
            pixels_list_B[22][9] = wr
            pixels_list_B[23][9] = wr

            pixels_list_B[21][10] = wr
            pixels_list_B[22][10] = wr
            pixels_list_B[23][10] = wr

            pixels_list_B[21][11] = wr
            pixels_list_B[22][11] = wr
            pixels_list_B[23][11] = wr

            pixels_list_B[21][12] = wr
            pixels_list_B[22][12] = wr
            pixels_list_B[23][12] = wr

            # blue robe right (extended jacket)
            pixels_list_B[21][16] = wr
            pixels_list_B[22][16] = wr
            pixels_list_B[23][16] = wr

            pixels_list_B[21][17] = wr
            pixels_list_B[22][17] = wr
            pixels_list_B[23][17] = wr

            # individual stars
            pixels_list_B[17][8] = st
            pixels_list_B[17][11] = st
            pixels_list_B[18][6] = st
            pixels_list_B[20][9] = st
            pixels_list_B[21][12] = st
            pixels_list_B[23][9] = st
            
            pixels_list_B[17][17] = st
            pixels_list_B[20][16] = st
            pixels_list_B[22][17] = st

            avatarB = True

        if item == "spear": 
            # colors
            br = (150, 108, 108) # brown for wizard staff
            dg = (132, 138, 153) # dark grey
            lg = (179, 185, 199) # light grey

            # staff
            pixels_list_B[23][19] = br
            pixels_list_B[22][19] = br
            pixels_list_B[22][20] = br
            pixels_list_B[21][20] = br
            pixels_list_B[20][20] = br
            pixels_list_B[20][21] = br
            pixels_list_B[19][21] = br
            pixels_list_B[18][21] = br
            pixels_list_B[18][22] = br
            pixels_list_B[17][22] = br
            pixels_list_B[16][22] = br
            pixels_list_B[15][22] = br
            pixels_list_B[15][23] = br
            pixels_list_B[14][23] = br
            pixels_list_B[13][23] = br

            # metal head
            pixels_list_B[12][23] = lg
            pixels_list_B[13][24] = dg
            pixels_list_B[12][24] = dg
            pixels_list_B[11][24] = lg
            pixels_list_B[12][25] = dg
            pixels_list_B[11][25] = dg
            pixels_list_B[10][25] = lg


            avatarB = True

        if avatarB == True: 
            return pixels_list_B


    def save_character_pic(self, pixels_list):
        """ To be able to save the character pixel_list created with build_character"""
        self.pixels_list = pixels_list

        # transform list into array
        avatar_array = np.array(pixels_list, dtype=np.uint8)
        avatar_image = Image.fromarray(avatar_array)
        avatar_image = avatar_image.resize((600, 600), resample=Image.NEAREST)
        avatar_image.save("avatar.png")

        # resize character image, so that it can fit on map
        image = Image.open('avatar.png')
        new_image = image.resize((150, 150))
        new_image.save('avatar_resized.png')

    def show_avatar_on_screen(self, saved_png_filename, pygame_screen,x, y):
        """ function to print the generated character on the screen"""
        self.saved_png_filename = saved_png_filename
        self.pygame_screen = pygame_screen
        self.x = x
        self.y = y

        playerImage = pygame.image.load(saved_png_filename)
        pygame_screen.blit(playerImage, (x, y))


    
       
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
# all the color palettes user can choose from
skin_palette = {"Dark Brown": (70, 42, 18), "Brown": (98, 59, 25), "Mid Brown": (152, 102, 57), "Light Brown": (163, 118, 79),"Tanned White": (241, 194, 125), "White": (255, 219, 172), "Pinkish": (244, 208, 205)}
eye_palette = {"Blue": (46, 83, 111), "Grey Blue": (152, 175, 199), "Brown": (99, 78, 52), "Black Brown": (25, 16, 7), "Green": (61, 103, 29), "Grey Green": (73, 118, 101)}
natural_hair_palette = {"Blonde": (250, 240, 130), "Dirty Blonde": (223, 195, 147), "Orange": (231, 151, 13), "Ginger": (202, 116, 0), "Light Brown": (137, 85, 57), "Dark Brown": (100, 47, 12), "Black": (10, 5, 0), "Grey": (145, 145, 145), "White": (240, 247, 255) }
unnatural_hair_palette = {"Red": (168, 0, 0), "Purple": (155, 70, 170), "Blue": (75, 89, 170), "Green": (109, 165, 44), "Coral": (249, 139, 136), "Pink": (255, 105, 180), "Bright Red": (254, 32, 32)}
clothing_neutrals = {"Green": (190, 186, 152), "Grey": (199, 199, 199), "Beige": (196, 177, 160), "Brown": (156, 132, 124), "Blue": (157, 173, 193), "Dirty Pink": (193, 157, 173), "Violet": (177, 157, 193), "Turquoise": (157, 191, 193), "Khaki": (177, 139, 103)}
clothing_dark_colors = {"Black": (39, 39, 39), "Grey": (82, 84, 86), "Brown": (52, 32, 29), "Blue": (26, 54, 97), "Green": (19, 69, 50), "Red": (111, 0, 0), "Violet": (72, 0, 103), "Turquoise": (29, 96, 108), "Orange": (213, 84, 41)}
clothing_light_colors = {"Green": (176, 229, 31), "Yellow": (243, 231, 95), "Hot Pink": (243, 68, 182), "Blue": (1, 176, 221), "Bright Red": (245, 1, 0), "Violet": (225, 184, 245), "Turquoise": (133, 209, 188), "Light Orange": (247, 175, 54), "Baby Pink": (234, 166, 179), "Baby Blue": (149, 204, 213)}

# for base character displayed at the beginning
hr = natural_hair_palette["Black"] # Hair color
sk = skin_palette["Light Brown"] # Skin
bl = (sk[0], sk[1] - 34, sk[2]) # blushies
jk = clothing_dark_colors["Black"] # Jacket
ts = clothing_light_colors["Baby Pink"] # T-shirt
ps = clothing_neutrals["Grey"] # pants (/skirt)
sh = clothing_dark_colors["Brown"] # shoes
ey = eye_palette["Black Brown"] # Eye color / pupil
hairstyle = "short"
pants_long = True 
pants_short = False
skirt_long = False
skirt_short = False
item = "" # item empty for now


user = Person("Lisa", "Woman", 19)
pixels = user.build_character(hr, sk, jk, ts, ps, sh, ey, "ponytail", False, True, skirt_long, skirt_short, "wizard robe")
user.save_character_pic(pixels)
print(user.hairstyle)
"""
import pygame
from pygame import mixer # for music
import time
from End_Screen import end_screen
import os

#file_path ="C:\Projects\AdventureGame\Txt_files"
file_path = str(os.path.abspath("Txt_files"))


def multilineRender(window, text, x, y, font, colour):
    """ function to be able to print several lines of text at once without them overlapping"""
    text = text.strip().replace('\r','').split('\n')
    max_width = 0
    text_bitmaps = [] 

    # Convert all the text into bitmaps (mapping to bits), calculate the justification width
    for t in text: # each line seperately
        text_bitmap = font.render(t, True, colour)
        text_width  = text_bitmap.get_width() 
        text_bitmaps.append((text_width, text_bitmap))
        if (max_width < text_width):
            max_width = text_width 
    
    # Paint all the text bitmaps to the screen
    for (width, bitmap) in text_bitmaps:  
        window.blit(bitmap, (x, y) )  # where text will be placed
        y += bitmap.get_height()
    return y


class FileInfo:
    """Class to format the text files """

    def __init__(self):
        self.infotext = ""
        self.options = []
        self.InvalidOptionEntered = False 


    def ReadInfoFromFile(self,fname, user):
        """Function to read the files and finds out which comes after the input
        (which file ha^s to be opened after each decision """

        self.InvalidOptionEntered = False 
        self.infotext = ""
        self.options = []
        optionsInfo = []

        #string options - for the game only options 1, 2, 3, q/Q, and k/K, but theoretical there could be up to 9 options (more generally useable)
        stroptions = ["1","2","3","4","5","6","7","8","9","Q","q","K","k"]  

        file_name = file_path + fname 

        with open(file_name, 'r', encoding='utf-8') as f:  
            line = ""
            for ln in f:
                line=ln

                # For formatting all text files
                if "{name}" in line: 
                    line = line.format(name = user.name)
                if "{age}" in line:
                    line = line.format(age = int(user.age) + 10)
                if "{gender}" in line:
                    if user.gender == "Woman":
                        line = line.format(gender = "mother")
                    if user.gender == "Man":
                        line = line.format(gender = "father")
                    else:
                        line = line.format(gender = "parent")

                if line[0] == '\ufeff': #we need to take out the first character of the text files:'\ufeff'
                    line = line[1:] 
                if line[0] == '(' and stroptions.count(line[1])>-1 and line[2] == ')': # find out which option are given (e.g. detect if the file starts with ("1") )
                    self.options.append(line[1]) # put the options under the other text
                    optionsInfo.append(line) 
                else :
                    self.infotext += line
        
        for s in optionsInfo:
            self.infotext += s


class InputBox:
    """class to create input box object"""

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text = event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)


    def draw(self, window):
        # Blit the text.
        window.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(window, self.color, self.rect, 2)


class Background(pygame.sprite.Sprite):
    """class for background images: picture automatically resizes if screen enlarged"""

    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        # scale the picture with the size of the window:
        self.image= pygame.transform.scale(self.image,(info.current_w, info.current_h - 30)) 
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

pygame.init()
info = pygame.display.Info() # we take the sizes of the screen
width =  info.current_w  
height = info.current_h - 30
window = pygame.display.set_mode( (width, height),pygame.RESIZABLE) 

COLOR_TEXT = pygame.Color('black')
COLOR_INACTIVE = pygame.Color('black')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.SysFont('TimesNewRoman', 35)
MAX_OPTIONS=9

def main(user, hr, sk, jk, ts, ps, sh, ey, hairstyle, pants_long, pants_short, skirt_long, skirt_short):
    """ function for the story part of the game"""
    starttime = time.time()

    # new screen caption
    pygame.display.set_caption("Your Adventure:") 

    clock = pygame.time.Clock()
    input_box = InputBox(0, 0, 0, 0)
    input_box.txt_surface=FONT.render(input_box.text, True, input_box.color)
    
    finfo = FileInfo()
    finfo.ReadInfoFromFile("\\_start.txt", user)
    currentfilename = "start"
  
    #Background music
    mixer.init()
    mixer.music.load('music.wav')
    mixer.music.play(-1) # (-1) makes the music play in a loop as long as the game is being played

    Done = False  # for game loop
    EndGameReached = False 

    while not Done:
        for event in pygame.event.get():
            input_box.handle_event(event)

            if event.type == pygame.QUIT:
               Done = True  # quit while-loop
        
            mytext = input_box.text # take input from input text

            if len(mytext) == 1:
                mytext = mytext.upper()
                if mytext == 'Q':  # if input text = Q or q -> quit the program
                    Done = True

                # we make a loop to go from file for example: 1_1 to file 1_1_2 if the input is "2"
                if finfo.options.count(mytext) == 1:
                    finfo.InvalidOptionEntered = False
                    
                    if currentfilename == "start":
                        currentfilename = mytext
                    else:
                        currentfilename = currentfilename + "_" + mytext  # to go through the next file on path

                else:
                    if not finfo.InvalidOptionEntered:
                        finfo.infotext += "\n" + "Sorry, this is an invalid option"
                        finfo.InvalidOptionEntered = True 

                # if the input is k we display the end screen
                if not finfo.InvalidOptionEntered and mytext != 'K':  
                    actualfilename = "\\" + currentfilename + ".txt"
                    finfo.ReadInfoFromFile(actualfilename, user)
                input_box.text = ""
     
                if mytext == 'K':  # end of the path/story
                    window.fill([30, 30, 30])
                    EndGameReached = True 
                    endtime = time.time()  # record the amount of time played until k was pressed
               
             # different backgrounds detecting happy or tragic end in the text files
            if not EndGameReached :                            
                if (finfo.infotext.find("The End!(Happy)") != -1):
                    BackGround = Background("images/good_end.jpg", [0,0])
                    window.fill([30, 30, 30])
                    window.blit(BackGround.image, BackGround.rect)

                elif (finfo.infotext.find("The End!(Tragic)") != -1):
                    BackGround = Background("images/bad_end.jpg", [0,0])
                    window.fill([30, 30, 30])
                    window.blit(BackGround.image, BackGround.rect)

                # default background for the questions if neither Happy nor Sad ending
                else:
                    DefaultBackGround = Background("images/background_1.jpg", [0,0])
                    window.fill([255, 255, 255])
                    window.blit(DefaultBackGround.image, DefaultBackGround.rect)

                # adjust the inputbox under the text           
                coord_y = multilineRender(window, finfo.infotext, 5, 5, FONT, COLOR_TEXT)
                input_box.rect = pygame.Rect(100, (coord_y + 10), 50, 30)
                input_box.draw(window)
            
            else: # at the eding, check if an item was acquired --> different endings have different items
                items = {"\\1_1_1_1_1_1_1_1.txt": "spear", "\\1_1_1_1_1_1_1_2.txt": "spear", "\\1_1_1_1_1_1_2.txt": "spear", 
                         "\\1_1_1_1_1_2.txt": "spear", 
                         "\\1_1_1_1_2_1_1_1.txt":"knifes", "\\1_1_1_1_2_1_1_2.txt":"knifes", "\\1_1_1_1_2_1_2.txt":"knifes",  
                         "\\1_1_1_1_2_2.txt":"knifes", "\\1_2_1_1_1_2_1_1_1.txt":"knifes",
                         "\\1_2_1_2_1_1_2.txt": "wizard's robe", "\\1_3_2_1_1_2.txt": "wizard's robe",
                         "\\1_3_1_1_1.txt": "wizard's staff", 
                         "\\1_3_2_1_1_1.txt": "medic's robe"
                            }
                try:
                    newitem = items[actualfilename]
                    
                except:  # if no new item was acquired, the "try: newitem = items[actualfilename]" will fail
                    newitem = ""

                # build character with new item
                pixels = user.build_character(hr, sk, jk, ts, ps, sh, ey, hairstyle, pants_long, pants_short, 
                                                skirt_long, skirt_short, item=newitem)
                user.save_character_pic(pixels_list=pixels)
                print(user.item)

                # go to the end screen
                end_screen(user, newitem, starttime, endtime)

            pygame.display.update()



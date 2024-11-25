from Character_generator import main_char_gen
from Story_Main import main
import pygame



if __name__ == '__main__':
    """ main game loop, starts with name, age, gender input, then character is generated,
        then story starts, then end screen shown """
        
    player = main_char_gen()
    main(player, player.hr, player.sk, player.jk, player.ts, player.ps, player.sh, player.ey, 
            player.hairstyle, player.pants_long, player.pants_short, player.skirt_long, player.skirt_short)
    pygame.quit()
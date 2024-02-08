import pygame
from itertools import chain

from functions import *
from Player import *
from Object import *
from TerrainBlocks import *
from Traps import *
from Fruits import *
from Fruits import fruit_counter

pygame.init()

pygame.display.set_caption("Super Hemmie-o")
# new_logo = pygame.image.load("HemalPuppyHead")
# pygame.display.set_icon(new_logo)

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Pink.png")
    
    block_size = 96


    player = Player(-950, 400, 200, 200)
    fire1 = Fire(block_size * -4 - 16, HEIGHT - block_size - 64, 16, 32)
    fire2 = Fire(block_size * -2 - 16, HEIGHT - block_size - 64, 16, 32)
    apple = Apple(block_size * -5 + 16, HEIGHT - block_size * 4 - 64 , 32, 32)
    banana = Bananas(block_size * -4 + 16, HEIGHT - block_size * 4 - 64 , 32, 32)
    cherries = Cherries(block_size * -3 + 16, HEIGHT - block_size * 4 - 64 , 32, 32)
    kiwi = Kiwi(block_size * -2 + 16, HEIGHT - block_size * 4 - 64 , 32, 32)
    melon = Melon(block_size * 5 + 16, HEIGHT - block_size * 5 - 64 , 32, 32)
    orange = Orange(block_size * 6 + 16, HEIGHT - block_size * 5 - 64 , 32, 32)
    pineapple = Pineapple(block_size * 9 + 16, HEIGHT - block_size * 6 - 64 , 32, 32)
    strawberry = Strawberry(block_size * 10 + 16, HEIGHT - block_size * 6 - 64 , 32, 32)

    fire1.on()
    fire2.on()

    floor = [Terrain(i * block_size, HEIGHT - block_size, block_size) 
             for i in range(-WIDTH // block_size - 2, 2)]
    hidden_wall = [Terrain(block_size * -14, HEIGHT - block_size * i, block_size) 
             for i in range(1, 8)]
    mini_platform = [Terrain(block_size * i, HEIGHT - block_size * 4, block_size) 
            for i in range(-5, -1)]
    wall = [Terrain(block_size * 2, HEIGHT - block_size * j , block_size) 
           for j in chain(range(0, 7), range(8,20))]
    floating_platform1 = [Terrain(block_size * i, HEIGHT - block_size * 5 , block_size)
                          for i in range(5, 7)]
    floating_platform2 = [NetherTerrain(block_size * i, HEIGHT - block_size * 6 , block_size)
                          for i in range(9, 11)]
    floating_platform3 = [Terrain(block_size * i, HEIGHT - block_size * 5 , block_size)
                          for i in range(13, 15)]
    before_rising_block = [Terrain(block_size * i, HEIGHT - block_size * j , block_size)
                          for i in range(17, 20) for j in range(1, 4)]
    pink_floor =   [PinkTerrain(block_size * i, HEIGHT - block_size , block_size)
                          for i in range(3, WIDTH * 2 // block_size - 3)]
    

    objects = [*floor, *pink_floor, *hidden_wall,
               Terrain(block_size * -8, HEIGHT - block_size * 2, block_size),
               *mini_platform, *wall, 
               *floating_platform1, *floating_platform2, *floating_platform3,
               *before_rising_block,
               apple, banana, cherries, kiwi, melon, orange, pineapple, strawberry,
                fire1, fire2] 

    initial_offset_x = -1100
    offset_x = -1100
    scroll_area_width = 250

    run = True
    while(run):
        
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player.jump_count < 2:
                    player.jump()   
        
        player.loop(FPS)
        fire1.loop()
        fire2.loop()
        apple.loop()
        banana.loop()
        cherries.loop()
        kiwi.loop()
        melon.loop()
        orange.loop()
        pineapple.loop()
        strawberry.loop()
        handle_move(player, objects)
        draw(window, background, bg_image, player, objects, offset_x)     

        if ((player.rect.right - offset_x <= scroll_area_width) and player.x_vel < 0):
            if initial_offset_x <= offset_x + player.x_vel:
                offset_x += player.x_vel
        elif (player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0:
            offset_x += player.x_vel

        if offset_x < initial_offset_x:
            offset_x = initial_offset_x

    pygame.quit()
    quit()        

if __name__ == "__main__":
    main(window)
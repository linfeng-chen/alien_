import pygame
import sys
def run():
    '''初始化一个空屏幕'''
    pygame.init()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("TEST")
    bg_color=(0,255,0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                print(event.type)

            elif event.type == pygame.KEYUP:
                print(event.type)

        pygame.display.flip()

run()


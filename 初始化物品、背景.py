import sys
import pygame
from settings import Setting
from ship import Ship

def run_game():
    '''初始化游戏并创建一个屏幕对象'''
    pygame.init()
    # 创建实例
    ai_settings=Setting()
    screen = pygame.display.set_mode((ai_settings.screen_height,ai_settings.screen_width))#设置屏幕大小
    pygame.display.set_caption("Alien Invasion")#设置标题
    # 创建飞船
    ship = Ship(screen)
    # 设置背景色
    bg_color = (0,255,0)

    #  开始游戏的主循环
    while True:
        '''监视鼠标和键盘事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
# 添加飞船图像

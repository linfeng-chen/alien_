import pygame
from settings import Setting
from ship import Ship
import game_functions as gf
from background import Background

def run_game():
    '''初始化游戏并创建一个屏幕对象'''
    pygame.init()
    # 创建实例
    ai_settings=Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#设置屏幕大小
    pygame.display.set_caption("Alien Invasion")#设置标题
    # 创建飞船
    ship = Ship(screen,ai_settings)
    # 创建背景
    background = Background(screen)

    # 设置背景色
    #  开始游戏的主循环
    while True:
        '''监视鼠标和键盘事件'''
        gf.check_events(ship)
        ship.update()
        gf.Update_screen(ai_settings,screen,ship,background)


run_game()
# 添加飞船图像/
# 将管理事件代码单独放在模块中
# 将屏幕更新放在管理事件代码模块中
# 控制飞船移动
# 调整飞船移动速度，避免移动到屏幕以外
# 限制飞船的活动范围
# 重构check_events函数
# 添加子弹设置

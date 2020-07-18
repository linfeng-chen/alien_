import pygame
from settings import Setting
from ship import Ship
import game_functions as gf
from background import Background
from pygame.sprite import Group


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
    # 创建一个用于储存子弹的编组
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # 创建一个外星人
    # alien = Alien(ai_settings,screen)

    # 设置背景色
    #  开始游戏的主循环
    while True:
        '''监视鼠标和键盘事件'''
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings, screen, ship, background,aliens,bullets)


run_game()
# 添加飞船图像/
# 将管理事件代码单独放在模块中
# 将屏幕更新放在管理事件代码模块中
# 控制飞船移动
# 调整飞船移动速度，避免移动到屏幕以外
# 限制飞船的活动范围
# 重构check_events函数
# 添加子弹设置
# 发射子弹
# 删除消失的子弹
# 限制子弹数量
# 创建一个外星人
# 创建一群外星人
# 让外星人动起来
# 表示外星人移动方向
# 检查外星人是否撞到屏幕边缘
# 向下移动外星人群并改变移动方向





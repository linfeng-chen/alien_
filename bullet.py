import pygame
from  pygame.sprite import Sprite

class Bullet(Sprite):
    '''对发射的子弹进行管理'''
    def __init__(self,ai_settings,screen,ship):
        '''在飞船所处位置创建一个子弹对象'''
        super(Bullet,self).__init__()
        self.screen = screen

        #在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 储存用小数表示的子弹位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet.color
        self.speed_factor = ai_settings.bullet_speed_factor

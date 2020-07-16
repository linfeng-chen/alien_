import pygame

class Background():
    '''添加背景'''
    def __init__(self,screen):
        '''加载背景图像并获取其矩形'''
        self.screen = screen
        self.background = pygame.image.load("images/b.bmp")
        self.rect = self.background.get_rect()
        self.screen_rect = self.screen.get_rect()

        '''将背景填充屏幕'''
        self.rect.centerx = self.screen_rect.centerx

    def blitme(self):
        '''在指定位置填充屏幕'''
        self.screen.blit(self.background, self.rect)

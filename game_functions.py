import sys
import pygame



def check_keydown_events(event,ship):
    '''相应按键'''
    if event.key == pygame.K_RIGHT:
        '''向右运动'''
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        '''向左运动'''
    ship.moving_left = True

def check_keyup_events(event,ship):
    '''相应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    '''响应鼠标和按键事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def Update_screen(ai_settings,screen,ship,background):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环重绘屏幕
    screen.fill(ai_settings.bg_color)
    background.blitme()
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
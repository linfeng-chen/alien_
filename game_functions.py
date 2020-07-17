import sys
import pygame
from bullet import Bullet


def check_keydown_events(event,ai_settings,screen,ship,bulltes):
    '''相应按键'''
    if event.key == pygame.K_RIGHT:
        '''向右运动'''
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        '''向左运动'''
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        '''创建一颗子弹，并将其加入编组bullets中'''
        if len(bulltes)<ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bulltes.add(new_bullet)


def check_keyup_events(event,ship):
    '''相应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    '''响应鼠标和按键事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def Update_screen(ai_settings,screen,ship,background,bullets):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环重绘屏幕
    screen.fill(ai_settings.bg_color)
    background.blitme()
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    '''更新子弹的位置并删除已消失的子弹'''
    bullets.update()

    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


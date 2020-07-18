import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''相应按键'''
    if event.key == pygame.K_RIGHT:
        '''向右运动'''
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        '''向左运动'''
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key ==pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings,screen,ship,bullets):
    '''创建一颗子弹，并将其加入编组bullets中'''
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


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

def update_screen(ai_settings,screen,ship,background,aliens,bullets):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环重绘屏幕
    screen.fill(ai_settings.bg_color)
    background.blitme()
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_aliens(ai_settings,aliens):
    '''更新全部外星人的位置'''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

def update_bullets(bullets):
    '''更新子弹的位置并删除已消失的子弹'''
    bullets.update()

    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)




def get_number_aliens_x(ai_settings,alien_width):
    '''计算每行外星人'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_row(ai_settings,ship_height,alien_height):
    '''计算屏幕可容纳多少行外星人'''
    available_space_y = ai_settings.screen_height - 3*alien_height -ship_height
    num_rows = int(available_space_y/(2*alien_height))
    return num_rows

def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
    # 创建一个外星人并将其加入到当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x

    alien.rect.y = alien.rect.height +2*alien.rect.height*row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen,ship, aliens):
    '''创建外星人群'''
    # 创建一个外星人，计算一行能容纳多少外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_row = get_number_row(ai_settings,ship.rect.height,alien.rect.height)

    # 创建第一行外星人
    for row_number in range(number_row):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings, screen, aliens, alien_number,row_number)

def check_fleet_edges(ai_settings,aliens):
    '''有外星人到达边缘时采取措施'''
    for alien in aliens.sprites():
        if alien.chcek_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    '''将外星人下移，并改变方向'''
    for alien in aliens.sprites():
        alien.rect.y +=ai_settings.alien_drop_speed
    ai_settings.fleet_direction *=-1
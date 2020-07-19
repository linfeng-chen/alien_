import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

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

def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets):
    '''响应鼠标和按键事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            '''使用pygame.mouse.get_pos()，它返回一个元组，其中包含玩家单击时鼠标的x和y坐标'''
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)


def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    '''在玩家单机play按钮时开始新游戏'''
    '''函数使用collidepoint()检查鼠标单击位置是否在Play按钮的rect内'''
    button_chicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_chicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏信息
        stats.reset_stats()
        stats.game_active =True
        #清空外星人和子弹
        aliens.empty()
        bullets.empty()
#         创建新的外星人并让飞船居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

def update_screen(ai_settings,screen,stats,ship,background,aliens,bullets,play_button):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环重绘屏幕
    screen.fill(ai_settings.bg_color)
    background.blitme()
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    aliens.draw(screen)

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    '''响应被外星人撞到的飞船'''
    if stats.ship_left >0:
        # 将ship_left减1
        stats.ship_left -= 1

        # 清空外星人列表和子弹列表、
        aliens.empty()
        bullets.empty()

        # 创建新的外星人群并将飞船置于屏幕中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active =False
        pygame.mouse.set_visible(True)


def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    '''更新全部外星人的位置'''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    #检测外星人与飞船的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
    #检测外星人到达屏幕底端
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)


def update_bullets(ai_settings,screen,ship,aliens,bullets):
    '''更新子弹的位置并删除已消失的子弹'''
    bullets.update()

    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)


def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
    # 检查是否有子弹击中外星人
    # 如果击中了就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    '''这行代码遍历编组bullets中的每颗子弹，再遍历编组aliens中的每个外星人。每当
    有子弹和外星人的rect重叠时，groupcollide()就在它返回的字典中添加一个键值对。
    两个实参True告诉Pygame删除发生碰撞的子弹和外星人'''
    if len(aliens) == 0:
        # 删除现有的子弹,提升等级，并新建一群外星人

        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    '''检查外星人是否到达底端'''
    screen_rect =screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >=screen_rect.bottom:
            '''像飞船被撞一样处理'''
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break


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
class Setting():
    '''存储游戏中的设置'''
    def __init__(self):
        '''初始化游戏的设置'''
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(0,0,100)

        # 飞船速度设置
        self.ship_speed_factor = 1.5
        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color=(60,60,60)
        self.bullet_allowed =15
        #外星人设置
        self.alien_speed_factor =1
        self.alien_drop_speed = 10
        #fleet_direction =1表示右移，-1表示左移
        self.fleet_direction = 1










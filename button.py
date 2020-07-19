import pygame.font
# '''将文本渲染到屏幕上'''

class Button():
    def __init__(self,ai_settings,screen,msg):
        '''初始化按钮属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width,self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)    #设置字体，None表示使用默认字体
        #创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #按钮的标签只需创建一次
        self.prep_msg(msg)
        #Pygame通过将你要显示的字符串渲染为图像来处理文本

    def prep_msg(self,msg):
        '''将文本渲染为图像并使其在按钮上居中
        方法font.render()还接受
        一个布尔实参，该实参指定开启还是关闭反锯齿功能（反锯齿让文本的边缘更平滑）。余下的两
        个实参分别是文本颜色和背景色'''
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''绘制一个用颜色填充的按钮再绘制文本'''
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
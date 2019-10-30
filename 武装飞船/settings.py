class settings():
    """一个存储游戏《外星人入侵》的所有设置的类""" 
    def __init__(self):
        """初始化游戏的静态设置""" 
        # 设置背景 ：宽度（像素） 高度（像素） 颜色（三基色组成）
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 0)  
        
        # 设置飞船命数
        self.ship_limit = 3
        
        # 设置子弹 ：速度 宽度 长度（高度） 颜色
        self.bullet_speed_factor = 3
        self.bullet_width = 150
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        
        # 外星人每次下降高度
        self.fleet_drop_speed = 10

        # 以什么样的速度加快游戏节奏 
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5

        # 上面为静态，以外的放在initialize
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        # 外星人速度
        self.alien_speed_factor = 1
        
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        
        # 子弹允许数量
        self.bullets_allowed = 3
       
        # 飞船速度
        self.ship_speed_factor = 2.0

        # 记分 
        self.alien_points = 50


    def increase_speed(self): 
        """提高速度设置和外星人点数""" 
        self.alien_speed_factor *= self.speedup_scale
        self.bullets_allowed *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        



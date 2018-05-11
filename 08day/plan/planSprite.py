import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)

FRAME_PER_SEC = 60

CREATE_ENEMY_EVENT = pygame.USEREVENT

HERO_FIRE_EVENT = pygame.USEREVENT +1
#精灵类
class GameSprite(pygame.sprite.Sprite):
	def __init__(self, image_name, speed=1):
		# 调用父类的初始化方法
		super().__init__()

		# 加载图像
		self.image = pygame.image.load(image_name)
		# 设置尺寸
		self.rect = self.image.get_rect()
		# 记录速度
		self.speed = speed



	def update(self):
		self.rect.y += self.speed

class Background(GameSprite):	
	def __init__(self,is_alt=False):
		image_name = './images/background.png'
		super().__init__(image_name)
		if is_alt:
			self.rect.y = -self.rect.height

	def update(self):
		super().update()
		if self.rect.y > SCREEN_RECT.height:
			self.rect.y = -self.rect.height


class Enemy(GameSprite):
	def __init__(self):
		image_name = './images/enemy1.png'
		super().__init__(image_name)

		self.speed = random.randint(1,3)
		self.rect.bottom = 0
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)
	

		def update(self):
			super().update()
			if self.rect.y >= SCREEN_RECT.height:
				print('敌机飞出屏幕')
				self.kill()
		def __del__(self):
			pass

class Hero(GameSprite):
	def __init__(self):
		image_name = './images/hero.gif'
		super().__init__(image_name,0)
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
		self.bullet_group= pygame.sprite.Group()
		self.speed1 = 0


	def update(self):
		self.rect.x += self.speed
		self.rect.y += self.speed1
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_RECT.width:
			self.rect.right = SCREEN_RECT.width

	def fire(self):
		print('发射子弹')
		bullet = Bullet()
		bullet.rect.bottom = self.rect.y -20
		bullet.rect.centerx = self.rect.centerx
		self.bullet_group.add(bullet)
class Bullet(GameSprite):
	def __init__(self):
		super().__init__('./images/bullet1.png',-10)
	def update(self):
		super().update()
		if self.rect.bottom < 0:
			self.kill()



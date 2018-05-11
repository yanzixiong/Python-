import pygame
from planSprite import *

class PlanGame(object):
	#初始化
	def __init__(self):
		print("游戏初始化")
		#创建窗口
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		#创建时钟对象
		self.clock = pygame.time.Clock()
		self.__create_sprite()
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)#毫秒
		pygame.time.set_timer(HERO_FIRE_EVENT,500)


		self.enemy_group = pygame.sprite.Group()
	#开始游戏
	def startGame(self):
		print("开始游戏")	
		while True:
			self.clock.tick(FRAME_PER_SEC)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()

			pygame.display.update()


	#创建精灵或精灵组
	def __create_sprite(self):
		bg1 = Background()
		bg2 = Background(True)
		self.back_group = pygame.sprite.Group(bg1,bg2) 

		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)

		


	#事件监听
	def __event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				PlanGame.__game_over(self)
			elif event.type == CREATE_ENEMY_EVENT:
				enemy = Enemy()
				self.enemy_group.add(enemy)
			elif event.type == HERO_FIRE_EVENT:
				self.hero.fire()
		
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_RIGHT]:
			self.hero.speed = 2
			self.hero.speed1 = 0
		elif keys_pressed[pygame.K_LEFT]:
			self.hero.speed = -2
			self.hero.speed1 = 0
		elif keys_pressed[pygame.K_UP]:
			self.hero.speed = -2
			self.hero.speed1 = 0
		elif keys_pressed[pygame.K_DOWN]:
			self.hero.speed = 2
			self.hero.speed1 = 0
		else:
			self.hero.speed1 = 0
			self.hero.speed = 0

				

	#碰撞检测

	def __check_collide(self):
		b = pygame.sprite.groupcollide(self.hero.bullet_group,self.enemy_group,True,True)
		print(b)

		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		if len(enemies) > 0:
			self.hero.kill()
			PlanGame.__game_over(self)
	#更新精灵组
	def __update_sprites(self):
		self.back_group.update()
		self.back_group.draw(self.screen)

		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

		self.hero_group.update()
		self.hero_group.draw(self.screen)

		self.hero.bullet_group.update()
		self.hero.bullet_group.draw(self.screen)


	@staticmethod
	def __game_over(self):
		print("游戏结束")	
		pygame.quit()
		exit()	


if __name__ == '__main__':
	plangame = PlanGame()
	plangame.startGame()

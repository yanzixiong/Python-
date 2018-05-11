import pygame 
from planSprite import *
pygame.init()
screen = pygame.display.set_mode((450,700))

#绘制背景
bg = pygame.image.load('./飞机大战/background.png')
screen.blit(bg,(0,0))
#pygame.display.update()

#绘制英雄
hero = pygame.image.load('./飞机大战/hero.gif')
screen.blit(hero,(180,500))

hero_rect = pygame.Rect(180,500,200,200)
#绘制敌机
enemy = GameSprite('./飞机大战/enemy1.png')
enemy1 = GameSprite('./飞机大战/enemy1.png',3)
enemy1.rect.x = 100
enemy_group = pygame.sprite.Group(enemy,enemy1)

clock = pygame.time.Clock()

while True:
	clock.tick(300)
	hero_rect.y -= 1
	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)
	#监听退出
	if hero_rect.bottom<= 0:
		hero_rect.y = 700
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print('退出游戏')
			pygame.quit()
			exit()
	enemy_group.update()
	enemy_group.draw(screen)
	pygame.display.update()
pygame.quit()

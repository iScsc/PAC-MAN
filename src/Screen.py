

import pygame as pg
import os 
from pygame.locals import *											# import of global variables

link = "../res/sprites/characters.png" 									# link of the image of the characters

class Screen :
	
	BLACK = 0, 0, 0
	RED = 255, 0, 0
	
	def __init__(self):
		pg.init()
		self.size = 1000,500
		self.widith, self.height = self.size
		self.screen = pg.display.set_mode(self.size)
		self.running = True
		self.list_image = []
		self.list_rect = []


	def aff(self,link):
		image = pg.image.load(link)
		self.list_image.append(image)
		rect = image.get_rect()
		self.list_rect.append(rect)


	def end(self,event):
		return(event.type == QUIT or (event.type == KEYDOWN and event.key == K_q))	

	
	def run(self):
		while self.running : 
			for event in pg.event.get():
				if self.end(event):
					self.running = False
	
			self.screen.fill(Screen.BLACK)
			for i in range(len(self.list_image)) :
				self.screen.blit(self.list_image[i], self.list_rect[i])	
			pg.display.update()
		pg.quit()


if '__main__' == __name__ :
	ig = Screen()
	ig.aff(link)
	ig.run()





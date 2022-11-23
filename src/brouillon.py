

import pygame as pg
import os 
from pygame.locals import *											# import of global variables

link = "../res/sprites/characters.png" 										# link of the image of the characters

class Screen :
	
	BLACK = 0, 0, 0
	RED = 255, 0, 0

	def clip(surface, x, y, x_size, y_size): 						#Get a part of the image
		handle_surface = surface.copy() 						#Sprite that will get process later
		clipRect = pg.Rect(x,y,x_size,y_size) 						#Part of the image
		handle_surface.set_clip(clipRect) 						#Clip or you can call cropped
		image = surface.subsurface(handle_surface.get_clip())				#Get subsurface
		return image.copy() 								#Return


	def __init__(self):
		pg.init()
		self.size = 1000,500
		self.widith, self.height = self.size
		self.screen = pg.display.set_mode(self.size)
		self.running = True
		self.list_image = []
		self.list_rect = []


	def aff(self, link):
		image = pg.image.load(link)
		self.list_image.append(image)
		rect = image.get_rect()
		self.list_rect.append(rect)

	def aff_part(self, link, x, y, x_size, y_size):
		image = pg.image.load(link)
		image = Screen.clip(image, x, y, x_size, y_size)
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
	s = Screen()
	s.aff_part(link,0,0,15,15)
	s.run()





## Imports 

import pygame as pg
import os 
import numpy as np
from pygame.locals import *		# import of global variables




## Global variables
link = "../res/sprites/sprites.png" 	# link of the image of the characters
link_txt_map = "../res/maps/01.txt"


BLACK = 0, 0, 0
RED = 255, 0, 0


scale = 2
taille_case = 17 * scale
taille_sprite = 15 * scale
dim = 28,31 # en nombre de cases


## Class for managing printing on the screen

class Screen :
	
	def clip(surface, x, y, x_size, y_size): 			## Get a part of an image
		"""
		Get part of the image := surface
		at position (x,y)
		of size (x_size,y_size)
		"""
		handle_surface = surface.copy() 			# Sprite that will get process later
		clipRect = pg.Rect(x,y,x_size,y_size) 			# Part of the image
		handle_surface.set_clip(clipRect) 			# Clip or you can call cropped
		image = surface.subsurface(handle_surface.get_clip())	# Get subsurface
		return image.copy() 					# Return

	def init_map():
		liste = []
		dic = { "W" : 															#### A COMPLETER
			}
		with open(link) as file:
			i = 0
			for item in file:
				j = 0
				for s in item:
					rect = pg.Rect(i*taille_case, j*taille_case, taille_case, taille_case)
					liste.append((dic[s],rect))
					j+=1
		   		i+=1

	def __init__(self):								## create the window and initialise all sprits
		pg.init()
		self.size = dim[0] * taille_case, dim[1] * taille_case 			# scale of the window
		self.widith, self.height = self.size
		self.screen = pg.display.set_mode(self.size)
		self.running = True							# useless ??
		self.list_image = []
		self.list_rect = []		

		image = pg.image.load(link)						# image of all the sprites
		self.sprites_tab = [[image for j in range(8)] for i in range(5)]	# init of the tab containing sprites
		
		for i in range(5):
			for j in range(8):
				image_clip = Screen.clip(image, taille_sprite*j/scale, taille_sprite*i/scale, taille_sprite/scale, taille_sprite/scale)
				image_clip = pg.transform.rotozoom(image_clip, 0, scale)
				self.sprites_tab[i][j] = image_clip			# creation of sprites
		Screen.init_map()		


		
	def display_demo(self,entity_list):
		for entity in entity_list :
			x,y = entity[0] #entity.getXY()
			i,j = entity[1] #entity.getSprite() 
			#entity.Sprite()
			rect = pg.Rect(x*taille_case, y*taille_case, taille_sprite, taille_sprite)
			self.screen.blit(self.sprites_tab[i][j], rect)


	def display(self,entity_list):
		for entity in entity_list :
			x,y = entity.getXY()
			i,j = entity.getSprite() 
			entity.Sprite()
			rect = pg.Rect(x*taille_case, y*taille_case, taille_sprite, taille_sprite)
			self.screen.blit(self.sprites_tab[i][j], rect)

	




####	DEMO   ####

if '__main__' == __name__ :
	s = Screen()

	j = 2
	entity_list = [[(2*i,3*j),(i,j)] for i in range(5)]
	
	running = True
	while running : 
		for event in pg.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
				running = False

		s.screen.fill(BLACK)
		s.display_demo(entity_list)
		pg.display.update()
	pg.quit()


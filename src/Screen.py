## Imports 

import pygame as pg
import os 
import numpy as np
from pygame.locals import *		# import of global variables




## Global variables
link = "../res/sprites/sprites.png" 	# link of the image of the characters
link_txt_map = "/home/tudual/Public/PAC-MAN/res/maps/01.txt"
#"../res/maps/01.txt"


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

	def init_map(tab):
		liste = []
		dic = { "W" : tab[1][4],
			"O" : tab[2][5],
			"T" : tab[3][6],
			"x" : tab[4][7],
			"G" : tab[4][8],
			"=" : tab[4][9],
			"P" : tab[4][10],
			"D" : tab[4][11]
			}
		with open(link_txt_map,'r') as file:
			i = 0
			for item in file:
				j = 0
				l = []
				for s in item:
					if s != "\n" :
						rect = pg.Rect(i*taille_case, j*taille_case, taille_case, taille_case)
						l.append(dic[s]) ## Euh .....
					j+=1
				liste.append(l)
				i += 1
		return(liste)

	def __init__(self):								## create the window and initialise all sprits
		pg.init()
		self.size = dim[0] * taille_case, dim[1] * taille_case 			# scale of the window
		self.widith, self.height = self.size
		self.screen = pg.display.set_mode(self.size)
		self.running = True							# useless ??
		self.list_image = []
		self.list_rect = []		

		image = pg.image.load(link)						# image of all the sprites
		self.sprites_tab = [[image for j in range(12)] for i in range(7)]	# init of the tab containing sprites
		
		for i in range(7):
			for j in range(12):
				image_clip = Screen.clip(image, taille_sprite*j/scale, taille_sprite*i/scale, taille_sprite/scale, taille_sprite/scale)
				image_clip = pg.transform.rotozoom(image_clip, 0, scale)
				self.sprites_tab[i][j] = image_clip			# creation of sprites
		self.map = Screen.init_map(self.sprites_tab)		


		
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

	def display_map(self):
		for i in range(len(self.map)):
			for j in range(len(self.map[0])):
				rect = pg.Rect(j*taille_case, i*taille_case, taille_case, taille_case)
				self.screen.blit(self.map[i][j],rect)
			




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
		s.display_map()
		pg.display.update()
	pg.quit()








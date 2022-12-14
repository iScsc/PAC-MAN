import pygame as pg

class Player:
    
    keys = [pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN]
    
    points = 0
    
    @staticmethod
    def getEvents():
        
        r = [0 for i in range(len(Player.keys))]
        
        for event in pg.event.get():
            
            if event.type in Player.keys:
                r[Player.keys.index(event.type)] = 1
            
        return r
    

from Movable import Movable

class PacMan(Movable):
    
    spritesNumber = 3
    
    def __init__(self, x, y):
        super.__init__(x, y, 5, 0, PacMan.spriteNumber, dir=3)

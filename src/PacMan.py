import Movable

class PacMan(Movable):
    
    spritesNumber = 3
    
    def __init__(self, x, y):
        super.__init__(x, y, 4, 4, PacMan.spriteNumber, 0, 0)

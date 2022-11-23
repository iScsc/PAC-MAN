import Movable

class PacMan(Movable):
    
    spritesNumber = 3
    spritePosition = (4, 4)
    
    def __init__(self, x, y):
        super.__init__(x, y)

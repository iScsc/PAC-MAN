import Movable

class Ghost(Movable):
    
    spritesNumber = 2
    
    def __init__(self, x = 0, y = 0):
        super.__init__(x, y)
        
import Movable

class Ghost(Movable):
    
    powered = False
    
    spritesNumber = 2
    
    def __init__(self, x = 0, y = 0, i = 0):
        super.__init__(x, y, i, 2, Ghost.spritesNumber, 0, 2)
        self.eaten = False
    

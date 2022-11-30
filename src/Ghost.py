import Movable

class Ghost(Movable):
    
    powered = False
    
    spritesNumber = 2
    
    
    def __init__(self, x = 0, y = 0):
        super.__init__(x, y)
        self.eaten = False
        self.current = 0
        self.dir = 2    
    
    

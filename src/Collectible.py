import Entity

class Collectible(Entity):
    
    def __init__(self, x = 0, y = 0, i = 0, j = 0, maxSprite = 1, current = 0):
        super.__init__(x, y, i, j, maxSprite, current)
        
    def collect(self):
        pass
        
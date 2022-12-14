from Entity import Entity

class Movable(Entity):
    
    def __init__(self, x = 0, y = 0, i = 0, j = 0, maxSprite = 1, current = 0, dir = 0): # x,y pos / i,j sprite pos / max sprites / current sprite / sprite direction
        super.__init__(x, y, i, j, maxSprite, current)
        self.dir = dir
        
    
    def getSprite(self):
        return (self.i, self.j + self.current + self.dir * self.maxSprite)
        
    def move(self, x, y):
        self.x = x
        self.y = y

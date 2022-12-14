class Entity:
    
    def __init__(self, x = 0, y = 0, i = 0, j = 0, maxSprite = 1, current = 0): # x,y pos / i,j sprite pos / max sprites / current sprite
        self.x = x
        self.y = y
        self.i = i
        self.j = j
        self.maxSprite = maxSprite,
        self.current = current
    
    def changeCurrent(self):
        self.current += 1
        if self.current == self.maxSprite:
            self.current = 0
    
    def getXY(self): # returns object position (x, y)
        return (self.x, self.y)
    
    def getSprite(self): # returns sprite position to display (i, j)
        return (self.i, self.j + self.current)


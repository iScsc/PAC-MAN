class Entity:
    
    def __init__(self, x = 0, y = 0, i = 0, j = 0, maxSprite = 1, current = 0):
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
    
    def getXY(self):
        return (self.x, self.y)
    
    def getSprite(self):
        return (self.i + self.current, self.j)
    
from Collectible import Collectible

class Fruit(Collectible):
    
    fruits = [100, 300, 500, 700, 1000, 2000, 3000, 5000]
    
    def __init__(self, x = 0, y = 0, f = 0):  # f int describing the fruit
        super.__init__(x, y, 4, 4 + f)
        self.points = Fruit.fruits[f]
        
    def collect(self):
        return (self.points, True, False) #Points / Should display points granted ? / Should make Pac-Man super ?

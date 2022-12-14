from Collectible import Collectible

class PacGum(Collectible):
    
    points = 50
    
    def __init__(self, x = 0, y = 0):
        super.__init__(x, y, 99, 99)
    
    def collect(self):
        return (PacGum.points, False, True) #Points / Should display points granted ? / Should make Pac-Man super ?
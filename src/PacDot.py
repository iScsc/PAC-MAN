from Collectible import Collectible

class PacDot(Collectible):
    
    points = 10
    
    def __init__(self, x = 0, y = 0):
        super.__init__(x, y, 98, 98)
    
    def collect(self):
            return (PacDot.points, False, False) #Points / Should display points granted ? / Should make Pac-Man super ?

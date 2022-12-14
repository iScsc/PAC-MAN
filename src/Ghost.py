from Movable import Movable

class Ghost(Movable):
    
    powered = False
    
    basePoints = 200
    
    killedStreak = 0
    
    
    spritesNumber = 2
    
    def __init__(self, x = 0, y = 0, i = 0):  # i stands for the ghost type
        super.__init__(x, y, i, 2, Ghost.spritesNumber, current=0, dir=2)
        self.eaten = False
    
    def setEatable():
        Ghost.powered = True
    
    def eaten():
        if Ghost.killedStreak < 4:
            Ghost.killedStreak += 1
            
        return (Ghost.basePoints ** Ghost.killedStreak)
    
    def setNotEatable():
        Ghost.powered = False
        Ghost.killedStreak = 0

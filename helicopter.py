from utilis import randcell
import os
import sys

class Helicopter:
    def __init__(self, width, height):
        rc = randcell(width, height)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.height = height
        self.width = width
        self.water = 0
        self.maxwater = 1
        self.score = 0
        self.lives = 200
        
    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if(nx >= 0 and ny >= 0 and nx < self.height and ny < self.width):
            self.x, self.y = nx, ny
            
            
    def print_stats(self):
        print('💧', self.water, '/',  self.maxwater, sep='', end= ' | ')
        print('🏆', self.score, end=' | ')
        print('💛', self.lives)
        
    def game_over(self):
        os.system('cls')
        print('XXXXXXXXX')
        print('         ')
        print('GAME OVER', self.score)
        print('         ')
        print('XXXXXXXXX')
        sys.exit(0)
    
    def export_data(self):
        return {'score': self.score,
                'lives': self.lives,
                'x': self.x, 'y': self.y,
                'water': self.water, 'maxwater': self.maxwater}
     
    def import_data(self, data):
        self.x = data['x'] or 0
        self.y = data['y'] or 0
        self.water = data['water'] or 0
        self.maxwater = data['maxwater'] or 1
        self.score = data['score'] or 3
        self.lives = data['lives'] or 0
        
    
from utilis import randbool
from utilis import randcell
from utilis import randcell2
from utilis import sec
from helicopter import Helicopter as Helico
from pynput import keyboard
import time

# 0 - поле 
# 1 - дерево
# 2 - река
# 3 - больница
# 4 - магазин улучшений
#def generate_rivers(): 
#def generate_forest():

CELL_TYPES ='🥮🥦🌊🏥🏨💥⚡️' 
TREE_BONUS = 100
UPGRADE_COST = 5000
LIFE_COST = 1000

class Map:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for i in range(width)] for j in range(height)]
        self.generate_forest(3, 10)
        self.generate_rivers(8)
        self.generate_rivers(8)
        self.generate_rivers(8)
        self.generate_upgrade_shop()
        self.generate_hospital()
    
    def check_bouds(self, x, y): #проверка границ, x and y координаты клетки
        if(x < 0 or y < 0 or x >= self.height or y >= self.width): #такое неочивидное сравнение x с высотой является обоснованным так помимо обычной высоты у нас есть еще рамки 
           return False 
        return True
    
    def print_map(self, helico):
        print('🧇' * (self.width + 2)) #открытие рамки
        for ri in range(self.height):
            print('🧇', end='')
            for ci in range(self.width):
                cell = self.cells[ri][ci]
                if(helico.x == ri and helico.y == ci):
                    print('🚁', end='')   
                elif(cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end='')
            print('🧇')
        print('🧇' * (self.width + 2)) #закрытие рамки  
        
    def generate_rivers(self, l):
        rc = randcell(self.width, self.height)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 0
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if(self.check_bouds(rx2, ry2)):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1
                
              
    def generate_forest(self, r, mxr):
        for ri in range (self.height):
            for ci in range (self.width):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1
                    
    def generate_tree(self): #генерация рандомной индексов клетки в случае если в этой клетки поле туда ставится дерево
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        if(self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1
            
    def generate_upgrade_shop(self):
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4
        
    def generate_hospital(self):
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 4:  #это делается во избежание чтобы функция generate_hospital не перекрыла generate_upgrade_shop
            self.cells[cx][cy] = 3
        else:
            self.generate_hospital()
        
        
        
    
    def add_fire(self): #генерация рандомной индексов клетки в случае если в этой клетки дерево там возникает огонь
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        if(self.cells[cx][cy] == 1):
            self.cells[cx][cy] = 5
    
    def fire_delete(self):
       c = randcell(self.width, self.height)
       cx, cy = c[0], c[1]
       if(self.cells[cx][cy] == 5):
           self.cells[cx][cy] = 0 
           
    def add_lightning(self): #генерация рандомной индексов клетки в случае если в этой клетки дерево там возникает огонь
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        if(self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 6

    def delete_lightning(self):
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        if(self.cells[cx][cy] == 6):
            self.cells[cx][cy] = 0
        
                    
    def process_helicopter(self, helico):
        c = self.cells[helico.x][helico.y]
        d = self.cells[helico.x][helico.y]
        if(c == 2):
            helico.water = helico.maxwater
        if(c == 5 and helico.water > 0):
            helico.water -= 1
            helico.score += TREE_BONUS
            self.cells[helico.x][helico.y] = 1
        if(c == 4 and helico.score >= UPGRADE_COST):
            helico.maxwater += 1
            helico.score -= UPGRADE_COST
        if(c == 3 and helico.score >= LIFE_COST):
            helico.lives += 1000
            helico.score -= LIFE_COST
        if(d == 7):
            helico.lives -= 1
            if (helico.lives == 0):
                helico.game_over()
        
    def export_data(self):
        return {'cells': self.cells}            
    
    def import_data(self, data):
        self.cells = data['cells'] or [[0 for i in range(self.width)] for j in range(self.height)]
    
    
        
            
            
                
                
                
            
    
         







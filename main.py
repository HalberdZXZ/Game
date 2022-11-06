#🌊🌾🏆➕💛🏥🏨🚁💧🧇🌲🥦💥🌳

from map import Map
import time
import os
from helicopter import Helicopter as Helico
from pynput import keyboard
import json

TICK_SLEEP = 0.05
TREE_UPDATE = 50
C_L_UPDATE = 100
FIRE_UPDATE = 10
FIRE_DELETE = 30
ADD_LIGHTNING = 20
DELETE_LIGHTNING = 21
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)

tick = 1
helico = Helico(MAP_W, MAP_H)
MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}
# f - соранение, g - восстановление
  
def proccess_key(key):
    global helico, field, tick
    c = key.char.lower()
    
    #обработка движений вертолета
    if c in MOVES.keys():
        dx, dy  = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
        
    #сохранение игры    
    elif c == 'f':
        data = {'helicopter': helico.export_data(), 
                'field': field.export_data(),
                'tick': tick}
        with open('level.json', 'w') as lvl:
            json.dump(data, lvl)
            
    #загрузка игры
    elif c =='g':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            tick = data['tick'] or 1
            helico.import_data(data['helicopter'])
            field.import_data(data['field'])
        
        
            
        
        
listener = keyboard.Listener(
    on_press=None,
    on_release=proccess_key)
listener.start()



while True:
    os.system('cls')
    field.process_helicopter(helico)
    helico.print_stats()
    field.print_map(helico)
    print('TICK', tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if(tick % TREE_UPDATE == 0):
        field.generate_tree()
    if(tick % FIRE_UPDATE == 0):
        field.add_fire()
    if(tick % FIRE_DELETE == 0):
        field.fire_delete()
    if(tick % ADD_LIGHTNING == 0):
        field.add_lightning()
    if(tick % DELETE_LIGHTNING == 0):
        field.delete_lightning()
from random import randint as rand
import time

def randbool(r, mxr): #функция 
    t = rand(0, mxr)
    return (t <= r)

def randcell(width,height):
    tw = rand(0, width - 1)
    th = rand(0, height - 1)
    return(th, tw)

#0 - наверх, 1 - направо, 2 - вниз, 3 - налево
def randcell2(x, y): #x и y координаты клетки w и h ограничения поля
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = rand(0, 3)
    dx, dy = moves[t][0], moves[t][1]
    return (x + dx, y + dy)


def sec(sec_i):
    sec_i = 0
    while True:
        time.sleep(1)
        sec_i += 1

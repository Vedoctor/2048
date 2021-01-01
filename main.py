import pgzrun as pg
import sys, random
WIDTH = 500
HEIGHT = 500

blocks = []
size = 4

def draw():
    screen.fill('black')
    for block in blocks:
        if block.value == 2:
            block.draw()
        if block.value == 4:
            block.draw()
            block.image = '2048_4'
        if block.value == 8:
            block.draw()
            block.image = '2048_8'
        if block.value == 16:
            block.draw()
            block.image = '2048_16'
        if block.value == 32:
            block.draw()
            block.image = '2048_32'
        if block.value == 64:
            block.draw()
            block.image = '2048_64'



def on_key_down(key):
    if key == keys.ESCAPE:
        sys.exit()

    if key == keys.LEFT:
        move_left()

    if key == keys.RIGHT:
        move_right()

    if key == keys.UP:
        move_up()

    if key == keys.DOWN:
        move_down()

def add_block():
    block = Actor('2048_2')
    posx = 0
    while posx == 0:
        posx, posy = get_available_spot()
    block.posx = posx
    block.posy = posy
    rnd = random.randint(0, 100)
    if rnd < 20:
        block.value = 4
    else:
        block.value = 2
    blocks.append(block)


def get_available_spot():
    posx = random.randint(1, 4)
    posy = random.randint(1, 4)
    for block in blocks:
        if block.posx == posx and block.posy == posy:
            return 0, 0
    return posx, posy


def update():
    for block in blocks:
        block.x = block.posx * 100
        block.y = block.posy * 100

    if len(blocks) == pow(size, 2):
        sys.exit()



def move_left():
    for i in range(size):
        for block in blocks:
            action = can_move(block, 'left')
            if action == 'move' and block.posx != 1:
                block.posx -= 1
            elif action == 'merge':
                block.value += block.value
                block.posx -= 1
    add_block()


def move_right():
    for block in blocks:
        if block.posx != 4:
            block.posx += 1
    add_block()


def move_up():
    for block in blocks:
        if block.posy != 1:
            block.posy -= 1
    add_block()


def move_down():
    for block in blocks:
        if block.posy != 4:
            block.posy += 1
    add_block()


def can_move(block, dir):
    posx = block.posx
    posy = block.posy
    for block2 in blocks:
        if block2.posx == posx - 1 and block2.posy == posy:
            if block2.value == block.value:
                blocks.remove(block2)
                return 'merge'
            return 'nomerge'
    return 'move'


def add_first_blocks():
    block = Actor('2048_2')
    block.posx = random.randint(1, 4)
    block.posy = random.randint(1, 4)
    rnd = random.randint(0, 100)
    if rnd < 20:
        block.value = 4
    else:
        block.value = 2
    blocks.append(block)


add_first_blocks()
pg.go()
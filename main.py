import pgzrun as pg
import sys, random
WIDTH = 500
HEIGHT = 500

blocks = []


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
    block.posx = random.randint(1, 4)
    block.posy = random.randint(1, 4)
    rnd = random.randint(0, 100)
    if rnd < 20:
        block.value = 4
    else:
        block.value = 2
    blocks.append(block)


def update():
    for block in blocks:
        block_pos(block, block.posx, block.posy)


def block_pos(block, posx, posy):
    block.x = posx * 100
    block.y = posy * 100


def move_left():
    for block in blocks:
        if block.posx != 1:
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



add_block()
add_block()

pg.go()
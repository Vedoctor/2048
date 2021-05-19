import pgzrun as pg
import sys, random
WIDTH = 500
HEIGHT = 500

blocks = []
positions = []

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
    block.position = [random.randint(1, 4), 2]
    if len(blocks) != 0:
        for other_block in blocks:
            if other_block.position == block.position:
                add_block()
    rnd = random.randint(1, 100)
    if rnd <= 20:
        block.value = 4
    else:
        block.value = 2
    blocks.append(block)


def update():
    for block in blocks:
        block.pos = block.position[0] * 100, block.position[1] * 100
    update_positions()


def update_positions():
    for block in blocks:
        positions.clear()
        positions.append(block.position)


def move_left():
    for i in range(4):
        for block in blocks:
            for position in positions:
                if block.position[0] - 1 == position[0]:
                    continue
            if block.position[0] != 1:
                block.position[0] -= 1


add_block()
add_block()

pg.go()
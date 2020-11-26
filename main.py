import pgzrun as pg
import sys, random
WIDTH = 500
HEIGHT = 500

blocks = []

pos_list = [50, 150, 250, 350]

def draw():
    screen.fill('black')
    for block in blocks:
        screen.draw.filled_rect(block, 'white')


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
    block = Rect(
        random.choice(pos_list),
        random.choice(pos_list),
        100, 100)
    blocks.append(block)


def update():
    pass


def move_left():
    for block in blocks:
        if block.x != 50:
            block.x -= 100
    add_block()


def move_right():
    for block in blocks:
        if block.x != 350:
            block.x += 100
    add_block()


def move_up():
    for block in blocks:
        if block.y != 50:
            block.y -= 100
    add_block()


def move_down():
    for block in blocks:
        if block.y != 350:
            block.y += 100
    add_block()


add_block()
add_block()
print(blocks)

pg.go()
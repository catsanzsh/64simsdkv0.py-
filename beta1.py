from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()
CSIZE, VIEW = 16, 2        # Chunk size, view distance
seed = random.randint(0,999999)
world = Entity()
loaded = {}

class Voxel(Button):
    def __init__(s, pos=(0,0,0)):
        super().__init__(
            parent=world,
            position=pos,
            model='cube',
            origin_y=0.5,
            texture='white_cube',
            color=color.color(0,0,random.uniform(0.9,1)),
            scale=1,
            collider='box'
        )
    def input(s, k):
        if s.hovered:
            if k == 'right mouse down':
                Voxel(s.position + mouse.normal)
            if k == 'left mouse down':
                destroy(s)

class Chunk(Entity):
    def __init__(s, cx, cz):
        super().__init__()
        random.seed((cx, cz, seed))
        for x in range(CSIZE):
            for z in range(CSIZE):
                h = random.randint(1,5)
                for y in range(h):
                    Voxel((cx*CSIZE + x, y, cz*CSIZE + z))

player = FirstPersonController()
Sky()

def update():
    cx, cz = int(player.x // CSIZE), int(player.z // CSIZE)
    for dx in range(-VIEW, VIEW+1):
        for dz in range(-VIEW, VIEW+1):
            key = (cx+dx, cz+dz)
            if key not in loaded:
                loaded[key] = Chunk(cx+dx, cz+dz)

app.run()

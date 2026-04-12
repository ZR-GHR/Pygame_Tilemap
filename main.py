import pygame as pg
from modules.player import Player
from modules.tilemap import TileMap

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Tilemap Platformer")
clock = pg.time.Clock()

tilemap = TileMap(tile_size = 32)
try:
    tilemap.load_from_file("tilemap.json")
except FileNotFoundError:
    print("Создайте карту в редакторе сначала!")
    tilemap.map_data = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2],
        [1, 1, 1, 1, 1, 1, 3, 3, 3, 4, 4, 3, 3, 3, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 3, 3, 3, 4, 4, 3, 3, 3, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1]
    ]
    tilemap.width = 20
    tilemap.height = 15

    player =Player(100, 300)

    camera_x = 0
    camera_y = 0

    running = True
    while running:
        dr = clock.tick(60) / 1000.0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
            if event.tupe == pg.KEYDOWN:
                if event.key == pg.K_r and not player.alive:
                    player = Player(100, 300)
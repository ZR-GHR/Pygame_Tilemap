import pygame as pg

class TileEditor:

    def __init__(self, width, height, tile_size):
        self.width = width
        self.height = height
        self.tile_size = tile_size

        # пустая карта
        self.map_data = [[0 for _ in range(width)] for _ in range(height)]

        # текущий выбраггый тайл

        self.current_tile = 1

        # смещение карты на экране

        self.offset_x = 150
        self.offset_y = 60

        # цвета тайлов
        self.tile_colors = {
            0: (50, 50 ,50),

            1: (139, 69, 19),

            2: (0, 200, 0),

            3: (100, 100, 100),

            4: (0, 100, 255)
        }
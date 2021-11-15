from Class.TileHint import TileHint
from Helper.Command import Command
from random import sample

class Grid:
    
    MIN_SIZE = 5
    MAX_SIZE = 15

    MINES_PERCENT = 10

    def __init__(self):
        self.command = Command()

        self.initSizes()
        self.initTileHints()
        self.initTileMinesCoords()

    def initTileMinesCoords(self):
        self.tile_mines_coords = tuple()
        for tile_hint in self.tile_hints:
            self.tile_mines_coords = self.tile_mines_coords + (tile_hint.x, tile_hint.y)

        mines_number = round(self.MINES_PERCENT / 100 * len(self.tile_hints))
        print(self.tile_mines_coords)
        # self.tile_mines_coords = sample(self.tile_mines_coords, mines_number)

    def initSizes(self):
        self.height = self.command.askGridSize('Veuillez entrer la hauteur de la grille (entre ' + str(self.MIN_SIZE) + ' et ' + str(self.MAX_SIZE) + ') : ', self)
        self.width = self.command.askGridSize('Veuillez entrer la largeur de la grille (entre ' + str(self.MIN_SIZE) + ' et ' + str(self.MAX_SIZE) + ') : ', self)

    def initTileHints(self):
        self.tile_hints = []
        for x in range(1, self.width + 1):
            for y in range(1, self.height + 1):
                self.tile_hints.append(TileHint(self, x, y))
from Class.TileHint import TileHint
from Class.TileMine import TileMine
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
        self.initTileMines()

    def __str__(self) -> str:
        string = '\n'
        for key, tile in enumerate(self.tiles):
            string = string + str(tile)
            if (key + 1) % self.width == 0:
                string = string + '\n'
        
        return string

    def getTile(self, x, y):
        for tile in self.tiles:
            if tile.x == x and tile.y == y:
                return tile

    def initTileMines(self):
        for key, tile in enumerate(self.tiles):
            for tile_mines_coord in self.tile_mines_coords:
                if tile.x == tile_mines_coord[0] and tile.y == tile_mines_coord[1]:
                    self.tiles[key] = TileMine(self, tile.x, tile.y)
            tile.hint = None # Permet de calculer le nombre de bombes autour de chaque tile

    def initTileMinesCoords(self):
        self.tile_mines_coords = []
        for tile in self.tiles:
            self.tile_mines_coords.append((tile.x, tile.y))

        mines_number = round(self.MINES_PERCENT / 100 * len(self.tiles))
        self.tile_mines_coords = sample(self.tile_mines_coords, mines_number)

    def initSizes(self):
        self.height = self.command.askGridSize('Veuillez entrer la hauteur de la grille (entre ' + str(self.MIN_SIZE) + ' et ' + str(self.MAX_SIZE) + ') : ', self)
        self.width = self.command.askGridSize('Veuillez entrer la largeur de la grille (entre ' + str(self.MIN_SIZE) + ' et ' + str(self.MAX_SIZE) + ') : ', self)

    def initTileHints(self):
        self.tiles = []
        for x in range(1, self.width + 1):
            for y in range(1, self.height + 1):
                self.tiles.append(TileHint(self, x, y))
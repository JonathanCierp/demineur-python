from Class.PlayerHuman import PlayerHuman
from Class.TileHint import TileHint
from Class.TileMine import TileMine
from random import sample

class Grid:
    
    MIN_SIZE = 5
    MAX_SIZE = 15

    MINES_PERCENT = 10

    def __init__(self):
        self.player_human = PlayerHuman()

        self.initSizes()
        self.initTileHints()
        self.tile_mines_coords = []
        self.remaining = len(self.tiles)

    def __str__(self) -> str:
        string = '\nRestant: ' + str(self.remaining) + '\n\n '
        # Indicateurs Colonnes
        for i in range(1, self.width + 1, 1):
            string = string + ' ' + str(i)
        string = string + '\n'

        # Grille
        i = 1
        for key, tile in enumerate(self.tiles):
            if (key + 1) % self.width == 1:
                string = string + str(i)# Indicateur ligne
                i += 1

            string = string + ' ' + str(tile) # Tile
            
            if (key + 1) % self.width == 0:
                string = string + '\n' # Nouvelle ligne
        
        return string

    def openFull(self, tile):
        # Pour chaque tuile autour de celle-ci on les ouvre si ce n'est pas une bombe, si elle n'est pas ouverte mais aussi si son indice est de 0
        for tileAround in tile.tilesAround:
            tileAround = self.getTile(tileAround[0], tileAround[1])
            if isinstance(tileAround, TileHint):
                if not tileAround.opened:
                    tileAround.open()
                    self.remaining -= 1
        

    def open(self, x: int, y: int):
        tile = self.getTile(x, y)
        if tile.opened:
            print('Case déjà ouverte !')
            return
        elif tile.flagged:
            print('Case drapeau !')
            return

        tile.open()
        
        if isinstance(tile, TileMine):
            return

        self.remaining -= 1

    def toggleFlag(self, x: int, y: int):
        tile = self.getTile(x, y)
        if tile.opened:
            print('Case déjà ouverte !')
            return
        
        if tile.flagged:
            tile.flagged = False
        else:
            tile.flagged = True

    def getTile(self, x: int, y: int):
        for tile in self.tiles:
            if tile.x == x and tile.y == y:
                return tile

    def initTileMines(self, first_open_coords):
        self.initTileMinesCoords(first_open_coords)
        for key, tile in enumerate(self.tiles):
            for tile_mines_coord in self.tile_mines_coords:
                if tile.x == tile_mines_coord[0] and tile.y == tile_mines_coord[1]:
                    self.tiles[key] = TileMine(self, tile.x, tile.y)
        
        for tile in self.tiles:
            if isinstance(tile, TileHint):
                tile.hint = None # Permet de calculer le nombre de bombes autour de chaque tile
        
        self.remaining = len(self.tiles) - len(self.tile_mines_coords)

    def initTileMinesCoords(self, first_open_coords):
        self.tile_mines_coords = []
        for tile in self.tiles:
            self.tile_mines_coords.append((tile.x, tile.y))

        mines_number = round(self.MINES_PERCENT / 100 * len(self.tiles))
        self.tile_mines_coords = sample(self.tile_mines_coords, mines_number)
        
        # Empeche la mine de spawn au même endroit que la première ouverture
        if first_open_coords in self.tile_mines_coords:
            self.initTileMinesCoords(first_open_coords)

    def initSizes(self):
        self.height = self.player_human.askGridSize('Veuillez entrer la hauteur de la grille (entre ' + str(self.MIN_SIZE) + ' et ' + str(self.MAX_SIZE) + ') : ', self)
        self.width = self.player_human.askGridSize('Veuillez entrer la largeur de la grille (entre ' + str(self.MIN_SIZE) + ' et ' + str(self.MAX_SIZE) + ') : ', self)

    def initTileHints(self):
        self.tiles = []
        for y in range(1, self.height + 1):
            for x in range(1, self.width + 1):
                self.tiles.append(TileHint(self, x, y))
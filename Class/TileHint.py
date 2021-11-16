from Class.Tile import Tile
from Class.TileMine import TileMine

class TileHint(Tile):
    
    def __init__(self, grid, x: int, y: int, opened: bool = False, flagged: bool = False):
        super().__init__(grid, x, y, opened, flagged)
        self._hint = None
        self.tilesAround = [
            (self.x - 1, self.y - 1),
            (self.x, self.y - 1),
            (self.x + 1, self.y - 1),
            (self.x + 1, self.y),
            (self.x + 1, self.y + 1),
            (self.x, self.y + 1),
            (self.x - 1, self.y + 1),
            (self.x - 1, self.y),
        ]

    def __str__(self) -> str:
        if not self.opened:
            return super().__str__()
        
        elif self.hint == 0:
            return '0'

        return str(self.hint)

    @property
    def hint(self):
        return self._hint

    @hint.setter
    def hint(self, hint):
        if self._hint != None:
            return

        hint = 0
        for tileAround in self.tilesAround:
            tile = self.grid.getTile(tileAround[0], tileAround[1])
            if isinstance(tile, TileMine):
                hint = hint + 1
        self._hint = hint
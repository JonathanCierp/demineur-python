from Class.Tile import Tile
from Class.TileMine import TileMine

class TileHint(Tile):
    
    def __init__(self, grid, x: int, y: int, opened: bool = False, flagged: bool = False):
        super().__init__(grid, x, y, opened, flagged)
        self._hint = None

    def __str__(self) -> str:
        if not self.opened:
            return super().__str__()
        
        elif self._hint == 0:
            return '0'

        return str(self._hint)

    @property
    def hint(self):
        return self._hint

    @hint.setter
    def hint(self, hint):
        if self._hint != None:
            return

        hint = 0
        tilesToCheck = [
            (self.x - 1, self.y - 1),
            (self.x, self.y - 1),
            (self.x + 1, self.y - 1),
            (self.x + 1, self.y),
            (self.x + 1, self.y + 1),
            (self.x, self.y + 1),
            (self.x - 1, self.y + 1),
            (self.x - 1, self.y),
        ]
        for tileToCheck in tilesToCheck:
            tile = self.grid.getTile(tileToCheck[0], tileToCheck[1])
            if isinstance(tile, TileMine):
                hint = hint + 1
        self._hint = hint
from Class.Tile import Tile

class TileHint(Tile):
    
    def __init__(self, grid, x: int, y: int, opened: bool = False, flagged: bool = False):
        super().__init__(grid, x, y, opened, flagged)
        self.hint = 0

    def __str__(self) -> str:
        if not self.opened:
            return super().__str__()
        
        elif self.hint == 0:
            return '0'

        else:
            return str(self.hint)
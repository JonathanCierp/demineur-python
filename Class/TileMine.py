from Class.Tile import Tile

class TileMine(Tile):
    
    def __init__(self, grid, x: int, y: int, opened: bool = False, flagged: bool = False):
        super().__init__(grid, x, y, opened, flagged)

    def __str__(self) -> str:
        if not self.opened:
            return super().__str__()

        elif self.opened:
            return 'B'
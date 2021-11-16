class Tile:
    
    def __init__(self, grid, x: int, y: int, opened: bool = False, flagged: bool = False):
        self.grid = grid
        self.x = x
        self.y = y
        self.opened = opened
        self.flagged = flagged

    def __str__(self) -> str:
        if self.flagged:
            return 'F'
        
        elif not self.opened:
            return '#'

        raise NotImplementedError
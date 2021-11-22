from Class.Grid import Grid
from Class.PlayGame import PlayGame
from Class.TileMine import TileMine
from Class.PlayerHuman import PlayerHuman

class MineSweeper:

    FLAG = 'F'
    OPEN = 'O'
    HELP = 'help'
    NEW_GAME = 'new game'
    QUIT = 'quit'

    def __init__(self):
        self.player_human = PlayerHuman(self)
        self.play_game = PlayGame(self, self.player_human)

    def isPlaying(self):
        if not self.game_over and not self.isWon() and not self.isLost():
            return True

        return False

    def isWon(self):
        if self.grid.remaining == 0:
            return True
        
        return False

    def isLost(self):
        for tile in self.grid.tiles:
            if isinstance(tile, TileMine) and tile.opened:
                return True
        
        return False

    def quit(self):
        self.game_over = True

    def newGame(self):
        print('Nouvelle partie !')
        self.game_over = False
        self.need_init_mines = True
        self.grid = Grid()
        self.play_game.run()

    def open(self, x: int, y: int):
        self.checkCoords(x, y)
        
        if self.need_init_mines:
            self.grid.initTileMines((x, y))
            self.need_init_mines = False

        self.grid.open(x, y)

        if self.isWon():
            self.game_over = True
            print(str(self.grid))
            print('\nGagné !')

        if self.isLost():
            self.game_over = True
            print(str(self.grid))
            print('\nPerdu !')


    def flag(self, x: int, y: int):
        self.checkCoords(x, y)

        self.grid.toggleFlag(x, y)

    def checkCoords(self, x: int, y: int):
        if x <= 0 or x > self.grid.width or y <= 0 or y > self.grid.height:
            print('\nMauvaises coordonnées !')
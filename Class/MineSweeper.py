from Class.Grid import Grid
from Class.TileMine import TileMine
from Helper.Command import Command

class MineSweeper:

    FLAG = 'F'
    OPEN = 'O'
    HELP = 'help'
    NEW_GAME = 'new game'
    QUIT = 'quit'

    def __init__(self):
        self.command = Command()

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

    def newGame(self):
        print('Here is a new Game !')
        self.game_over = False
        self.grid = Grid()
        self.play()

    def open(self, x: int, y: int):
        self.checkCoords(x, y)

        self.grid.open(x, y)

        if self.isWon():
            raise Exception('Game is won !')

        if self.isLost():
            raise Exception('Game is lost !')


    def flag(self, x: int, y: int):
        self.checkCoords(x, y)

        self.grid.toggleFlag(x, y)
    
    def play(self):
        while not self.game_over :
            print(str(self.grid))
            answer = self.command.askAction('Entrez une commande (help pour la liste des commandes) : ', self)

    def checkCoords(self, x: int, y: int):
        if self.game_over:
            raise Exception('GameOver !')
        elif x <= 0 or x > self.grid.width or y <= 0 or y > self.grid.height:
            raise Exception('Mauvaises coordonnées !')
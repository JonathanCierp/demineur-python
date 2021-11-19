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
        print('Nouvelle partie !')
        self.game_over = False
        self.grid = Grid()
        self.play()

    def open(self, x: int, y: int):
        self.checkCoords(x, y)

        self.grid.open(x, y)

        if self.isWon():
            print('\nGagné !')
            self.game_over = True

        if self.isLost():
            print('\nPerdu !')
            self.game_over = True


    def flag(self, x: int, y: int):
        self.checkCoords(x, y)

        self.grid.toggleFlag(x, y)
    
    def play(self):
        while not self.game_over :
            print(str(self.grid))
            answer = self.command.askAction('Entrez une commande (help pour la liste des commandes) : ', self)

    def checkCoords(self, x: int, y: int):
        if x <= 0 or x > self.grid.width or y <= 0 or y > self.grid.height:
            print('\nMauvaises coordonnées !')
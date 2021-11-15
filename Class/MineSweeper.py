from Class.Grid import Grid
from Helper.Command import Command

class MineSweeper:

    FLAG = 'F'
    OPEN = 'O'
    HELP = 'help'
    NEW_GAME = 'new game'
    QUIT = 'quit'

    def __init__(self):
        self.command = Command()

        self.is_playing = False
        self.game_over = False

    def newGame(self):
        print('Here is a new Game !')
        self.is_playing = True
        self.game_over = False
        self.grid = Grid()
        self.play()

    def open(self, x, y):
        if not self.is_playing:
            raise Exception('Playing is false !')

        print('Open - cell x: ' + x + ', y:' + y)


    def flag(self, x, y):
        if not self.is_playing:
            raise Exception('Playing is false !')

        print('Flag - cell x: ' + x + ', y:' + y)
    
    def play(self):
        while not self.game_over :
            answer = self.command.askAction('Entrez une commande (help pour la liste des commandes) : ', self)
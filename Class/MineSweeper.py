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

    def open(self, x: int, y: int):
        if not self.is_playing:
            raise Exception('Playing is false !')
        elif x <= 0 or x > self.grid.width or y <= 0 or y > self.grid.height:
            raise Exception('Mauvaises coordonnées !')

        self.grid.open(x, y)
        print('Open - cell x: ' + str(x) + ', y:' + str(y))


    def flag(self, x: int, y: int):
        if not self.is_playing:
            raise Exception('Playing is false !')

        print('Flag - cell x: ' + str(x) + ', y:' + str(y))
    
    def play(self):
        while not self.game_over :
            print(str(self.grid))
            answer = self.command.askAction('Entrez une commande (help pour la liste des commandes) : ', self)
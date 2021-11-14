from Helper.Command import Command

class MineSweeper:

    def __init__(self):
        print('Hi, I\'m MineSweeper Class')
        self.command = Command(self)
        self.is_playing = False
        self.game_over = False

    def newGame(self):
        print('Here is a new Game !')
        self.is_playing = True

    def open(self, x, y):
        if not self.is_playing:
            raise Exception('Playing is false !')

        print('open cell x: ' + x + ' y:' + y)


    def flag(self, x, y):
        if not self.is_playing:
            raise Exception('Playing is false !')

        print('flag cell x: ' + x + ' y:' + y)
    
    def play(self):
        while not self.game_over :
            answer = self.command.prompt('Entrez une commande (help pour la liste des commandes) : ')
            #answer = doCommad(prompt('Entrez une command (help pour la liste des commandes) : '))
            answer = answer.split(' ')
            action = answer[0]
            line = answer[1]
            column = answer[2]
            print('Action : ' + action)
            print('Ligne : ' + line)
            print('Colonne : ' + column)
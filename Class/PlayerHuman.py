from Helper.input import prompt
from Class.Player import Player
from Class.MineSweeper import MineSweeper
from Class.ActionNewGame import ActionNewGame
from Class.ActionQuit import ActionQuit
from Class.ActionOpen import ActionOpen
from Class.ActionFlag import ActionFlag

class PlayerHuman(Player):

    FLAG = 'F'
    OPEN = 'O'
    HELP = 'help'
    NEW_GAME = 'new game'
    QUIT = 'quit'

    def __init__(self, mine_sweeper: MineSweeper) -> None:
        self.mine_sweeper = mine_sweeper
    
    def getAction(self):
        message = 'Entrez une commande (help pour la liste des commandes) : '
        action = prompt(message)

        if action == self.HELP:
            print('    - ' + self.FLAG + ' <X> <Y> (mettre un drapeau dans une case)')
            print('    - ' + self.OPEN + ' <X> <Y> (ouvir une case)')
            print('    - ' + self.NEW_GAME + ' (commence une nouvelle partie)')
            print('    - ' + self.QUIT + ' (quitter la partie)')
            return self.getAction(message) # Rappelle cette fonction après le 'help' afin de reposer la question à l'utilisateur

        elif action == self.NEW_GAME:
            return ActionNewGame()

        elif action == self.QUIT:
            return ActionQuit()
        
        elif action[0] == self.FLAG or action[0] == self.OPEN:
            action = action.split(' ')
            if len(action) < 3:
                print('Veuillez entrer une commande valide !')
                return self.getAction(message) # Rappelle cette fonction si l'utilisateur a rentré n'importequoi
            if not action[1].isdigit() or not action[2].isdigit():
                print('Veuillez entrer des nombres !')
                return self.getAction(message) # Rappelle cette fonction si l'utilisateur a rentré n'importequoi
            if action[0] == self.OPEN:
                return ActionOpen((int(action[1]), int(action[2])))
            elif action[0] == self.FLAG:
                return ActionFlag((int(action[1]), int(action[2])))

        else:
            print('Veuillez entrer une commande valide !')
            return self.getAction(message) # Rappelle cette fonction si l'utilisateur a rentré n'importequoi

    def gameOver(self):
        self.mine_sweeper.game_over = True
        print(str(self.mine_sweeper.grid))
        print('\nPerdu !')
from Class.MineSweeper import MineSweeper
from Class.Player import Player
from Helper.Command import Command

class PlayGame:
    
    def __init__(self, mine_sweepper: MineSweeper, player: Player):
        self.command = Command()
        self.mine_sweepper = mine_sweepper
        self.player = player

    def run(self):
        while not self.mine_sweepper.game_over :
            print(str(self.mine_sweepper.grid))
            answer = self.command.askAction('Entrez une commande (help pour la liste des commandes) : ', self)
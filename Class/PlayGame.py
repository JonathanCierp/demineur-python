from Class.Player import Player

class PlayGame:
    
    def __init__(self, mine_sweepper, player: Player):
        self.mine_sweepper = mine_sweepper
        self.player = player

    def run(self):
        while not self.mine_sweepper.game_over :
            print(str(self.mine_sweepper.grid))
            answer = self.player.getAction()
from Class.Action import Action

class ActionOpen(Action):

    def action(self, coords: tuple):
        self.mine_sweeper.open(coords[0], coords[1])

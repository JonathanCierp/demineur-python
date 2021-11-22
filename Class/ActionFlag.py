from Class.Action import Action

class ActionFlag(Action):

    def action(self, coords: tuple):
        self.mine_sweeper.flag(coords[0], coords[1])
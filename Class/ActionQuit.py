from Class.Action import Action

class ActionQuit(Action):

    def action(self):
        self.mine_sweeper.quit()
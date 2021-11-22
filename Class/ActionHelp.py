from Class.Action import Action

class ActionHelp(Action):

    def action(self):
        print('    - ' + self.FLAG + ' <X> <Y> (mettre un drapeau dans une case)')
        print('    - ' + self.OPEN + ' <X> <Y> (ouvir une case)')
        print('    - ' + self.NEW_GAME + ' (commence une nouvelle partie)')
        print('    - ' + self.QUIT + ' (quitter la partie)')
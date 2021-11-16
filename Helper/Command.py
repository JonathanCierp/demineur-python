from Helper.input import prompt

class Command():

    FLAG = 'F'
    OPEN = 'O'
    HELP = 'help'
    NEW_GAME = 'new game'
    QUIT = 'quit'

    def askAction(self, message, mine_sweeper):
        action = prompt(message)

        if action == self.HELP:
            print('    - ' + self.FLAG + ' <X> <Y> (put a flag in a cell)')
            print('    - ' + self.OPEN + ' <X> <Y> (open a cell)')
            print('    - ' + self.NEW_GAME + ' (begin a new game)')
            print('    - ' + self.QUIT + ' (leave the game)')
            return self.askAction(message, mine_sweeper) # Rappelle cette fonction après le 'help' afin de reposer la question à l'utilisateur

        elif action == self.NEW_GAME:
            mine_sweeper.newGame()

        elif action == self.QUIT:
            mine_sweeper.quit()
        
        elif action[0] == self.FLAG or action[0] == self.OPEN:
            action = action.split(' ')
            if not action[1].isdigit() or not action[2].isdigit():
                print('Veuillez entrer des nombres !')
                return self.askAction(message, mine_sweeper) # Rappelle cette fonction si l'utilisateur a rentré n'importequoi
            if action[0] == self.FLAG:
                mine_sweeper.flag(action[1], action[2])
            elif action[0] == self.OPEN:
                mine_sweeper.open(action[1], action[2])

        else:
            print('Veuillez entrer une commande valide !')
            return self.askAction(message, mine_sweeper) # Rappelle cette fonction si l'utilisateur a rentré n'importequoi

    def askGridSize(self, message, grid):
        grid_size = prompt(message)

        if not grid_size.isdigit():
            print('Veuillez entrer un nombre !')
            return self.askGridSize(message, grid) # Rappelle cette fonction si l'utilisateur a rentré n'importequoi
        
        elif int(grid_size) < grid.MIN_SIZE or int(grid_size) > grid.MAX_SIZE:
            print('Veuillez entrer un nombre valide !')
            return self.askGridSize(message, grid) # Rappelle cette fonction si l'utilisateur a rentré n'importequoi

        return int(grid_size)
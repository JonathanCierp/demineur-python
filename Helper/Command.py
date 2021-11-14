class Command():

    HELP = 'help'
    NEW_GAME = 'new game'
    QUIT = 'quit'

    def __init__(self, mine_sweeper):
        self.mine_sweeper = mine_sweeper

    def prompt(self, message):
        prompt = input(message)

        while prompt == '':
            prompt = input(message)

        if prompt == self.HELP:
            print('- F <LINE> <COLUMN> (put a flag in a box)')
            print('- O <LINE> <COLUMN> (open a box)')
            print('- new game (begin a new game)')
            print('- quit (leave the game)')
            self.prompt(message) # Rappelle cette fonction après le 'help' afin de reposer la question à l'utilisateur

        if prompt == self.NEW_GAME:
            self.mine_sweeper.newGame()

        if prompt == self.QUIT:
            self.mine_sweeper.quit()

        return prompt
def prompt(message):
    prompt = input(message)

    while prompt == '':
        prompt = input(message)

    return prompt

class Command():

    def __init__(self, command_name :str):
        self.command_name = str(command_name)

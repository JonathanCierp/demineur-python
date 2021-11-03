def prompt(message):
    prompt = input(message)

    while prompt == '':
        prompt = input(message)
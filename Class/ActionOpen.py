from Class.Action import Action

class ActionOpen(Action):
    
    def __init__(self, coords: tuple):
        self.coords = coords
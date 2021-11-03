
from Helper.input import prompt

def main():
    grid_height = prompt('Veuillez entrer la hauteur de la grille (entre 5 et 15) : ')
    grid_width = prompt('Veuillez entrer la largeur de la grille (entre 5 et 15) : ')
    play()
    print(grid_height)
    print(grid_width)

if __name__ == '__main__':
    main()


def play():
    game_over = False
    while not game_over :
        askAction()


def askAction():
    return prompt('Entrez une command (help pour la liste des commandes)')
    #doCommad(prompt('Entrez une command (help pour la liste des commandes)'))

from Helper.input import prompt

def main():
    gridSize = prompt('Veuillez entrer la hauteur de la grille (entre 5 et 15) : ')

    action = prompt('Veuillez entrer l\'action(O pour ouvir ou D pour mettre un drapeau) : ')
    x = prompt('Veuillez entrer le numéro de la colonne : ')
    y = prompt('Veuillez entrer le numéro de la ligne : ')

    if action == 'O':
        print(f'O en {x} {y}')
    elif action == 'D':
        print(f'D en {x} {y}')

if __name__ == '__main__':
    main()
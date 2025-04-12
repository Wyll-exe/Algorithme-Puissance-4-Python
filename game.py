import os

class TicTacToe():

    def __init__(self, nl=6, nc=7, token=('@', 'X')):
        # Créer la grille et lance une nouvelle partie
        self.nl = nl
        self.nc = nc
        self.token = token
        self.board = [['.' for i in range(nc)] for j in range(nl)]
        self.new_game(self.nl, self.nc, self.token)

    def __str__(self):
        # Affiche la grille de jeu
        board_str = ' '.join([str((i+1) % 10) for i in range(self.nc)]) + '\n'
        for i in range(self.nl):
            board_str += ' '.join(self.board[i]) + '\n'
        return board_str

    def coup(self, joueur, colonne):
        """ Joue le coup du joueur dans la colonne choisie. """
        board_colonne = [ligne[colonne] for ligne in self.board]
        ligne = board_colonne.count('.')
        if ligne == 0:
            return False, 0
        else:
            ligne = ligne - 1
            self.board[ligne][colonne] = self.token[joueur-1]
            return True, ligne

    def check_victoire(self, ligne, colonne, joueur):
        """ Vérifie si le dernier coup joué permet de gagner. """
        pattern = self.token[joueur-1] * 4

        # Vérification colonne
        if pattern in ''.join([l[colonne] for l in self.board]):
            return True

        # ligne
        if pattern in ''.join(self.board[ligne]):
            return True

        # diagonale nord-ouest -> sud-est
        diag1 = []
        for k in range(self.nl):
            try:
                char = self.board[k][(colonne-ligne+k)]
            except IndexError:
                pass
            else:
                diag1.append(char)
        if pattern in ''.join(diag1):
            return True

        # diagonale sud-ouest -> nord-est
        diag2 = []
        for k in range(self.nl):
            try:
                char = self.board[k][(colonne+ligne-k)]
            except IndexError:
                pass
            else:
                diag2.append(char)
        if pattern in ''.join(diag2):
            return True

        return False

    def computer_play(self):
        """ Logique de l'ordinateur pour jouer. """
        # Vérifie si l'ordinateur peut gagner
        for col in range(self.nc):
            for ligne in range(self.nl):
                if self.board[ligne][col] == ".":
                    if self.check_victoire(ligne, col, 2):
                        return True

        # Sinon, bloque le joueur humain
        return False

    def new_game(self, nl=6, nc=7, token=('@', 'X')):
        os.system('clear')
        print(self)

        victoire = False
        compteur = 0

        while not victoire and compteur < nc * nl:
            compteur += 1
            joueur = (compteur + 1) % 2 + 1

            if joueur == 1:  # Joueur humain
                while True:
                    print(f"Joueur {joueur} ({self.token[joueur-1]}), C'EST TON TOUR !")
                    colonne = input('Colonne jouée: ')
                    if colonne not in {str(i+1) for i in range(self.nc)}:
                        os.system('clear')
                        print("IMPOSSIBLE DE METTRE CE COUP")
                        print(f"TU DOIS METTRE UN CHIFFRE ENTRE 1 ET {self.nc}!")
                        print(self)
                        continue
                    colonne = int(colonne) - 1
                    coupvalide, ligne = self.coup(joueur, colonne)
                    if not coupvalide:
                        print(f"PLUS DE PLACE : {colonne+1}")
                        print(self)
                        continue
                    break
            else:  # Joueur ordinateur
                print(f"Joueur {joueur} ({self.token[joueur-1]}), L'ORDINATEUR JOUE ..")
                for col in range(self.nc):
                    coupvalide, ligne = self.coup(joueur, col)
                    if coupvalide:
                        break

            os.system('clear')
            print(self)

            if compteur > 6:  # Vérification à partir du 7ème coup
                victoire = self.check_victoire(ligne, colonne, joueur)

        if victoire:
            print(f"C'est terminé .. le Joueur {joueur} ({self.token[joueur-1]}) a gagné !")
        else:
            print("EX-AEQUO !")


if __name__ == '__main__':
    TicTacToe()
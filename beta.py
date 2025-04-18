class TicTacToe():
    def __init__(self, nl=6, nc=7, token=('@', 'X')):
        self.nl = nl
        self.nc = nc
        self.token = token
        self.board = [['.' for i in range(nc)] for j in range(nl)]
        self.new_game(self.nl, self.nc, self.token)

    def __str__(self):
        board_str = ' '.join([str((i+1) % 10) for i in range(self.nc)]) + '\n'
        for i in range(self.nl):
            board_str += ' '.join(self.board[i]) + '\n'
        return board_str

    def coup(self, joueur, colonne):
        board_colonne = [ligne[colonne] for ligne in self.board]
        ligne = board_colonne.count('.')
        if ligne == 0:
            return False, 0
        else:
            ligne -= 1
            self.board[ligne][colonne] = self.token[joueur-1]
            return True, ligne

    def check_victoire(self, ligne, colonne, joueur):
        pattern = self.token[joueur-1] * 4

        if pattern in ''.join([l[colonne] for l in self.board]):
            return True
        if pattern in ''.join(self.board[ligne]):
            return True

        diag1 = []
        for k in range(self.nl):
            try:
                char = self.board[k][(colonne-ligne+k)]
                diag1.append(char)
            except IndexError:
                pass
        if pattern in ''.join(diag1):
            return True

        diag2 = []
        for k in range(self.nl):
            try:
                char = self.board[k][(colonne+ligne-k)]
                diag2.append(char)
            except IndexError:
                pass
        if pattern in ''.join(diag2):
            return True

        return False

    # 
    def case_value(self, x, y, joueur):
        if self.board[y][x] != '.':
            return 0
        valeur = 0
        directions = [(1,0), (0,1), (1,1), (1,-1)]
        for dx, dy in directions:
            count = self.count_alignement(x, y, dx, dy, joueur)
            valeur += count ** 2
            if count + 1 >= 4:
                valeur += 100  # Bonus si ça aligne 4
        # Bonus si la case est centrale
        centre = self.nc // 2
        valeur += max(0, centre - abs(x - centre))
        return valeur

    # 
    def count_alignement(self, x, y, dx, dy, joueur):
        compteur = 0
        token = self.token[joueur-1]

        i = 1
        while self.case_valide(x + i*dx, y + i*dy) and self.board[y + i*dy][x + i*dx] == token:
            compteur += 1
            i += 1

        i = 1
        while self.case_valide(x - i*dx, y - i*dy) and self.board[y - i*dy][x - i*dx] == token:
            compteur += 1
            i += 1

        return compteur

    # validation
    def case_valide(self, x, y):
        return 0 <= x < self.nc and 0 <= y < self.nl

    # ordinateur
    def computer_play(self):
        max_val = -1
        best_col = None
        for x in range(self.nc):
            for y in range(self.nl-1, -1, -1):
                if self.board[y][x] == '.':
                    val = self.case_value(x, y, 2)
                    # Simulation blocage joueur 
                    val += self.case_value(x, y, 1) * 2
                    if val > max_val:
                        max_val = val
                        best_col = x
                    break  # on ne peut jouer que sur la première case vide de la colonne
        if best_col is not None:
            self.coup(2, best_col)

    def new_game(self, nl=6, nc=7, token=('@', 'X')):
        print('\n' + '-'*30 + '\n')
        print(self)

        victoire = False
        compteur = 0

        while not victoire and compteur < nc * nl:
            compteur += 1
            joueur = (compteur + 1) % 2 + 1

            if joueur == 1:  # Joueur
                while True:
                    print(f"Joueur {joueur} ({self.token[joueur-1]}), C'EST TON TOUR !")
                    colonne = input('Colonne jouée: ')
                    if colonne not in {str(i+1) for i in range(self.nc)}:
                        print('\n' + '-'*30 + '\n')
                        print("COUP INVALIDE")
                        print(self)
                        continue
                    colonne = int(colonne) - 1
                    coupvalide, ligne = self.coup(joueur, colonne)
                    if not coupvalide:
                        print('\n' + '-'*30 + '\n')
                        print(f"PLUS DE PLACE DANS LA COLONNE {colonne+1}")
                        print(self)
                        continue
                    break
            else:  # Ordinateur
                print(f"Joueur {joueur} ({self.token[joueur-1]}) - L'ORDINATEUR JOUE ..")
                self.computer_play()
                ligne = next((i for i in range(self.nl) if self.board[i][colonne] != '.'), self.nl - 1)

            print('\n' + '-'*30 + '\n')
            print(self)

            if compteur > 6:
                victoire = self.check_victoire(ligne, colonne, joueur)

        if victoire:
            print(f"Victoire du Joueur {joueur} ({self.token[joueur-1]}) !")
        else:
            print("MATCH NUL")

if __name__ == '__main__':
    TicTacToe()
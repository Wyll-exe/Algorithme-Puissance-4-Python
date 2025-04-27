
## Puissance 4

### Questions

> **Question 1** :<br/>
> Quelle est la structure de données qui vous paraît la plus adaptée à la représentation du problème ? Expliquez pourquoi et décrivez quelle information devrait contenir chaque élément de cette structure.

**Réponse :**

On possède une fonction qui donne un nombre a chaque case.
Le coup doit être dans la diagonale ou la ligne ou la colonne d'un autre jeton et plus il y de jetons appartenant au joueur a dans la meme ligne/colonne/diagonale mieux c'est. Il faut aussi éviter que le joueur adverse puisse aligner 4 jetons, cette problématique est la priorité. Moins le jeton est placé proche d'un bord mieux c'est.
Après ces calculs une valeur est attribué a chaque case, plus elle est élevée meilleur c'est.


Si la case comprends déjà un jeton alors sa valeur est 0.
On assigne une valeur a chaque case en fonction de toutes les possibilités qu'elle offre. Plus la valeur est élevée plus la case offre de possibilités.
Les cases qui permettent a l'adversaire d'aligner plusieurs jetons augmentent en valeur, la valeur passe au maximum si la case permet d'aligner 4 jetons.
retourner la case avec la valeur la plus haute.
On simule l'action de l'adversaire, il va jouer en priorité sur les cases avec la moins grosse valeur pour nous car ce sont les cases avec la plus grosse valeur pour lui.
On refais les calculs a chaque fois qu'un jeton est joué.


> **Question 2** :<br/>
> Ecrivez l'algorithme qui permet de résoudre le problème. Comme dans le documenet **Arbres.md**, cous pourrez éventuellemnt décomposer l'algorithme en pseudo-fonctions qui rendront les choses plus simples. Le pseudo-code peut être rédigé en « langue naturelle » — le français, l'anglais, etc. — mais doit respecter un niveau de structration minimal qui le rend comparable à un programme. Les symboles, comme le signe d'affectation, par exemple, peuvent être choisis de manière libre ( = , :=, <-, <::, etc. )

**Réponse :**

```
valeur_maximum = 20

fonction case_value(grille, x, y, player) :
	Si plateau[x][y] contient un jeton :
		Retourner 0
	valeur <- 0
	Pour chaque direction dans (horizontale, verticale, diagonale_gauche, diagonale_droite) :
		compteur <- countalignement(grille, x, y, player)
		si (compteur + 1) > 4 :
			valeur <- valeur + valeur_maximum
		sinon :
			valeur <- valeur + (compteur)²
	Retourner valeur

fonction choosebestcase(grille, joueur) :
	maxvalue <- -infini
	bestcase <- null
	Pour x de 0 à lageurgrille - 1 :
		pour y de hauteurgrille - 1 :
			valeur <- case_value(grille, x, y, player)
			si value > maxvalue :
				maxvalue <- value
				bestcase <- (x, y)
	Retourner bestcase

fonction choosecaseforopponent(grille, player) :
	minvalue <- +infini
	casechoose <- null
	Pour x de 0 à lageurgrille - 1 :
		pour y de hauteurgrille - 1 :
			valeur <- case_value(grille, x, y, player)
			si value < minvalue :
				minvalue <- value
				casechoose <- (x, y)
	Retourner casechoose

fonction play() :
	grille <- init(largeurgrille, hauteurgrille)
	Tant que gamenotover(grille) :
		caseplayed <- choosebestcase(grille, us)
		action(grille, caseplayed, us)
		updatevalue(grille)
		Si checkvictory(grille, us) ou draw(grille) :
			Afficher "Partie finie"
			Arreter la boucle
		caseopponentplayed <- choosecaseforopponent(grille, us)
		caseplayed(grille, caseopponentplayed, adversaire)
		updatevalue(grille)
		Si checkvictory(grille, opponent) ou draw(grille) :
			Afficher "Partie finie"
			Arreter la boucle

fonction countalignement(grille, x, y, player) :
	compteur <- 0
	(dx, dy) <- vectordirection(direction)
	i <- 1
	Tant que casevalid(x + i*dx, y + i*dy, grille) et grille[x + i*dx][y + i*dy] == player :
		compteur <- compteur + 1
		i <- i + 1
	i <- 1
	Tant que casevalid(x - i*dx, y - i*dy, grille) et grille[x - i*dx][y - i*dy] == player :
		compteur <- compteur + 1
		i <- i + 1
	Retourner compteur
```

> **Question 3** :<br/>
> Estimez la complexité de l'algorithme. Appuyez votre calcul sur les opérations associés à chaque structure algorithmique de base (d'où l'importance d'avoir un pseudo-code structuré ;o)

**Réponse :**

Pour un coup unique (c’est-à-dire, l’évaluation du plateau pour choisir le meilleur coup) :
O(m × n × max(m, n))

Pour la simulation complète d’un jeu (dans le pire des cas où l’on joue m×n coups) :
O((m × n)² × max(m, n))


> **Question 4** :<br/>
> Êtes-cous certain que votre algorithme termine ? Ou pourrait-il éventuellement entrer dans une boucle infinie ? Expliquez pourquoi ?

**Réponse :**

L'algorithme ne peut pas entrer une boucle infinie.Lors de son tour , il parcourt les colonnes de gauche à droite en cherchant un coup valide , si la colonne est invalide (pleine) on passe à la suivante , si une colonne est valide (place disponnible) le coup est joué et le tour (boucle) se termine (break).Si toutes les colonnes sont invalides la boucle se termine et la partie aussi avec un EX-AEQUO.

> **Question 5** :<br/>
> D'après vous, serait-il possible d'imaginer un algorithme globalement plus simple, c'est-à-dire de complexité moins grande pour résoudre le problème ? Pourquoi ?

**Réponse :**

Il serait possible de faire beaucoup plus simple , la complexité de notre algorithme réside dans les calculs et analyse du plateau pour jouer de la façon la plus "parfaite" possible.Pour simplifier tout cela on peut utiliser la méthode de penser qu'aurait un enfant sur une partie , son objectif est gagner et il n'a pas de stratégie précise.Pour décider de gagner il sélectionne une colonne au hasard et en fait sa priorité , bien entendu il cherchera à bloquer son adversaire en cas de victoire imminente à son prochain tour.


#### Questions complémentaires

> **Question 6** :<br/>
> Implémentez l'algorithme, dans le langage de votre choix, dans le cas du jeu **Puissance 4**.<br/>
> Vous pourriez éventuellement vous trouver confrontés à des problèmes d'affichage graphique ; faites en sorte de les simplifier au maximum, quitte à afficher la solution en mode textuel.

**Réponse :**

fichier
```
beta.py
```

> **Question 7** :<br/>
> Existe-t-il un moyen d'optimiser la résolution du problème en évitant d'explorer certains coups qui, quoiqu'il arrive, ne pourraient pas être choisis ? Si oui, proposer une solution.

**Réponse :**


En termes d'optimisation , il y a plusieurs facteurs qui seraient possible délaisser.Les coups que nous devrions éviter d'explorer seront ceux-ci

- Une colonne pleine , il n'y a rien à faire
- Jouer sur une colonne à moitié-pleine où l'issue de ne permet de terminé la partie
- Une case isolée , sur un début de partie au milieu puis revirement après une colonne pleine
- Si un coup a une valeur précédente que celui précedent (à voir)


## Compression

#### Questions

> **Question 1** :<br/>
> Imaginons que vous ayez une image de taille quelconque, mais carrée (1024 x 1024 px, par exemple), quelles est la structure de donnée qui vous paraît la plus appropriée pour représenter cette image et quelles sont les informations qu'elle devrait contenir ?

**Réponse :**

Je prends pour exemple une image scindée en deux couleurs bleu et rouge avec donc une taille de 1024 x 1024 pixels :

-De 0 à 512 pixels en largeur , j'aurais donc des pixels bleu.
-De 512 à 1024 pixels en largeur , j'aurais des pixels rouge.
Pour représenter ça , on utilise une matrice

exemple d'une image (8x8 pixels)
```
[ B B B B | R R R R ]
[ B B B B | R R R R ]
[ B B B B | R R R R ]
[ B B B B | R R R R ]
[ B B B B | R R R R ]
[ B B B B | R R R R ]
[ B B B B | R R R R ]
[ B B B B | R R R R ]
```

Les informations contenus pour cette image seront le code couleur RGB des pixels.
```
[
  [(0,0,255), (0,0,255) , (0,0,255), (0,0,255) , (255,0,0), (255,0,0) , (255,0,0), (255,0,0)],
  [(0,0,255), (0,0,255) , (0,0,255), (0,0,255) , (255,0,0), (255,0,0) , (255,0,0), (255,0,0)],
  [(0,0,255), (0,0,255) , (0,0,255), (0,0,255) , (255,0,0), (255,0,0) , (255,0,0), (255,0,0)],
  [(0,0,255), (0,0,255) , (0,0,255), (0,0,255) , (255,0,0), (255,0,0) , (255,0,0), (255,0,0)],
  [(0,0,255), (0,0,255) , (0,0,255), (0,0,255) , (255,0,0), (255,0,0) , (255,0,0), (255,0,0)],
  [(0,0,255), (0,0,255) , (0,0,255), (0,0,255) , (255,0,0), (255,0,0) , (255,0,0), (255,0,0)],
  [(0,0,255), (0,0,255) , (0,0,255), (0,0,255) , (255,0,0), (255,0,0) , (255,0,0), (255,0,0)],
  [(0,0,255), (0,0,255) , (0,0,255), (0,0,255) , (255,0,0), (255,0,0) , (255,0,0), (255,0,0)]
]
                      <bleu>                                      <rouge>
```
> **Question 2** :<br/>
> Comment écrire l'algorithme qui permettra de réduire la taille de l'image de manière optimale, sans perdre sa qualité ?

**Réponse :**
Pour ne pas perdre sa qualité il faut utiliser une compression dîtes lossless.Dans le cas de mon image dans la réponse précedente , on peut utiliser l'algorithme RLE (Run-Length Enconding).Le principe est de compresser une suite de donnée dans une matrice en remplaçant les séquences répétées par une valeur + un compteur du nombre de répétition , exemple :


```
Première ligne d'une matrice :
[B, B, B, B, R, R, R, R] -> B = (0, 0, 255), R = (255, 0, 0)

RLE :
[(4, B), (4, R)] ->

La compression fonctionne car chaque pixel est codé en RGB avec 3 composantes (rouge,vert,bleu)
1 composante = 8 bits
1 pixel = 3 x 8 = 24 bits
Nous avons 8 pixels dans l'exemple donc 8 x 24 = 192 bits

Après compression
1 compteur = 8 bits (jusqu'à 255 pixels)
1 couleur RGB = 3 x 8 = 24 bits
1 paire = 24 + 8 = 32 bits
Nous avons 2 paires donc 2 x 32 = 64 bits

On passe de 192 bits à 64 bits
```

Algorithme :
```
Pour chaque ligne de l'image :
    initialiser une liste vide pour stocker l'encodage
    prendre le premier pixel comme pixel courant
    initialiser un compteur à 1

    pour chaque pixel suivant dans la ligne :
        si le pixel est identique au pixel courant :
            incrémenter le compteur
        sinon :
            enregistrer (compteur, pixel courant) dans la liste
            redémarrer compteur à 1 avec le nouveau pixel courant

    à la fin de la ligne, enregistrer le dernier (compteur, pixel)
```

Si une autre cas exemple d'image devrait être choisit avec des pixels de répétitions consécutives, l'algorithme d'Huffman serait sûrement le choix le plus pertinent.C’est une méthode de compression sans perte qui repose sur la fréquence d’apparition des données , plus des valeurs sont fréquentes moins elles sont codées avec de bits et à l'inverse les valeurs les plus rares sont codées avec plus de bits.




> **Question 3** :<br/>
> Sur quel(s) paramètre(s) de l'algorithme pourrait-on éventuellement jouer pour tolérer une certaine perte de qualité (dans des cas où l'on préfère privilégier la vitesse, par exemple) ?

**Réponse :**




Il faudrait utiliser une compression lossy , on cherche des détails dans nos données qui ne sont pas importante à l'humain , c'est ce que fait le format JPG.

> **Question 4** :<br/>
> Estimez la complexité de cet algorithme

**Réponse :**



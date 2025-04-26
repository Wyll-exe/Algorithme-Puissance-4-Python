
## Puissance 4

### Questions

> **Question 1** :<br/>
> Quelle est la structure de données qui vous paraît la plus adaptée à la représentation du problème ? Expliquez pourquoi et décrivez quelle information devrait contenir chaque élément de cette structure.

**Réponse :**







> **Question 2** :<br/>
> Ecrivez l'algorithme qui permet de résoudre le problème. Comme dans le documenet **Arbres.md**, cous pourrez éventuellemnt décomposer l'algorithme en pseudo-fonctions qui rendront les choses plus simples. Le pseudo-code peut être rédigé en « langue naturelle » — le français, l'anglais, etc. — mais doit respecter un niveau de structration minimal qui le rend comparable à un programme. Les symboles, comme le signe d'affectation, par exemple, peuvent être choisis de manière libre ( = , :=, <-, <::, etc. )

**Réponse :**



> **Question 3** :<br/>
> Estimez la complexité de l'algorithme. Appuyez votre calcul sur les opérations associés à chaque structure algorithmique de base (d'où l'importance d'avoir un pseudo-code structuré ;o)

**Réponse :**


> **Question 4** :<br/>
> Êtes-cous certain que votre algorithme termine ? Ou pourrait-il éventuellement entrer dans une boucle infinie ? Expliquez pourquoi ?

**Réponse :**


> **Question 5** :<br/>
> D'après vous, serait-il possible d'imaginer un algorithme globalement plus simple, c'est-à-dire de complexité moins grande pour résoudre le problème ? Pourquoi ?

**Réponse :**


#### Questions complémentaires

> **Question 6** :<br/>
> Implémentez l'algorithme, dans le langage de votre choix, dans le cas du jeu **Puissance 4**.<br/>
> Vous pourriez éventuellement vous trouver confrontés à des problèmes d'affichage graphique ; faites en sorte de les simplifier au maximum, quitte à afficher la solution en mode textuel.

**Réponse :**


> **Question 7** :<br/>
> Existe-t-il un moyen d'optimiser la résolution du problème en évitant d'explorer certains coups qui, quoiqu'il arrive, ne pourraient pas être choisis ? Si oui, proposer une solution.

**Réponse :**


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


### Exercice complémentaire : Calcul de surface

Imaginons que nous voulions mesurer (plus ou moins approximativement) la surface d'un lac donc le contour est très irrégulier, et potentiellement « **non convexe** » (i.e. dit simplement : « _il y a des creux et des bosses dans le contour_ »).

En théorie, nous pourrions appliquer la formule de Gauss, qui s'écrit ainsi :

> Aire = | (Sum(i=1..n-1) (x{i} * y{i+1} - x{i+1} * y{i}) + (x{n} * y{1} - x{1} * y{n})) / 2 |

Gauss considère toute forme comme un polygone dont les _n_ sommets sont des coordonnées _x_ et _y_.

Une autre technique pourrait consister à utiliser un quatree pour estimer la taille du lac.

#### Questions

> **Question 1** :<br/>
> En partant de l'exercice précédent, écrivez un algorithme permettant de trouver l'aire de manère empirique, dans appliquer de formule mathématique (sauf des additions, naturellement)

**Réponse :**


> **Question 2** :<br/>
> A votre avis, quelle est la meilleur méthode à utiliser en termes de nombres d'opérations à effectuer ? Expliquez votre réponse.

**Réponse :**

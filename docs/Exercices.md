# Devoir pour le cours d'Algorithmique

## Introduction

Le devoir comprend deux exercices distincts.

- Dans chaque cas, le but est davantage de présenter et d'expliquer une méthode de résolution du problème que d'écrire un programme concret dans un langage de programmation.
- Pour toutes les questions qui vous sont posées, vous essaierez de de répondre de la manière la plus concise possible (mais suffisamment détaillée tout de même pour développer une argumentation complète et compréhensible ;o).
- Les exercices et questions complémentaires sont là à titre de bonus, si vous avez le temps de vous y atteler, ou pour votre curiosité intellectuelle. Comme tout bonus, ils entreront pour une petite part dans la notation finale.
- Le travail en binôme est fortement conseillé. Vous pouvez éventuellement constituer des trinômes, mais pas au-delà (tout groupe plus nombreux sera considéré comme ayant eu suffisamment de ressources pour les faire les exercices complémentaires ;o)
- Vous êtes encouragé à vous servir de toute la documentation publique à votre disposition, l'essentiel étant que vous soyez capable d'expliquer le résultat.
- Vous êtes également autorisés à m'envoyer des messages pour toute question qui vous semblerait utile à votre progression.

## Jeu de stratégie

On cherche à écrire un algorithme qui permettra à un ordinateur de jouer à divers jeux de stratégie à deux joueurs comme les échecs, les dames, le go, le backgammon, etc.

Dans ces jeux, il est nécessaire de prédire le **meilleur coup** suivant à jouer, pour chaque joueur alternativement. Le « meilleur coup » est celui qui assure la plus grande probabilité de gain final de la partie, voire, dans certaines situations, un coup qui mènera de manière sûre à la victoire.
Comme ce sont des jeux qui se jouent tour par tour, un des deux joueurs _« calcule »_ un coup, puis le second fait de même, et ainsi de suite (alternativement) jusqu'à la fin de la partie.

Pour calculer le meilleur coup, on a besoin de connaître, d'estimer sa **valeur**. Pour cela, on dispose d'une fonction, appelée **heuristique**, qui se base sur des considérations propres à chaque jeu (cf. Annexe). Cette fonction retourne un nombre, entier ou réel, peu importe, Elle doit être croissante, c'est-à-dire que plus la valeur de sortie est grande, meilleur est le coup. Dans la première partie de la conception de l'algorithme, cette fonction est considérée comme connue.

Le principe de l'algorithme repose sur un double calcul et l'exploration de ce que nous appellerons un « **arbre de décision** ».

Prenons une situation donnée, par exemple le début du jeu (vous pouvez imaginer le début d'une partie d'échecs ou, plus simple, d'une partie de morpion). Le joureur A doit trouver le coup le plus avantageux pour lui.

### Version « naïve »

Une version simple de l'algorithme consiste à calculer l'heuristique pour tous les coups possibles et choisir celui dont la valeur est la plus grande. Cela étant fait, on peut passer au joueur B, qui procède de la même façon, puis redonner la main à A. Le processus se répète jusqu'à ce que l'algorithme détecte un cas de fin de partie.

Cette version est un cas particulier de l'algorithme général dans lequel l'arbre de décision est exploré avec une **profondeur** de 1, la profondeur étant le nombre de coups que chaque joueur va tenter d'anticiper.

Son avantage est d'être simple, mais il n'est pas certain que le meilleur coup immédiat garantisse la victoire finale. Aux échecs, par exemple, las cas de _« sacrifices_ » sont très courants, où un joueur laisse l'adversaire prendre une pièce, en espérant un gain futur.

### Version de profondeur 2

Prenons maintenant le cas dans lequel le joueur **A** essaie de savoir ce que jouera son adversaire en réponse à un coup donné. Il est très possible que le meilleur coup immédiat conduise à une situation qui serait par la suite défavorable à **A**.
Donc, avant de faire son choix, il faut que **A** _attende_ de savoir quel serait le meilleur choix de **B**.

En fonction du choix de **A**, **B** doit donc explorer à son tour tous les cas de figure mais, cette fois-ci, la meilleure valeur de l'heuristique sera la plus faible, car c'est celle qui rend la position de **A** la plus défavorable. Il faut donc comprendre la calcul de **B**, non pas comme celui qui serait le meilleur pour lui-même, mais comme celui qui empêcherait au mieux **A** de gagner. Petit exemple avec le jeu du morpion (les valeurs numériques sont purement indicatives) :

Situation initiale :
```
| O | X |   |
| O | O |   |
| X |   | X |
```
Admettons le coup **C<sub>1</sub>** suivant pour **A** (es ronds) :
```
| O | X |   |
| O | O |   |
| X | O | X |
```
Pour connaître la valeur de ce coup, je dois savoir quelles sont les réponses possibles **C<sub>2</sub><sup>k</sup>** de **B**.
```
| O | X | X | Le coup ne produit aucun avantage particulier
| O | O |   | H(x) = 10
| X | O | X | (coup favorable à A)

| O | X |   | Le coup empêche l'alignement de A
| O | O | X | H(x) = 0
| X | O | X | (mauvais coup _du point de vue de A_)
```
La valeur du coup **C<sub>1</sub>** est donc fonction de **C<sub>2</sub><sup>k</sup>**. B devrait donc choisir, s'il joue correctement  **C<sub>2</sub><sup>2</sup>**, ce qui serait donc la valeur attribuée à **C1**.
Soit, du point de vue mathématique :

> C<sub>1</sub> = Minimum<sub>i=1</sub><sup>n</sup> (C<sub>2</sub><sup>i</sup>)

Comme **A** peut jouer trois coups différents, il faut refaire la même opération pour chacun.

```
| O | X |   | Coup gagnant
| O | O | O | H(x) = 1000 (c'est-à-dire + ∞)
| X |   | X |

| O | X | O | Coup faible menant à une victoire possible de B
| O | O |   | H(x) = - 1000 (c'est-à-dire - ∞)
| X |   | X |
```

Quelle est maintenant la valeur finale de **C1** ? C'est celle qui maximise les gains de **A**. Soit :

> C = Maximum<sub>i=1</sub><sup>n</sup> (C<sub>1</sub><sup>i</sup>)

Ici, nous avons trois valeurs : 0, 1000, -1000.
**A** choisira donc le coup de valeur 1000 qui, dans cette situation lui assure le gain final de la partie.

### Cas général

Dans le cas général, on étend simplement le mécanisme précédent à une profondeur arbitraire, sachant que :

1. Plus la profondeur est grande, plus l'algorithme aura de chances de trouver un coup gagnant.
2. En contrepartie, le nombre de coups à examiner peut devenir prohibitif. Théoriquement, nous pourrions demander à la machine de calculer la valeur de tous les coups jusqu'à la fin de la partie, mais, hélas, cela suppose une combinatoire beaucoup trop grande pour être faisable pour la plupart des jeux intéressants.

Nous sommes donc contraints à nous limiter à un certain horizon, au-delà duquel la partie restera fondamentalement incertaine.

Cet algorithme permet de concevoir un **modèle théorique calculable** pour une grande famille de jeux à deux joueurs, mais pourrait aussi s'appliquer à des siotuation de la vie quotidienne, comme des négociations commerciales, dont l'heuristique pourrait cependant être extrêmement complexe à calculer.

Cet algorithme est également **récursif**. Il se définit à partir :

- d'un cas particulier : ici le coup le plus « lointain » que nous sommes en mesure d'évaluer
- du cas général : où la valeur du coup est estimée à partir des valeurs déjà calculées. C'edt ce quenous avons fait juste au-dessus pour le morpion.

> (cf. la présentation rapide de la récursivité dans la document <u>Récursivité.md</u>)

Dans le cas que nous étudions, nous pouvons dire que, si nous connaissons les valeurs pour les coups possibles à un niveau d'anticipation donné (par exemple 5), alors la valeur du coup _précédent_ dans le déroulement de la partie (donc de profondeur 4, dans l'exemple) sera, soit le maximum de ces valeurs, soit le minimum, en fonction du joueur dont c'est le tour. Ceci nous permettra, en fin de compte, d'estimer le meilleur _prochain_ coup (de profondeur 1).

### Questions

> **Question 1** :<br/>
> Quelle est la structure de données qui vous paraît la plus adaptée à la représentation du problème ? Expliquez pourquoi et décrivez quelle information devrait contenir chaque élément de cette structure.

> **Question 2** :<br/>
> Ecrivez l'algorithme qui permet de résoudre le problème. Comme dans le documenet **Arbres.md**, cous pourrez éventuellemnt décomposer l'algorithme en pseudo-fonctions qui rendront les choses plus simples. Le pseudo-code peut être rédigé en « langue naturelle » — le français, l'anglais, etc. — mais doit respecter un niveau de structration minimal qui le rend comparable à un programme. Les symboles, comme le signe d'affectation, par exemple, peuvent être choisis de manière libre ( = , :=, <-, <::, etc. )

> **Question 3** :<br/>
> Estimez la complexité de l'algorithme. Appuyez votre calcul sur les opérations associés à chaque structure algorithmique de base (d'où l'importance d'avoir un pseudo-code structuré ;o)

> **Question 4** :<br/>
> Êtes-cous certain que votre algorithme termine ? Ou pourrait-il éventuellement entrer dans une boucle infinie ? Expliquez pourquoi ?

> **Question 5** :<br/>
> D'après vous, serait-il possible d'imaginer un algorithme globalement plus simple, c'est-à-dire de complexité moins grande pour résoudre le problème ? Pourquoi ?

#### Questions complémentaires

> **Question 6** :<br/>
> Implémentez l'algorithme, dans le langage de votre choix, dans le cas du jeu **Puissance 4**.<br/>
> Vous pourriez éventuellement vous trouver confrontés à des problèmes d'affichage graphique ; faites en sorte de les simplifier au maximum, quitte à afficher la solution en mode textuel.

> **Question 7** :<br/>
> Existe-t-il un moyen d'optimiser la résolution du problème en évitant d'explorer certains coups qui, quoiqu'il arrive, ne pourraient pas être choisis ? Si oui, proposer une solution.

## Les quadtrees (arbres quadratiques)

Les « _quadtrees_ » sont des arbres pour lesquels chaque nœud à quatre enfants.
Ils sont beaucoup utilisés dans les applications liées à des représentations graphiques et aux images.

Le principe du [_quartree_](https://fr.wikipedia.org/wiki/Quadtree) est simple :

> **Définition**wbr/>
Si des données peuvent être représentées ous la forme  d'un tableau à deux dimensions carré — comme les pixels d'une image, par exemple — alors le _quadtree_ est la division de ce tableau en quatre tableaux carrés plus petits, de dimensions identiques entre eux, processus éventuellement reproduit récursivement, jusqu'à arriver à des dimensions indivisibles (un pixel, par exemple).

Exemple :
```
|   |   |   |   |   |   |   |   | Le chiffre 3 représenté dans une matrice 8 pixels sur 8 pixels
|   |   |XXX|XXX|XXX|XXX|   |   |
|   |   |   |   |   |XXX|   |   |
|   |   |   |XXX|XXX|XXX|   |   |
|   |   |   |   |   |XXX|   |   |
|   |   |XXX|XXX|XXX|XXX|   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
```
Décomposition en quatre sous-structures de premier niveau :
```
|   |   |   |   | HAUT GAUCHE
|   |   |XXX|XXX|
|   |   |   |   |
|   |   |   |XXX|

|   |   |   |   | BAS GACUCHE
|   |   |XXX|XXX|
|   |   |   |   |
|   |   |   |   |

|   |   |   |   | HAUT DROITE
|XXX|XXX|   |   |
|   |XXX|   |   |
|XXX|XXX|   |   |

|   |XXX|   |   | BAS DROITE
|XXX|XXX|   |   |
|   |   |   |   |
|   |   |   |   |

```

### Compression

La première application des quadtrees est la compression d'images. Naturellement, les algorithmes comme JPEG ou PNG sont beaucoup plus sophistiqués, quoique basés sur des considérations comparables, mais nous voulons mettre en œuvre le principe.

Les données de départ sont des images en noir et blanc, mais vous pouvez élargir le problème à des images en niveaux de gris, par exemple (la question des couleurs rend la chose plus difficile).

#### Questions

> **Question 1** :<br/>
> Imaginons que vous ayez une image de taille quelconque, mais carrée (1024 x 1024 px, par exemple), quelles est la structure de donnée qui vous paraît la plus appropriée pour représenter cette image et quelles sont les informations qu'elle devrait contenir ?

> **Question 2** :<br/>
> Comment écrire l'algorithme qui permettra de réduire la taille de l'image de manière optimale, sans perdre sa qualité ?

> **Question 3** :<br/>
> Sur quel(s) paramètre(s) de l'algorithme pourrait-on éventuellement jouer pour tolérer une certaine perte de qualité (dans des cas où l'on préfère privilégier la vitesse, par exemple) ?

> **Question 4** :<br/>
> Estimez la complexité de cet algorithme

## Rendu

- Le rendu devra être fait sous forme d'un document unique comportant les réponses aux différentes questions ;
- Si vous écrivez du code, pour Puissance 4 par exemple, ou tout autre code que vous auriez écrit, joignez-le au document dans une archive séparée ;
- Commentez vos codes et pseudo-codes. Pour le code informatique, toues les langages de programmation ont des formats de documentation, comme les **DocBLocks** en PHP, les **DocStrings** en JS ou en Python. Utilisez-les, ces formats permettent la création automatique de la documentation technique des applications ;
- Le rendu devra être fait de manière absolument prioritaire via la plate-forme **Hetic Learn**, qui consitue un point unique de dépôt ; en cas de problème, vous pouvez passer par Discord, de préférence en message privé pour que je sois notifié à coup sûr de votre message
- Votre rendu devra entionner expicitement les noms de personnes ayant participé au travail, mais un seul rendu par groupe est demandé.
- La date de rendu nominale est fixée au 27 avril 23h59:59 ; une latitude « modérée » et « raisonnable » restera cependant tolérée.

## Annexes

### Une heuristique (parmi d'autres) pour le jeu Puissance 4

Une bonne heuristique doit vous permettre de juger précisément la meilleure réponse à apporter à une situation donnée. C'est un équivalent algorithmique (et souvent incomplet) de notre compréhension du jeu.

On remarquera que, en passant d'un jeu à l'autre, ou d'un problème à l'autre, l'algorithme de change pas. Seul l'heuristique différencie les échecs du morpion, ainsi que la structure des données.

Pour des jeux complexes comme les échecs, une bonne heuristique puet être extrêmement difficile à écrire. Les pièces ont des puissances différentes, elles agissent en combinaison, certaines zones de l'échiquier sont plus importantes que d'autres, etc. Les grands joueurs d'échecs développent donc des représentations mentales des parties qui sont souvent éloignées d'un modèle calculatoire.

A l'inverse, une heuristique simple, et même simplette, serait de donner à chaque case — ou chaque mouvement — une valeur aléatoire. Il est tout de même possible, statistiquement, que le programme gagne, mais la probabilité sera très faible.

Pour un jeu relativement simple comme **Puissance 4**, l'heuristique s'attache à mesurer la valeur d'une position. On peut donc énumérer quelques critères qui participent à l'importance de jouer à un endroit précis.

1. L'emplacement permet un alignement de 4 jetons
2. L'emplacement empêche l'alignement de 4 jetons de l'adversaire
3. L'emplacement permet (potentiellement) un certain nombre d'alignements (davantage au centre que dans les coins, par exemple)
4. L'emplacement permet de progresser dans un alignement

La fonction heuristique H(p) calculera, dans la cas le plus simple, une somme des valeurs attribuées aux quatre critères. Cette somme pourrait être pondérée pour tenir compte de l'importance relative de ces critères. Il serait peut-être possible de trouver une formule plus sophistiquée, mais ce n'est sans doute pas utile ici.

Une bonne heuristique est souvent le résultat d'essais et d'erreurs. Il n'existe pas, hélas, de méthode formelle pour garantir _a priori_ qu'une heuristique est optimale.

### Ressources

- [Algorithme récursif (Wikipedia)](https://fr.wikipedia.org/wiki/Algorithme_r%C3%A9cursif)
- [Théorème du minimax de von Neumann (Wikipedia)](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_du_minimax_de_von_Neumann)
- [Dilemme du prisonnier (Wikipedia)](https://fr.wikipedia.org/wiki/Dilemme_du_prisonnier)
- [Théorie des jeux (Wikipedia)](https://fr.wikipedia.org/wiki/Th%C3%A9orie_des_jeux)
- [Quadtree (Wikipedia)](https://fr.wikipedia.org/wiki/Quadtree)
- [An overview of quatrees, octrees ... (Hanan Samet, 1975)](https://www.cs.umd.edu/~hjs/pubs/Samettfcgc88-ocr.pdf)
- [K-D trees and Quadtrees (James Fogarty, 2007)](https://courses.cs.washington.edu/courses/cse326/07au/lectures/lect12.pdf)
-

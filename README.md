
# Algorithme MinMax pour un Puissance 4.

## Membres du groupe

    JOVENE Kévin
    DUBOIS Laurent

## Stacks utilisée

    Python

## Briefing 

Nous allons commencer par établir le terrain de jeu du Puissance4 comme étant un tableau. Chaque case de ce tableau seront représentées par une valeur de 0 à 100, 100 étant le meilleur coup probable pour gagner la partie. 

Pour établir les valeurs initiales, nous allons créer plusieurs fonctions qui calculeront le nombre de combinaisons gagnantes pour chaques cases jouables du tableau :

    => La première fonction calculera les combinaisons en ligne de chaques cases jouables qu'on appellera CombiLine() qui va retourner 6 lignes de valeurs 

    => Le seconde fonction calculera les combinaisons en colonne de chaques cases jouables en prenant en paramètre CombiLine() qu'on appellera CombiColumn() qui retournera 7     lignes de valeurs (représentant les valeurs des colonnes) en prenant en compte les valeurs en ligne.

    => La troisième fonction calculera les combinaisons en diagonales de chaques cases jouables en prenant en paramètre CombiColumn() qui s'appellera CombiDiagonal() qui retournera le tableau final de valeurs initial.

Donc d'après ce tableau initial, on devrait apercevoir que les cases au centre du plateau sont les cases ayant le plus de valeur par exemple.

On va appeler ce tableau : I = []

Concernant les cases non jouables ou non jouées, nous allons établir une valeur par défault qui sera -1.

## Que la partie commence !

Chaque tours, l'algorithme va mettre à jour le tableau I en fonction des jetons joués sur le terrain.

Ce dernier va calculer les nouvelles possibilités et décider de laquelle est la meilleure en prenant en paramètres ces trois objectifs :

    => Le jeton joué

    => Les cases adjacentes au jeton joué : Ces dernières prendront un bonus de valeur en fonction du nombre de jeton probablement alignés.

    => Il prendra en considération la défense : Une case sera aussi intéréssante à jouer même si ce coup est défensif. (Case permettant de réduire les coups gagnants de l'adversaire qu'on appellera ) 
    Cependant l'algorithme favorisera toujours l'attaque à la défense (bonus de valeur)











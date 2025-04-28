
# Rendu du Projet d'Algorithmie

## Membres du groupe

    JOVENE Kévin
    DUBOIS Laurent
    MARCHESCHI Thomas

## Stacks utilisée

    Python

## QUESTION 1
Quelle est la structure de données qui vous paraît la plus adaptée à la représentation du problème ? Expliquez pourquoi et décrivez quelle information devrait contenir chaque élément de cette structure.

- La structure qui nous paraît la plus adaptée serait la structure en Arbres car cette dernière nous permet d'étudier toutes les possibilités et ainsi de décider laquelle est la meilleure. De plus c'est très lisible !

## QUESTION 2
Ecrivez l'algorithme qui permet de résoudre le problème. Comme dans le documenet **Arbres.md**, cous pourrez éventuellemnt décomposer l'algorithme en pseudo-fonctions qui rendront les choses plus simples. Le pseudo-code peut être rédigé en « langue naturelle » — le français, l'anglais, etc. — mais doit respecter un niveau de structration minimal qui le rend comparable à un programme. Les symboles, comme le signe d'affectation, par exemple, peuvent être choisis de manière libre ( = , :=, <-, <::, etc. )

- Prenons l'exemple du jeu Puissance4 afin d'illustrer l'algorithme MinMax : 

    - Nous allons commencer par établir le terrain de jeu du Puissance4 comme étant un tableau. Chaque case de ce tableau seront représentées par une valeur de 0 à 100, 100 étant le meilleur coup probable pour gagner la partie. 

    - Pour établir les valeurs initiales, nous allons créer plusieurs fonctions qui calculeront le nombre de combinaisons gagnantes pour chaques cases jouables du tableau :

        => La première fonction calculera les combinaisons en ligne de chaques cases jouables qu'on appellera CombiLine() qui va retourner 6 lignes de valeurs 

        => Le seconde fonction calculera les combinaisons en colonne de chaques cases jouables en prenant en paramètre CombiLine() qu'on appellera CombiColumn() qui retournera 7     lignes de valeurs (représentant les valeurs des colonnes) en prenant en compte les valeurs en ligne.

        => La troisième fonction calculera les combinaisons en diagonales de chaques cases jouables en prenant en paramètre CombiColumn() qui s'appellera CombiDiagonal() qui retournera le tableau final de valeurs initial.

    - Donc d'après ce tableau initial, on devrait apercevoir que les cases au centre du plateau sont les cases ayant le plus de valeur par exemple.

    - On va appeler ce tableau : I = []

    - Concernant les cases non jouables ou non jouées, nous allons établir une valeur par défault qui sera -1.

    - Chaque tours, l'algorithme va mettre à jour le tableau I en fonction des jetons joués sur le terrain.

    - Ce dernier va calculer les nouvelles possibilités et décider de laquelle est la meilleure en prenant en paramètres ces trois objectifs :

        => Le jeton joué

        => Les cases adjacentes au jeton joué : Ces dernières prendront un bonus de valeur en fonction du nombre de jeton probablement alignés.

        => Il prendra en considération la défense : Une case sera aussi intéréssante à jouer même si ce coup est défensif. (Case permettant de réduire les coups gagnants de l'adversaire qu'on appellera ) 
        Cependant l'algorithme favorisera toujours l'attaque à la défense (bonus de valeur)

## QUESTION 3
Estimez la complexité de l'algorithme. Appuyez votre calcul sur les opérations associés à chaque structure algorithmique de base (d'où l'importance d'avoir un pseudo-code structuré)


- La complexité de l'algorithme est de O(1) car nous avons un tableau de taille limité 6*7 où les opérations sont bornées par des constantes. 


## QUESTION 4
Êtes-cous certain que votre algorithme termine ? Ou pourrait-il éventuellement entrer dans une boucle infinie ? Expliquez pourquoi ?

- Notre algorithme ce termine car nous avons un nombre de coups limitée par la taille du tableau.

## QUESTION 5
D'après vous, serait-il possible d'imaginer un algorithme globalement plus simple, c'est-à-dire de complexité moins grande pour résoudre le problème ? Pourquoi ?

- Nous avons déjà une complexité de O(1) qui est la plus faible. Cependant, pour augmenter la complexité nous pourrions prendre en compte : les potentiels actions défensives et les bonus offensifs.



## QUESTION 6
Implémentez l'algorithme, dans le langage de votre choix, dans le cas du jeu **Puissance 4**.
Vous pourriez éventuellement vous trouver confrontés à des problèmes d'affichage graphique ; faites en sorte de les simplifier au maximum, quitte à afficher la solution en mode textuel.

- Cf Puissance4.py

## QUESTION 7
Existe-t-il un moyen d'optimiser la résolution du problème en évitant d'explorer certains coups qui, quoiqu'il arrive, ne pourraient pas être choisis ? Si oui, proposer une solution.

- Comme nous l'avons démontré précédement dans l'algorithme, nous affectons une valeur bonus en fonction de son efficacité.


# QUADTREES

## QUESTION 1
Imaginons que vous ayez une image de taille quelconque, mais carrée (1024 x 1024 px, par exemple), quelles est la structure de donnée qui vous paraît la plus appropriée pour représenter cette image et quelles sont les informations qu'elle devrait contenir ?

- La structure de donnée paraissant la plus appropriée serait les quadtrees. Grâce à cette derniere, nous pouvons diviser chaque pixels de l'image (qui représentent les noeuds du quadtree) et ainsi pouvoir conserver le même ratio de résolution tout en pouvant supprimer les noeuds non exploités.

## QUESTION 2
Comment écrire l'algorithme qui permettra de réduire la taille de l'image de manière optimale, sans perdre sa qualité ?

- 1. Fonction CompressImage(image, seuil):
    - Entrée : 
        - image : une matrice 2D représentant l'image (par exemple, 1024x1024 pixels).
        - seuil : une valeur de tolérance pour décider si une région peut être compressée.
    - Sortie : un Quadtree représentant l'image compressée.

2. Si la taille de l'image est 1x1 :
    - Retourner un nœud contenant la valeur du pixel.

3. Calculer la variance (ou l'écart maximal) des pixels dans la région actuelle :
    - variance = Max(pixel_values) - Min(pixel_values)

4. Si variance <= seuil :
    - Retourner un nœud unique contenant la valeur moyenne des pixels.

5. Sinon :
    - Diviser l'image en 4 sous-régions égales (haut-gauche, haut-droite, bas-gauche, bas-droite).
    - Pour chaque sous-région :
        - Appeler CompressImage(sous_région, seuil).
    - Retourner un nœud parent contenant les 4 enfants.

6. Fin de la fonction.

## QUESTION 3
Sur quel(s) paramètre(s) de l'algorithme pourrait-on éventuellement jouer pour tolérer une certaine perte de qualité (dans des cas où l'on préfère privilégier la vitesse, par exemple) ?

- Sur le paramètre "seuil", ce dernier est censé établir une limite de compression entre la taille et la qualité de l'image (par exemple: seuil élévé = perte de qualité, diminution de la profondeur du quadtree, diminution de la taille de l'image)

## QUESTION 4 
Estimez la complexité de cet algorithme.

- Pour une image de taille N x N la compléxité que nous estimons est de O(N²) car dans le pire des cas (une image 1x1) chaques pixels représentent un noeud.
# numworks-projects
Support :
  Ce jeu est destiné à être joué sur une calculatrice numworks avec la version 2.05 d'Omega.
  Il est aussi possible d'y jouer sans Omega, en revanche la notion de record ne sera plus fonctionnelle.

Principe du jeu :
  Ce programme python contient 2 modes de jeu :
    - un 1vs1
    - un mode solo contre un mur avec un système d'enregistrement de records d'échanges
  L'objectif du jeu est de, grâce aux raquettes verticales, renvoyer la balle du côté adverse.

Comment jouer :
  Afin de lancer le programme, il suffit de selectionner le mode de jeu (play1v1 ou play 1vmur).
  Une fois le programme lancé, le jeu commence au bout de 3 secondes.
  Le joueur rouge peut alors bouger sa raquette verticalement en utilisant les touches "7" pour monter et "0" pour descendre.
  Le joueur bleu, lui, bouge sa raquette grâce aux touches ")" pour menter et "EXE" pour descendre.
  A la fin de la partie il est possible de rejouer en cliquant sur "OK".

Utilisation de la notion de record :
  Afin d'utiliser cette fonctionnalité, il suffit de créer un fichier annexe se nommant "highscore.py" et de lancer la fonction initialisationDuFichierAnnexe().

=================================
Informations générales holeOffset
=================================

:Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
:Projet:             holeOffset
:dépôt GitHub:       
:documentation:      
:Licence:            CC BY-NC-SA 4.0
:Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

Déscription
===========

holeOffset.py permet de parcourrir un fichier de perçage généré par les logiciel de CIAO
et de corriger les coordonées de chacun des trous en fonction des repères identifiés sur
le PCB. Ce programme est extrait du projet : Trouilloteuse

Arborescence du projet
======================

Pour aider à la compréhension de mon organisation, voici un bref déscrptif de
l'arborescence de se projet.Cette arborescence est à reproduire si vous récupérez ce dépôt
depuis GitHub. ::

openFile               # Dossier racine du projet (non versionner)
|
+--project             # (branch master) contient l'ensemble du projet en lui même
|  |
|  +--_1_userDoc       # Contien toute la documentation relative au projet
|  |   |
|  |   \--source       # Dossier réunissant les sources utilisées par Sphinx
|  |
|  +--_2_modelisation  # contien tous les plans et toutes les modélisations du projet
|  |
|  +--_3_software      # Contien toute la partie programmation du projet
|  |
|  \--_4_PCB           # Contient toutes les parties des circuits imprimés (routage,
|                      # implantation, typon, fichier de perçage, etc
|
\--webDoc              # Dossier racine de la documentation qui doit être publiée
   |
   \--html             # (branch gh-pages) C'est dans se dosier que Sphinx vat
                       # générer la documentation à publié sur internet


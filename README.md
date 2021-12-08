# LabelsAPI
## Introduction
Ce programme à pour but de tester une phrase donner en entrée par un utilisateur et de lui renvoyer le sentiment de sa phrase.
## L'algorithme 'algo.py'
Afin de d'arriver à notre objectif de prédiction du sentiment d'une phrase, nous allons partir d'un labels.csv répertoriant des tweets. Ces tweets sont classés selon leur sentiments ('hate_speech', pour un discours haineux, 'offensive_language', pour les phrases offenssantes et 'neither', pour aucun des 2). Une colonne du .csv nous indique le sentiment de chaque tweets grâce ) un indice 'class'. Nous créons donc un algorithme s'entraînant sur les tweets et leurs 'class' afin d'obtenir notre prédiction de sentiment.
Pour pouvoir travaillier sur nos tweets, il a fallu les 'clean' pour ne pas avoir de biais au moment de la prédictions. Nous avons donc enlevé les caractères spéciaux, les '#', les mots possèdant 2 caractères ou moins pour obtenir de meileurs résultats et que l'entraînement de l'algorithme soit bon.
## L'application Flask 'app.py'
Nous avons développer une application permettant à l'utilisateur de rentrer un texte dans l'URL pour pouvoir en déduire son sentiment. 
## Comment utiliser l'application.

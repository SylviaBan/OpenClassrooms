# Participez à la conception d'une voiture autonome :red_car: :bike: :skateboard: :busstop:

Projet 8 [_Participez à la conception d'une voiture autonome_](https://openclassrooms.com/fr/projects/723/assignment)


## :pushpin: Enjeux
Votre entreprise conçoit des systèmes embarqués de vision par ordinateur pour les véhicules autonomes. Dans l’équipe projet, vous êtes responsable de la segmentation des images.
Votre rôle est de concevoir un premier modèle de segmentation d’images qui devra s’intégrer facilement dans la chaîne complète du système embarqué.

## :spiral_notepad: Dataset
[_cityscapes_](https://www.cityscapes-dataset.com/dataset-overview/)

## :ladder: Objectifs
Entraîner un modèle de Deep Learning sur des images et évaluer ses performances.
Utiliser des techniques d’augmentation des données.
Manipuler un jeu de données volumineux (générateur de données).

## :wrench: Technologies
- Pandas
- Numpy 
- Matplotlib
- Seaborn
- Scipy
- Sklearn (GridSearchCV, LogisticRegression, t-SNE, LatentDirichletAllocation)
- Tensorflow
- Docker, Flask, Heroku, Pythonanywhere, GCP

## :chart_with_upwards_trend: Compétences évaluées

###  🎓  Entraîner un modèle de Deep Learning sur des images
#### L’entraînement d’un modèle de Deep Learning sur des images est réalisé si :
>- la cible a été identifiée
>- la séparation du jeu de données en jeu d’entraînement et en jeu de test a été réalisée 
>- il n’y a pas de fuite d’information entre les deux jeux de données (entraînement et test)

#### L’entraînement d’un modèle de Deep Learning sur des images est pertinente si :
>- Plusieurs modèles ont été essayés en partant du plus simple vers les plus complexes

#### L’entraînement d’un modèle de Deep Learning sur des images est présentable si :
>- Le modèle a été déployé grâce à une API Flask ou FastAPI
>- Le modèle prend en entrée une image et retourne l’image des segments identifiés par le modèle (mask)

###  🎓  Evaluer la performance d’un modèle de Deep Learning sur des images 
#### L’évaluation des performances d’un modèle de Deep Learning sur des images est complète si :

>- une métrique adaptée à la problématique métier a été choisie et sert à évaluer la performance des modèles (ex : coefficient Sørensen-Dice de similarité)

>- la performance d’un modèle de référence a été évaluée (UnetMini par exemple) et sert de comparaison pour évaluer la performance des modèles plus complexes 

#### L’évaluation des performances d’un modèle de Deep Learning sur des images est pertinente si :
>- Hormis la métrique choisie, au moins un autre indicateur a été calculé pour comparer les modèles (ex : le temps nécessaire pour l’entraînement du modèle)
>- Au moins un des hyperparamètres du modèle choisi a été optimisé (ex : le choix de la fonction loss)

#### L’évaluation des performances d’un modèle de Deep Learning sur des images est présentable si :
>- une synthèse comparative des différents modèles a été rédigée dans la note technique (ex : tableau comparatif des résultats pour les différents modèles)
>- le choix de la métrique d’évaluation a été explicité 

###  🎓  Utiliser des techniques d’augmentation des données
#### La mise à profit des techniques d’augmentation des données est complète si :

>- au moins trois techniques d’augmentation des données ont été utilisées (ex : rotation, changement d’échelle, ajout de bruit,…)

#### La mise à profit des techniques d’augmentation des données est pertinente si :
>- l’utilisation des techniques d’augmentation ont permis d’améliorer la performance du modèle de Deep Learning

#### La mise à profit des techniques d’augmentation des données est présentable si :
>- une synthèse comparative des améliorations de performance grâce aux différentes techniques utilisées a été rédigée dans la note technique

###  🎓  Manipuler un jeu de données volumineux
#### La manipulation d’un jeu de données volumineux est réalisée si :
>- un générateur de données permettant le traitement des images sur plusieurs cœurs de calcul a été développé et testé

#### La manipulation d’un jeu de données volumineux est pertinente si :
>- le générateur de données a été rédigé sous forme de classe python

#### La manipulation d’un jeu de données volumineux est présentable si :
>- le script du générateur de données est entièrement automatisé

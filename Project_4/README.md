# Construisez un modèle de scoring :moneybag: :chart:

Projet 4 [_Construisez un modèle de scoring_](https://openclassrooms.com/fr/paths/188/projects/719/assignment)

## :pushpin: Enjeux
Pour accorder un crédit, l'entreprise Home Credit doit estimer la solvabilité d'un client. Elle souhaite donc développer une classification automatique de scoring pour décider si un prêt peut être accordé ou non.
Mise en œuvre d'un outil de "scoring" qui calcule la probabilité de remboursement de crédit par un client.

## :spiral_notepad: Dataset
[_olist_](https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/Parcours_data_scientist/Projet+-+Impl%C3%A9menter+un+mod%C3%A8le+de+scoring/Projet+Mise+en+prod+-+home-credit-default-risk.zip)

## :ladder: Objectifs
* Utiliser des modèles supervisés linéaires et non linéaires.
* Développer un algorithme de classification pour aider les chargés de relation client à décider si un prêt peut être accordé à un client.
* Fournir une mesure de l’importance des variables qui ont poussé le modèle à donner une probabilité à un client.

## :wrench: Technologies
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scipy
- Sklearn (RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, LogisticRegression, PolynomialFeatures, train_test_split, GridSearchCV, confusion_matrix)


## :chart_with_upwards_trend: Compétences évaluées

###  🎓  Transformer les variables pertinentes pour un modèle supervisé classique (= feature engineering)

#### Le feature engineering  est complète si :
>- une analyse exploratoire a été conduite sur les variables initiales
>- les variables catégorielles ont été identifiées et transformées pour être utilisées par le modèle (ex : one hot encoding)
>-  au moins trois nouvelles variables ont été construites à partir des variables initiales

#### Le feature engineering  est pertinente si :
>- les variables ont été normalisées (si besoin selon l’algorithme choisi)
>- la performance du modèle est améliorée par l’ajout des nouvelles variables construites

#### Le feature engineering est présentable si :
>-  une représentation graphique de l’importance des variables a été réalisée
>- la méthode de détermination de l’importance des variables a été explicitée et le principe décrit en 5-10 lignes

###  🎓  Entraîner un modèle supervisé classique qui répond aux attentes des métiers
####  L’entraînement d’un modèle supervisé classique répondant à la problématique métier est réalisé si:
>-la variable cible a été identifiée
>-  la séparation du jeu de données en jeu d’entraînement et en jeu de test a été réalisée et il n’y a pas de fuite d’information entre les deux jeux de données (ex : la normalisation a bien été réalisée uniquement sur le jeu d’entraînement indépendamment du jeu de données de test)

#### L’entraînement d’un modèle supervisé classique répondant à la problématique métier est pertinente si :

>- Plusieurs modèles ont été essayés (au minimum un linéaire et un non linéaire)

>- Au moins une méthode de mesure de l’importance des variables a été mise en oeuvre et explicitée.

###  🎓  Evaluer les performances d’un modèle supervisé classique
#### L’évaluation des performances d’un modèle supervisé classique est complète si :
>- une métrique specifiquement adaptée au cas et qui pénalise le non détection a été definie par l'étudiant et utilisé pour évaluer la performance de ses modèles
>- la performance d’un modèle de référence a été évaluée et sert de comparaison pour évaluer la performance des modèles plus complexes (exemple de modèle de référence : le modèle prédisant qu’aucun client ne fait défaut)

#### L’évaluation des performances d’un modèle supervisé classique est pertinente si :
>-la validation croisée est utilisée pour comparer les performances des modèles sur la métrique d’évaluation

#### L’évaluation des performances d’un modèle supervisé classique est présentable si :
>- une synthèse comparative des différents modèles a été rédigée (ex : tableau comparatif des résultats pour les différents modèles)
>- le choix de la métrique d’évaluation a été explicité

###  🎓 Adapter les hyperparamètres d’un modèle d’apprentissage supervisé classique afin de l’améliorer
#### L’optimisation des hyperparamètres d’un modèle supervisé est complète si :
>- les hyperparamètres des modèles utilisés ont été identifiés
>- une méthode d’optimisation des hyperparamètres a été mise en oeuvre (ex : grid search)
#### L’optimisation des hyperparamètres d’un modèle supervisé est pertinente si :
>- une validation croisée a été mise en oeuvre pour optimiser les hyperparamètres


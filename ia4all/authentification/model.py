# views.py
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler


def regression_models(df,target):      

    # Charger les données depuis un fichier CSV
    data = df.dropna()
    # Séparer les fonctionnalités et la variable cible
    X = data[data.describe().columns]
    if target in X.columns:
        X = X.drop(target,axis=1)    
    X = StandardScaler().fit_transform(X.values)
    y = data[target].values

       # Initialiser les modèles de régression linéaire, KNN et forêt aléatoire
    linear_regression = LinearRegression()
    knn = KNeighborsRegressor()
    random_forest = RandomForestRegressor()

    # Évaluer la performance des modèles à l'aide d'une validation croisée
    linear_regression_scores = cross_val_score(linear_regression, X, y, cv=5)
    knn_scores = cross_val_score(knn, X, y, cv=5)
    random_forest_scores = cross_val_score(random_forest, X, y, cv=5)

    # Afficher les scores moyens pour chaque modèle
    mse_lr = -1 * linear_regression_scores.mean()
    mse_knn = -1 * knn_scores.mean()
    mse_rf = -1 * random_forest_scores.mean()  

    result = f"Régression linéaire score moyen: {linear_regression_scores.mean()}<br>"
    result += f"KNN score moyen: {knn_scores.mean()}<br>"
    result += f"Forêt aléatoire score moyen: {random_forest_scores.mean()}"

    return mse_lr, mse_knn, mse_rf
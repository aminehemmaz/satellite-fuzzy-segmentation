# Théorie : logique floue et Fuzzy C-Means

[← Retour au README](../../README.fr.md) · [English](../theory.md)

Ce document présente les concepts du projet : des ensembles flous à l'algorithme de clustering **Fuzzy C-Means (FCM)** et à son usage pour la segmentation d'images.

## 1. La logique floue en bref

La **logique floue**, introduite par Lotfi Zadeh en 1965, étend la logique booléenne classique. Au lieu de deux valeurs de vérité (*faux = 0*, *vrai = 1*), une assertion possède un **degré de vérité** dans l'intervalle [0, 1]. Elle convient aux notions vagues, incertaines ou subjectives comme « chaud », « lourd » ou « rapide », et fait le lien entre modélisation symbolique (règles en langage naturel) et modélisation numérique.

### Ensembles classiques et ensembles flous
| | Ensemble classique | Ensemble flou |
|---|---|---|
| Appartenance | binaire : l'élément appartient ou non (0 ou 1) | graduelle : une valeur dans [0, 1] |
| Exemple | « nombres pairs » : 4 → 1, 5 → 0 | « températures chaudes » : 25 °C → 0,4 ; 35 °C → 0,9 |
| Frontière | nette | progressive |

Un ensemble flou A sur un univers X est défini par sa **fonction d'appartenance** μ_A : X → [0, 1]. Le **degré d'appartenance** μ_A(x) mesure à quel point x appartient à A.

### Inférence floue (pour mémoire)
Un système flou classique comporte quatre étapes :
1. **Fuzzification** : les entrées numériques (par ex. 35 °C) sont associées à des ensembles flous (« tiède », « chaud »).
2. **Base de règles floues** : règles `SI <condition> ALORS <action>` en langage naturel.
3. **Moteur d'inférence** : combine les règles activées par les degrés d'appartenance.
4. **Défuzzification** : la sortie floue est reconvertie en valeur précise, le plus souvent par la méthode du **centre de gravité**.

Le FCM n'utilise pas de base de règles : il reprend seulement l'idée d'**appartenance graduelle**.

## 2. Place du Fuzzy C-Means en IA et en machine learning

| Axe | Position du Fuzzy C-Means |
|---|---|
| Paradigme d'apprentissage | **Apprentissage non supervisé** : aucune donnée étiquetée n'est nécessaire |
| Tâche | **Clustering** (ici : regroupement de pixels = segmentation d'image) |
| Affectation | **Clustering flou (soft)** : chaque échantillon appartient à tous les clusters avec un degré |
| Famille | **Soft computing / intelligence computationnelle** (logique floue) |
| Plus proche parent | **K-Means** (clustering dur), dont le FCM est la généralisation floue |
| Domaine | Vision par ordinateur, traitement d'images, télédétection |

## 3. Fuzzy C-Means

Le Fuzzy C-Means (Dunn, 1973 ; généralisé par Bezdek, 1981) partitionne N points x₁ … x_N en **C clusters**. Chaque point a un degré d'appartenance u_ij ∈ [0, 1] à chaque cluster i, avec la contrainte que la somme des appartenances d'un point vaut 1 :

$$
\sum_{i=1}^{C} u_{ij} = 1 \quad \forall j
$$

### Fonction objectif
Le FCM minimise la somme pondérée des distances quadratiques intra-cluster :

$$
J_m(U, c) = \sum_{i=1}^{C}\sum_{j=1}^{N} u_{ij}^{\,m}\,\lVert x_j - c_i \rVert^{2}, \qquad m > 1
$$

* **U** est la matrice d'appartenance C × N, **c_i** le centre (centroïde) du cluster i.
* **m** est l'**indice de flou**. Quand m → 1, la partition devient dure (proche du K-Means) ; plus m est grand, plus elle est floue. Ce projet utilise **m = 1,7**.

### Optimisation alternée
La minimisation de J_m sous contrainte donne deux règles de mise à jour, appliquées alternativement :

**Mise à jour des centres** (moyenne pondérée par les appartenances) :

$$
c_i = \frac{\sum_{j=1}^{N} u_{ij}^{\,m}\, x_j}{\sum_{j=1}^{N} u_{ij}^{\,m}}
$$

**Mise à jour des appartenances** (plus un point est proche d'un centre par rapport aux autres, plus son appartenance est élevée) :

$$
u_{ij} = \frac{1}{\sum_{k=1}^{C}\left(\dfrac{\lVert x_j - c_i\rVert}{\lVert x_j - c_k\rVert}\right)^{\frac{2}{m-1}}}
$$

### Algorithme

```
Entrée : données x_1..x_N, nombre de clusters C, indice de flou m > 1, seuil epsilon, max_iter
Sortie : matrice d'appartenance finale U et centres c

1. Initialiser U aléatoirement (chaque colonne somme à 1)
2. Répéter jusqu'à ||U_new - U|| < epsilon ou max_iter atteint :
     a. calculer les centres c_i à partir de U         (mise à jour des centres)
     b. calculer U_new à partir des centres            (mise à jour des appartenances)
3. Retourner U et c
```

Dans ce projet, les données sont les **intensités des pixels** (une caractéristique par pixel, dans [0, 1]), `C = k`, `epsilon = 1e-5` et `max_iter = 300`. La **segmentation dure** finale affecte chaque pixel au cluster d'appartenance maximale (`argmax`).

### Complexité
Chaque itération coûte O(N · C), avec N le nombre de pixels. Pour une image de 2448 × 2448 (N = 5 992 704) et k = 6, chaque matrice N × C en double précision pèse environ 288 Mo ; c'est pourquoi l'implémentation finale est **vectorisée avec NumPy** au lieu de boucler sur les pixels.

## 4. Fuzzy C-Means contre K-Means

| Aspect | Fuzzy C-Means | K-Means |
|---|---|---|
| Affectation | Chaque point a un degré d'appartenance à chaque cluster | Chaque point appartient à un seul cluster |
| Frontières | Gère les zones ambiguës ou de transition | Frontières nettes uniquement |
| Bruit / valeurs aberrantes | Moins sensible (affectations souples) | Sensible |
| Forme des clusters | Plus flexible en pratique | Suppose des clusters à peu près sphériques et de variance similaire |
| Coût | Plus élevé (appartenances à stocker et mettre à jour) | Plus faible |
| Paramètres | C, m, epsilon, max_iter | K, max_iter |

## 5. Avantages et limites

**Avantages**
* Segmentation souple : un pixel peut appartenir partiellement à plusieurs régions, ce qui convient aux **images satellitaires** aux transitions progressives (littoral, limite de végétation, ombres).
* Non supervisé : aucun jeu d'entraînement ni annotation requis.
* Simple à implémenter, peu de paramètres.

**Limites**
* **Sensible à l'initialisation** des appartenances (départ aléatoire) : les résultats, et le nombre d'itérations, varient d'une exécution à l'autre.
* Le **nombre de clusters doit être fixé à l'avance**, ce qui est difficile sur des scènes réelles.
* Le **coût de calcul** croît avec la taille de l'image et le nombre de clusters (271 itérations pour k = 6 ici).
* N'utilise que l'**intensité** (aucune information spatiale) : les pixels voisins ne sont pas pris en compte, d'où une sensibilité au **bruit** et des régions mouchetées (visibles sur les figures).
* Les classes dont les intensités se recouvrent ne peuvent pas être séparées avec un seul niveau de gris.

## Références
* L. A. Zadeh, *Fuzzy sets*, Information and Control, 8(3), 338-353, 1965.
* J. C. Dunn, *A fuzzy relative of the ISODATA process and its use in detecting compact well-separated clusters*, Journal of Cybernetics, 3(3), 32-57, 1973.
* J. C. Bezdek, *Pattern Recognition with Fuzzy Objective Function Algorithms*, Plenum Press, 1981.

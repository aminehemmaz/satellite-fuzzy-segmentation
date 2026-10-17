# Contexte : imagerie satellitaire, télédétection et segmentation d'images

[← Retour au README](../../README.fr.md) · [English](../background.md)

Synthèse des connaissances du domaine à la base du projet (chapitres 1 et 2 du mémoire).

## 1. Satellites et capteurs

* Un **satellite** gravite autour de la Terre (ou d'un autre corps). En télédétection, les satellites observent la Terre et collectent des données à distance, pour la surveillance de l'environnement, la météorologie, la cartographie et la gestion des ressources naturelles.
* **Orbites** : *géostationnaire* (environ 36 000 km, météorologie et communications) et *héliosynchrone* (600 à 1 000 km, observation de la Terre comme SPOT et Landsat).
* Un **capteur** enregistre l'énergie électromagnétique réfléchie ou émise par la surface terrestre.
  * Les **capteurs passifs** utilisent une énergie naturelle (lumière du soleil) : caméras optiques, infrarouges, multispectrales et hyperspectrales.
  * Les **capteurs actifs** émettent leur propre signal et analysent l'écho, indépendamment de la lumière du jour : radar (SAR) et LiDAR.
* Les capteurs opèrent dans le visible, l'infrarouge et les hyperfréquences. Caractéristiques clés : **résolution spatiale** (capacité à distinguer des détails), **résolution spectrale** (nombre de bandes), résolutions radiométrique et temporelle.
* Exemples de missions d'observation de la Terre : Landsat, SPOT, Sentinel-1/2, PROBA-V, NOAA, Meteosat.

## 2. Télédétection

La **télédétection** est l'ensemble des techniques permettant de déterminer à distance les propriétés d'objets naturels ou artificiels à partir des rayonnements qu'ils émettent ou réfléchissent. Elle couvre à la fois l'**acquisition des images** (principes physiques) et leur **analyse**.

Trois éléments de base : la **cible**, la **source d'énergie** et la **plate-forme / le capteur**. Sept maillons forment la chaîne : source d'énergie, interaction avec l'atmosphère, interaction avec la cible, capteur, traitement des données, analyse et interprétation, application pratique.

* **Signature spectrale** : la manière caractéristique dont un objet absorbe ou réfléchit le rayonnement selon la longueur d'onde ; elle fonde l'interprétation des images.
* **Applications** : agriculture (prévision des rendements, suivi des cultures), foresterie, urbanisme, changement climatique, gestion des catastrophes (glissements de terrain, inondations, évaluation des risques).
* **Intégration aux SIG** : la télédétection alimente les systèmes d'information géographique pour l'analyse de l'occupation des sols, de la végétation et des ressources.

## 3. Chaîne de traitement des images satellitaires

1. **Acquisition** : émission, interaction avec la surface, capture, transmission aux stations au sol.
2. **Prétraitement** : *correction radiométrique* (illumination, atmosphère, capteur), *correction géométrique* (mouvement du satellite, courbure de la Terre, alignement sur des cartes de référence), *correction spectrale* (calibration des bandes).
3. **Amélioration** : manipulation du contraste et des valeurs de pixels pour faciliter l'interprétation.
4. **Classification et segmentation** (ci-dessous).
5. **Produits** : cartes thématiques, rapports analytiques, modèles prédictifs.

## 4. Classification et segmentation

| Approche | Principe | Exemples |
|---|---|---|
| **Classification supervisée** | Un analyste fournit des échantillons étiquetés ; l'algorithme apprend les signatures spectrales | K plus proches voisins, machines à vecteurs de support (SVM) |
| **Classification non supervisée** | Les pixels sont regroupés par similarité numérique ; un analyste interprète ensuite les groupes | **K-Means**, ISODATA, **Fuzzy C-Means** |
| **Segmentation traditionnelle** | Seuillage (Otsu), histogrammes, croissance de régions, clustering | Otsu, croissance de régions, K-Means |
| **Segmentation par apprentissage profond** | Réseaux de neurones entraînés sur des images annotées | FCN, U-Net, Mask R-CNN |

Granularité de la segmentation : **sémantique** (une classe par pixel), **d'instance** (chaque objet séparé) et **panoptique** (les deux). Ce projet réalise une **segmentation sémantique non supervisée** avec le Fuzzy C-Means.

## Références
* W. G. Rees, *Physical Principles of Remote Sensing*, Cambridge University Press, 2e éd., 2001.
* T. M. Lillesand et R. W. Kiefer, *Remote Sensing and Image Interpretation*, 4e éd., John Wiley & Sons.
* F. Bonn et G. Rochon, *Précis de télédétection, Vol. 1 : Principes et méthodes*, Presses de l'Université du Québec / AUPELF, 1992.
* J. A. Richards, *Remote Sensing Digital Image Analysis*, Springer-Verlag, 2e éd., 1993.
* M.-C. Girard et C. M. Girard, *Traitement des données de télédétection*, Dunod, 1999.
* L. Provencher et J.-M. Dubois, *Précis de télédétection*, Presses de l'Université du Québec, 2007.
* J. Betbeder, *Évaluation des données de télédétection*, Université de Rennes 2, 2015.

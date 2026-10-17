# Data

🇬🇧 English · [🇫🇷 Français](#données)

This folder is intentionally empty: the input image and mask are **not stored** in this repository. Only illustrative figures showing tile 606 (satellite image, mask, grayscale, histograms) are included in [`docs/figures/`](../docs/figures); the dataset is distributed under the MIT licence (see below).

## What the main notebook expects

| File | Description |
|---|---|
| `606_sat1.jpg` | RGB satellite tile, 2448 × 2448 pixels |
| `606_mask.png` | Colour-coded ground-truth mask of the same tile (4 classes) |

The paths are set at the top of [`notebooks/fuzzy_c_means_satellite_segmentation.ipynb`](../notebooks/fuzzy_c_means_satellite_segmentation.ipynb) (`IMAGE_PATH`, `MASK_PATH`).

## Where the data comes from

The tile naming (`<id>_sat.jpg` and `<id>_mask.png`), the 2448 × 2448 size and the colour palette follow the **DeepGlobe Land Cover Classification** dataset:

> I. Demir *et al.*, **DeepGlobe 2018: A Challenge to Parse the Earth through Satellite Images**, CVPR Workshops, 2018.

The dataset copy used for this project is distributed under the **MIT licence**. To reproduce the experiment, download it from its source (and keep its licence notice), then copy tile `606` (image and mask) into this folder. The notebook was run on a re-saved copy named `606_sat1.jpg`; the original tile is `606_sat.jpg`. Using the original file may change the accuracy slightly.

You can also run the notebook on **any RGB image with a colour-coded mask** of the same kind: only `IMAGE_PATH` and `MASK_PATH` need to change.

## Experiments

The two notebooks in [`experiments/`](../experiments) also read a small crop named `TESTsat.jpg` from this folder. It is not included either; use any small satellite image.

The synthetic image used for the sanity check (`assets/synthetic_shapes.png`) was drawn for this project and is included.

---

# Données

[🇬🇧 English](#data) · 🇫🇷 Français

Ce dossier est volontairement vide : l'image d'entrée et le masque ne sont **pas stockés** dans ce dépôt. Seules des figures illustratives montrant la tuile 606 (image satellite, masque, niveaux de gris, histogrammes) figurent dans [`docs/figures/`](../docs/figures) ; le jeu de données est distribué sous licence MIT (voir plus bas).

## Ce qu'attend le notebook principal

| Fichier | Description |
|---|---|
| `606_sat1.jpg` | Tuile satellite RVB, 2448 × 2448 pixels |
| `606_mask.png` | Masque de vérité terrain coloré de la même tuile (4 classes) |

Les chemins sont définis en haut de [`notebooks/fuzzy_c_means_satellite_segmentation.ipynb`](../notebooks/fuzzy_c_means_satellite_segmentation.ipynb) (`IMAGE_PATH`, `MASK_PATH`).

## Origine des données

Le nommage des tuiles (`<id>_sat.jpg` et `<id>_mask.png`), la taille 2448 × 2448 et la palette de couleurs suivent le jeu de données **DeepGlobe Land Cover Classification** :

> I. Demir *et al.*, **DeepGlobe 2018: A Challenge to Parse the Earth through Satellite Images**, CVPR Workshops, 2018.

La copie du jeu de données utilisée pour ce projet est distribuée sous **licence MIT**. Pour reproduire l'expérience, la télécharger depuis sa source (en conservant sa mention de licence), puis copier la tuile `606` (image et masque) dans ce dossier. Le notebook a été exécuté sur une copie réenregistrée nommée `606_sat1.jpg` ; la tuile d'origine est `606_sat.jpg`. Utiliser le fichier d'origine peut modifier légèrement l'accuracy.

Vous pouvez aussi exécuter le notebook sur **n'importe quelle image RVB avec un masque coloré** du même type : seuls `IMAGE_PATH` et `MASK_PATH` sont à modifier.

## Expériences

Les deux notebooks de [`experiments/`](../experiments) lisent aussi un petit extrait nommé `TESTsat.jpg` dans ce dossier. Il n'est pas inclus non plus ; utilisez n'importe quelle petite image satellite.

L'image synthétique du test de validité (`assets/synthetic_shapes.png`) a été dessinée pour ce projet et est incluse.

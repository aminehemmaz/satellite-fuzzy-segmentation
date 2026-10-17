# Results and discussion

[← Back to README](../README.md) · [Français](fr/results.md)

## 1. Sanity check on a synthetic image

Fuzzy C-Means with 4 clusters (circle, triangle, rectangle and background) isolates the shapes correctly, which validates the implementation before moving to real data.

![Synthetic image segmentation](figures/synthetic_image_segmentation.png)

*Figure labels are in French, as produced for the thesis: "Image en niveaux de gris" = grayscale image, "Image segmentée FCM (4 classes)" = FCM-segmented image (4 classes).*

## 2. Satellite image: effect of the number of clusters

Same image, same parameters (m = 1.7, ε = 1e-5), only `k` changes.

| k | Iterations to converge | Accuracy (%) |
|---|---|---|
| 2 | 39 | 49.28 |
| 3 | 73 | 51.61 |
| **4** | 110 | **52.55** |
| 5 | 124 | 49.24 |
| 6 | 271 ¹ | 45.13 |

¹ **271 iterations** is the value recorded by the notebook and given in the text of the thesis (the thesis summary table lists 262, which does not match). Because the initialisation is random and unseeded, the exact count varies slightly between runs.

![Accuracy as a function of k](figures/accuracy_vs_k.png)

### Segmentation maps

| k = 2 | k = 3 | k = 4 |
|:---:|:---:|:---:|
| ![k=2](figures/segmentation_k2.png) | ![k=3](figures/segmentation_k3.png) | ![k=4](figures/segmentation_k4.png) |

| k = 5 | k = 6 |
|:---:|:---:|
| ![k=5](figures/segmentation_k5.png) | ![k=6](figures/segmentation_k6.png) |

*Colours are arbitrary cluster labels. The satellite image and its mask are not shown here, see [`data/README.md`](../data/README.md).*

## 3. Discussion

1. **k = 4 gives the best compromise**: it separates the main structures (water, fields, coastline) without fragmenting the image, and it reaches the highest accuracy (52.55 %).
2. **Too few clusters merge distinct zones** (k = 2 and k = 3).
3. **Too many clusters split homogeneous regions** (k = 5 and k = 6), and the algorithm needs many more iterations to converge (271 for k = 6 vs 39 for k = 2).
4. **The measured accuracy is modest.** The thesis itself notes that it reveals limits of Fuzzy C-Means: sensitivity to noise, to outliers and to the random initialisation.

### How to read the accuracy

* The ground-truth mask has **four classes**, and the largest one covers **57.42 %** of the image. A trivial classifier that always predicts that class would score 57.42 %, which is higher than the best Fuzzy C-Means score. Pixel accuracy is therefore a **coarse indicator** here, not a full quality measure; class-wise metrics such as IoU or F1 would be more informative.
* With one-to-one label matching, **any k greater than 4 leaves some clusters without a ground-truth class**. This lowers the accuracy by construction for k = 5 and k = 6, in addition to the visual over-segmentation described in the thesis.
* The algorithm only sees **one grayscale intensity per pixel**. Land-cover classes whose gray levels overlap (for instance bright sand and bright crops) cannot be separated without colour, texture or spatial context.

## 4. Take-aways

* Fuzzy C-Means is a simple, label-free baseline that produces a plausible coarse partition of a satellite scene, with no training data.
* The soft memberships are the main strength; the lack of **spatial information** and the dependence on **initialisation** are the main weaknesses.
* These observations motivate the extensions listed in the [README](../README.md#perspectives): hybridisation with **K-Means** (stable initialisation) and with **deep learning** (CNN), spatially-aware FCM variants, and richer features (colour bands, texture).

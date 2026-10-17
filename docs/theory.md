# Theory: Fuzzy Logic and Fuzzy C-Means

[← Back to README](../README.md) · [Français](fr/theory.md)

This document presents the concepts behind the project: from fuzzy sets to the **Fuzzy C-Means (FCM)** clustering algorithm and its use for image segmentation.

## 1. Fuzzy logic in a nutshell

**Fuzzy logic**, introduced by Lotfi Zadeh in 1965, extends classical Boolean logic. Instead of two truth values (*false = 0*, *true = 1*), a statement has a **degree of truth** in the interval [0, 1]. It is well suited to vague, uncertain or subjective notions such as "hot", "heavy" or "fast", and it bridges symbolic modelling (rules expressed in natural language) and numerical modelling.

### Classical sets vs fuzzy sets
| | Classical (crisp) set | Fuzzy set |
|---|---|---|
| Membership | binary: an element belongs or not (0 or 1) | graded: a value in [0, 1] |
| Example | "even numbers": 4 → 1, 5 → 0 | "hot temperatures": 25 °C → 0.4, 35 °C → 0.9 |
| Boundary | sharp | gradual |

A fuzzy set A over a universe X is defined by its **membership function** μ_A : X → [0, 1]. The **degree of membership** μ_A(x) measures how strongly x belongs to A.

### Fuzzy inference (for reference)
A classical fuzzy system has four stages:
1. **Fuzzification**: crisp inputs (e.g. 35 °C) are mapped to fuzzy sets ("warm", "hot").
2. **Fuzzy rule base**: `IF <condition> THEN <action>` rules written in natural language.
3. **Inference engine**: combines the rules activated by the membership degrees.
4. **Defuzzification**: the fuzzy output is converted back to a crisp value, most commonly with the *centre of gravity* (centroid) method.

FCM does not need a rule base: it only borrows the idea of **graded membership**.

## 2. Where Fuzzy C-Means sits in AI and machine learning

| Axis | Position of Fuzzy C-Means |
|---|---|
| Learning paradigm | **Unsupervised learning**: no labelled data is needed to train it |
| Task | **Clustering** (here: pixel clustering = image segmentation) |
| Assignment | **Soft / fuzzy clustering**: each sample belongs to every cluster with a degree |
| Family | **Soft computing / computational intelligence** (fuzzy logic) |
| Closest relative | **K-Means** (hard clustering), of which FCM is the fuzzy generalisation |
| Domain | Computer vision, image processing, remote sensing |

## 3. Fuzzy C-Means

Fuzzy C-Means (Dunn, 1973; generalised by Bezdek, 1981) partitions N data points x₁ … x_N into **C clusters**. Each point has a membership degree u_ij ∈ [0, 1] to each cluster i, with the constraint that the memberships of a point sum to 1:

$$
\sum_{i=1}^{C} u_{ij} = 1 \quad \forall j
$$

### Objective function
FCM minimises the weighted within-cluster sum of squared distances:

$$
J_m(U, c) = \sum_{i=1}^{C}\sum_{j=1}^{N} u_{ij}^{\,m}\,\lVert x_j - c_i \rVert^{2}, \qquad m > 1
$$

* **U** is the C × N membership matrix, **c_i** the centre (centroid) of cluster i.
* **m** is the **fuzziness index**. As m → 1 the partition becomes hard (K-Means-like); the larger m, the fuzzier the partition. This project uses **m = 1.7**.

### Alternating optimisation
Minimising J_m under the constraint gives two update rules, applied alternately:

**Centroid update** (membership-weighted mean):

$$
c_i = \frac{\sum_{j=1}^{N} u_{ij}^{\,m}\, x_j}{\sum_{j=1}^{N} u_{ij}^{\,m}}
$$

**Membership update** (the closer a point is to a centre, relative to the others, the higher its membership):

$$
u_{ij} = \frac{1}{\sum_{k=1}^{C}\left(\dfrac{\lVert x_j - c_i\rVert}{\lVert x_j - c_k\rVert}\right)^{\frac{2}{m-1}}}
$$

### Algorithm

```
Input : data x_1..x_N, number of clusters C, fuzziness m > 1, tolerance epsilon, max_iter
Output: final membership matrix U and centroids c

1. Initialise U randomly (each column sums to 1)
2. Repeat until ||U_new - U|| < epsilon or max_iter is reached:
     a. compute the centroids c_i from U             (centroid update)
     b. compute U_new from the centroids             (membership update)
3. Return U and c
```

In this project, the data points are **pixel intensities** (one feature per pixel, in [0, 1]), `C = k`, `epsilon = 1e-5` and `max_iter = 300`. The final **hard segmentation** assigns each pixel to the cluster with the highest membership (`argmax`).

### Complexity
Each iteration costs O(N · C), with N the number of pixels. For a 2448 × 2448 image (N = 5,992,704) and k = 6, every N × C double-precision matrix weighs about 288 MB, which is why the final implementation is **vectorised with NumPy** instead of looping over pixels.

## 4. Fuzzy C-Means vs K-Means

| Aspect | Fuzzy C-Means | K-Means |
|---|---|---|
| Assignment | Each point has a degree of membership to every cluster | Each point belongs to exactly one cluster |
| Boundaries | Handles ambiguous or transitional zones | Sharp boundaries only |
| Noise / outliers | Less sensitive (soft assignments) | Sensitive |
| Cluster shape | More flexible in practice | Assumes roughly spherical clusters of similar variance |
| Cost | Higher (memberships to store and update) | Lower |
| Parameters | C, m, epsilon, max_iter | K, max_iter |

## 5. Advantages and limitations

**Advantages**
* Soft segmentation: a pixel can belong partially to several regions, which suits **satellite images** with gradual transitions (coastlines, vegetation fronts, shadows).
* Unsupervised: no training set or annotation is required.
* Simple to implement, with few parameters.

**Limitations**
* **Sensitive to initialisation** of the memberships (random start), so results, and the number of iterations, vary between runs.
* The **number of clusters must be given in advance**, which is hard on real scenes.
* **Computational cost** grows with image size and number of clusters (271 iterations for k = 6 here).
* Uses **only intensity** (no spatial information): neighbouring pixels are not taken into account, which makes the result sensitive to **noise** and produces speckled regions (visible in the figures).
* Classes whose intensities overlap cannot be separated with a single grayscale feature.

## References
* L. A. Zadeh, *Fuzzy sets*, Information and Control, 8(3), 338-353, 1965.
* J. C. Dunn, *A fuzzy relative of the ISODATA process and its use in detecting compact well-separated clusters*, Journal of Cybernetics, 3(3), 32-57, 1973.
* J. C. Bezdek, *Pattern Recognition with Fuzzy Objective Function Algorithms*, Plenum Press, 1981.

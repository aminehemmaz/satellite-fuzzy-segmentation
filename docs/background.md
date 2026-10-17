# Background: satellite imagery, remote sensing and image segmentation

[← Back to README](../README.md) · [Français](fr/background.md)

A concise summary of the domain knowledge behind the project (chapters 1 and 2 of the thesis).

## 1. Satellites and sensors

* A **satellite** orbits the Earth (or another body). In remote sensing, satellites observe the Earth and collect data from a distance, for environment monitoring, meteorology, mapping and natural-resource management.
* **Orbits**: *geostationary* (about 36,000 km, meteorology and communications) and *sun-synchronous* (600 to 1,000 km, Earth observation such as SPOT and Landsat).
* A **sensor** records the electromagnetic energy reflected or emitted by the Earth's surface.
  * **Passive sensors** use natural energy (sunlight): optical, infrared, multispectral and hyperspectral cameras.
  * **Active sensors** emit their own signal and analyse the echo, independent of daylight: radar (SAR) and LiDAR.
* Sensors operate in the visible, infrared and microwave bands. Key characteristics: **spatial resolution** (ability to distinguish details), **spectral resolution** (number of bands), radiometric and temporal resolution.
* Examples of Earth-observation missions: Landsat, SPOT, Sentinel-1/2, PROBA-V, NOAA, Meteosat.

## 2. Remote sensing

**Remote sensing** is the set of techniques used to determine the properties of natural or artificial objects from a distance, through the radiation they emit or reflect. It covers both **image acquisition** (physical principles) and **image analysis**.

Three basic elements: the **target**, the **energy source** and the **platform / sensor**. Seven building blocks make up the chain: energy source, interaction with the atmosphere, interaction with the target, sensor, data processing, analysis and interpretation, practical application.

* **Spectral signature**: the characteristic way an object absorbs or reflects radiation across wavelengths; it is the basis of image interpretation.
* **Applications**: agriculture (yield forecasting, crop monitoring), forestry, urban planning, climate change, disaster management (landslides, floods, risk assessment).
* **GIS integration**: remote sensing feeds Geographic Information Systems for land-cover, vegetation and resource analysis.

## 3. Satellite image processing chain

1. **Acquisition**: emission, interaction with the surface, capture, transmission to ground stations.
2. **Pre-processing**: *radiometric correction* (illumination, atmosphere, sensor), *geometric correction* (satellite motion, Earth curvature, alignment with reference maps), *spectral correction* (band calibration).
3. **Enhancement**: contrast and pixel-value manipulation to ease interpretation.
4. **Classification and segmentation** (below).
5. **Products**: thematic maps, analytical reports, predictive models.

## 4. Classification and segmentation

| Approach | Principle | Examples |
|---|---|---|
| **Supervised classification** | An analyst provides labelled samples; the algorithm learns spectral signatures | K-Nearest Neighbours, Support Vector Machines |
| **Unsupervised classification** | Pixels are grouped by numerical similarity; an analyst interprets the groups afterwards | **K-Means**, ISODATA, **Fuzzy C-Means** |
| **Traditional segmentation** | Thresholding (Otsu), histograms, region growing, clustering | Otsu, region growing, K-Means |
| **Deep-learning segmentation** | Neural networks trained on annotated images | FCN, U-Net, Mask R-CNN |

Segmentation granularity: **semantic** (a class per pixel), **instance** (each object separated) and **panoptic** (both). This project performs a **semantic, unsupervised segmentation** with Fuzzy C-Means.

## References
* W. G. Rees, *Physical Principles of Remote Sensing*, Cambridge University Press, 2nd ed., 2001.
* T. M. Lillesand and R. W. Kiefer, *Remote Sensing and Image Interpretation*, 4th ed., John Wiley & Sons.
* F. Bonn and G. Rochon, *Précis de télédétection, Vol. 1: Principes et méthodes*, Presses de l'Université du Québec / AUPELF, 1992.
* J. A. Richards, *Remote Sensing Digital Image Analysis*, Springer-Verlag, 2nd ed., 1993.
* M.-C. Girard and C. M. Girard, *Traitement des données de télédétection*, Dunod, 1999.
* L. Provencher and J.-M. Dubois, *Précis de télédétection*, Presses de l'Université du Québec, 2007.
* J. Betbeder, *Évaluation des données de télédétection*, Université de Rennes 2, 2015.

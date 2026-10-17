"""
Segmentation d'image par Fuzzy C-Means (FCM)
Version optimisée pour VSCode avec :
- Gestion des chemins relatifs
- Sauvegarde automatique des résultats
- Progress bar pour le temps d'exécution
- Visualisation interactive
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, transform
import skfuzzy as fuzz
import time
import os
from tqdm import tqdm
from pathlib import Path

# Configuration
class Config:
    INPUT_PATH = "images/IMAGEsint.png"
    OUTPUT_DIR = "results_fcm"
    N_CLUSTERS = 4
    DOWNSCALE_FACTOR = 2  # Pour accélérer le traitement
    SHOW_PLOTS = True
    SAVE_RESULTS = True

def main():
    # Création du dossier de sortie
    Path(Config.OUTPUT_DIR).mkdir(exist_ok=True)
    
    # 1. Chargement de l'image
    print("\n1. Chargement de l'image...")
    image = io.imread(Config.INPUT_PATH)
    print(f"Dimensions originales : {image.shape}")

    # 2. Prétraitement
    print("\n2. Prétraitement...")
    if len(image.shape) == 3:
        image = image[:, :, :3]  # Suppression canal alpha si présent
        image_gray = color.rgb2gray(image)
    else:
        image_gray = image
        
    # Réduction de taille pour accélérer FCM
    if Config.DOWNSCALE_FACTOR > 1:
        image_gray = transform.rescale(image_gray, 1/Config.DOWNSCALE_FACTOR, anti_aliasing=True)
    
    image_norm = image_gray / np.max(image_gray)
    
    # 3. Clustering FCM
    print("\n3. Clustering FCM en cours...")
    pixels = image_norm.reshape(-1, 1)
    
    start_time = time.time()
    with tqdm(total=100, desc="Progression FCM") as pbar:
        _, u, _, _, _, _, _ = fuzz.cluster.cmeans(
            pixels.T,
            Config.N_CLUSTERS,
            m=1.5,  # Paramètre de flou optimisé
            error=0.01,
            maxiter=200,
            seed=42,
            init=None,
            callback=lambda _: pbar.update(5)
        )
    
    print(f"Temps d'exécution FCM : {time.time()-start_time:.2f}s")
    
    # 4. Post-traitement
    print("\n4. Post-traitement...")
    segmented = np.argmax(u, axis=0).reshape(image_gray.shape)
    
    if Config.DOWNSCALE_FACTOR > 1:
        segmented = transform.resize(
            segmented,
            image.shape[:2],
            order=0,
            preserve_range=True,
            anti_aliasing=False
        ).astype(int)
    
    # 5. Visualisation
    if Config.SHOW_PLOTS:
        plt.figure(figsize=(15, 5))
        plt.subplot(131)
        plt.imshow(image)
        plt.title("Image originale")
        
        plt.subplot(132)
        plt.imshow(image_gray, cmap='gray')
        plt.title("Niveaux de gris")
        
        plt.subplot(133)
        plt.imshow(segmented, cmap='jet')
        plt.title(f"Segmentation FCM ({Config.N_CLUSTERS} classes)")
        plt.colorbar()
        
        plt.tight_layout()
        plt.show()
    
    # 6. Sauvegarde
    if Config.SAVE_RESULTS:
        print("\n5. Sauvegarde des résultats...")
        np.save(os.path.join(Config.OUTPUT_DIR, "segmented.npy"), segmented)
        
        for k in range(Config.N_CLUSTERS):
            mask = (segmented == k).astype(np.uint8) * 255
            io.imsave(
                os.path.join(Config.OUTPUT_DIR, f"cluster_{k}.png"),
                mask,
                check_contrast=False
            )
        
        print(f"Résultats sauvegardés dans {Config.OUTPUT_DIR}")

if __name__ == "__main__":
    main()
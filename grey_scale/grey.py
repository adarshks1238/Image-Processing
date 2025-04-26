import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('gtr.jpg')
if image is None:
    raise ValueError("Image not found or unable to load. Please check the file path.")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)


fig, axs = plt.subplots(1, 2, figsize=(15, 5))
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image\n')
axs[1].imshow(image_gray, cmap='gray')
axs[1].set_title('Grayscale Image\n')

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()

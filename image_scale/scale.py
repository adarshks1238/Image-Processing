import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('gtr.jpg')
if image is None:
    raise ValueError("Image not found or unable to load. Please check the file path.")


image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


scale_factor_1 = 3.0  
scale_factor_2 = 1/2.0  


height, width = image_rgb.shape[:2]
print(f"Original Dimensions: {width} x {height}")
new_height1 = int(height * scale_factor_2)
new_width1 = int(width * scale_factor_2)
scaled_image = cv2.resize(image_rgb, (new_width1, new_height1), interpolation=cv2.INTER_AREA)


fig, axs = plt.subplots(1, 2, figsize=(15, 5))
axs[0].imshow(image_rgb)
axs[0].set_title(f'Original\n')
axs[1].imshow(scaled_image)
axs[1].set_title(f'Scaled\n')

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()

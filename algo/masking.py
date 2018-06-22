import numpy as np
import matplotlib.pyplot as plt

# Construct a random 50x50 RGB image    
image = np.random.random((50, 50, 3))

# Construct mask according to some condition;
# in this case, select all pixels with a red value > 0.3
#mask = image[..., 0] > 0.3
#mask = image[:, :, :]> 0.3
#mask = np.zeros_like(image, dtype=np.bool_)
mask = np.zeros([50, 50], dtype=np.bool_)
mask[:, 10] = 1
mask[:, 20] = 1
mask[10, :] = 1

print(mask)

# Set all masked pixels to zero
masked = image.copy()
masked[mask,  :] = 0

# Display original and masked images side-by-side
f, (ax0, ax1) = plt.subplots(1, 2)
ax0.imshow(image)
ax1.imshow(masked)
plt.show()

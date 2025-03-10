import numpy as np
import matplotlib.pyplot as plt

# img = np.ones((200, 200, 3), dtype=int)
# img[:] = (255, 0, 255)
# img[:, 100:] = (0, 0, 128)


img = np.full((200, 200, 3), 200)

# img = np.random.rand(50, 50, 3)


plt.imshow(img)
plt.show()

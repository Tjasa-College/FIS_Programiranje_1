import matplotlib.pyplot as plt
import numpy as np

os_x = np.arange(0, 2 * np.pi, 0.01)
sin_x = np.sin(os_x)
cos_x = np.cos(os_x)

plt.plot(os_x, sin_x)
plt.plot(os_x, cos_x, color='green')
plt.show()
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft

f = 10
t = np.arange(0, 2, 0.005)
y = np.sin(2*np.pi*f*t)
yfft = fft(y)
plt.subplot(121)
plt.plot(t, y)
plt.subplot(122)
plt.plot(abs(yfft))
plt.show()



import matplotlib.pyplot as plt
import numpy as np
from math import pi
from scipy import signal

Fs = 10
t = 4
n = np.arange(0, t, 1 / Fs)
f = 13
x = np.cos(2 * pi * f * n)
plt.subplot(2, 1, 1)
plt.title('Sinusodial Signal')
plt.plot(n, x)
plt.xlabel('Frequency')
plt.ylabel('Magnetidude')
plt.grid()

# sampling the signal
plt.subplot(2, 1, 2)
plt.title('Sampling equation')
plt.plot(t, x, linewidth=3, lable='x = np.cos(2*pi*f*n)')
plt.show()

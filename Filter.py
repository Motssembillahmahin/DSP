import matplotlib.pyplot as plt
import numpy as np
from math import pi
import scipy.signal as sig

plt.close('all')
# design frequency butter response
Fs = 100
n = 4
fc = np.array([8,12])
w_c = 2 * fc / Fs

[b, a] = sig.butter(n,w_c,btype='bandstop')

# frequency response

[w, h] = sig.freqz(b, a, worN=2000)
w = Fs * w / (2 * pi)
h_db = 20 * np.log10(abs(h))

plt.figure()
plt.plot(w, h_db)
plt.title('Bandstop')
plt.xlabel('magnitude')
plt.ylabel('Frequency')
plt.show()

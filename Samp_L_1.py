import numpy as np
import matplotlib.pyplot as plt

# Define the parameters of the sinusoidal signal
A = 1.0        # amplitude
f = 10.0       # frequency in Hz
phi = np.pi/2  # phase in radians

# Define the sampling rate and duration
fs = 100.0     # sampling rate in Hz
T = 1.0        # duration in seconds

# Generate the time axis
t = np.arange(0, T, 1/fs)

# Generate the sinusoidal signal
x = A*np.sin(2*np.pi*f*t + phi)

# Plot the analog signal
plt.figure()
plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Analog signal')
plt.grid()

# Sample the signal
Ts = 1/(2*f)   # Nyquist sampling period
n = np.arange(0, T/Ts)
xn = A*np.sin(2*np.pi*f*n*Ts + phi)

# Plot the sampled signal
plt.figure()
plt.stem(n*Ts, xn)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sampled signal')
plt.grid()

# Reconstruct the analog signal using ideal interpolation
t_interp = np.arange(0, T, 1/(10*fs))
x_interp = np.zeros_like(t_interp)

for i in range(len(n)):
    x_interp += xn[i]*np.sinc((t_interp - n[i]*Ts)*fs)

# Plot the reconstructed analog signal
plt.figure()
plt.plot(t_interp, x_interp)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Reconstructed analog signal')
plt.grid()

plt.show()

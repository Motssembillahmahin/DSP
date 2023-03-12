import infinite as infinite
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the signal
n = np.arange(0, 20)
x = np.power(1 / 16, n)
# Compute the z-transform
w, h = signal.freqz(x)
print(w);
# Define the numerator and denominator of the transfer function
num = [3, 0]
den = [1, 1]

# Compute the residues of the transfer function
r, p, k = signal.residue(num, den)

# Compute the first 10 samples of the inverse Z-transform
n1 = np.arange(0, 10)
x1 = np.zeros_like(n1, dtype=np.complex128)
for i in range(len(r)):
    x1 += r[i] * p[i] ** n1

# Print the result
print("Result of inverse function :")
print(x1)
# Create a new figure
fig, ax = plt.subplots()

print("Zeros :", r)

print("Poles", p)

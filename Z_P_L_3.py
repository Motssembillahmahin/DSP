import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the transfer function
num_1 = [1, 0, 1]  # numerator coefficients for equation_1
den_1 = [1, -1.5, 0.7]  # denominator coefficients for equation_1
H_1 = signal.TransferFunction(num_1, den_1)
#eqn_2
num_2 = [1, 0, 0, 1]  # numerator coefficients for equation_1
den_2 = [1, 0, 2, 0, 1]  # denominator coefficients for equation_1
H_2 = signal.TransferFunction(num_2, den_2)

#eqn_3
num_3 = [4, 8, 10]  # numerator coefficients for equation_1
den_3 = [2, 8, 18, 20]  # denominator coefficients for equation_1
H_3 = signal.TransferFunction(num_3, den_3)


# Compute the zeros, poles, and gain
#enq_1
zeros_1, poles_1, gain_1 = signal.tf2zpk(num_1, den_1)
#eqn_2
zeros_2, poles_2, gain_2 = signal.tf2zpk(num_2, den_2)
#eqn_3
zeros_3, poles_3, gain_3 = signal.tf2zpk(num_3, den_3)


# Print the zeros and poles for eqn = 1
print("Zeros of eqn_1 : ", zeros_1)
print("Poles of eqn_1 : ", poles_1)
# Print the zeros and poles for eqn = 2
print("Zeros of eqn_2 : ", zeros_2)
print("Poles of eqn_2 : ", poles_2)
# Print the zeros and poles for eqn = 3
print("Zeros of eqn_3 : ", zeros_3)
print("Poles of eqn_3 : ", poles_3)
# Plot the zeros and poles on the complex plane for eqn-1
plt.subplot(3,1,1)
plt.plot(np.real(zeros_1), np.imag(zeros_1), 'o', label='zeros')
plt.plot(np.real(poles_1), np.imag(poles_1), 'x', label='poles')
plt.grid(True)
plt.legend(loc = "lower right")
#plot the zeros and poles on the complex plane for eqn-2
plt.subplot(3,1,2)
plt.plot(np.real(zeros_2), np.imag(zeros_2), 'o', label='zeros_2')
plt.plot(np.real(poles_2), np.imag(poles_2), 'x', label='poles_2')
plt.grid(True)
plt.legend(loc = "lower right")

# Plot the zeros and poles on the complex plane for eqn-3
plt.subplot(3,1,3)
plt.plot(np.real(zeros_3), np.imag(zeros_3), 'o', label='zeros_3')
plt.plot(np.real(poles_3), np.imag(poles_3), 'x', label='poles_3')
plt.grid(True)
plt.legend(loc = "lower right")
plt.show()
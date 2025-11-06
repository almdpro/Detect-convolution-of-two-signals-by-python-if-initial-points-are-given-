import numpy as np
import matplotlib.pyplot as plt

# Define signals with initial points
x = np.array([1, 2, 1, -1])  # initial point is 2 (index 1)
h = np.array([1, 2, 3, 1])   # initial point is 1 (index 0)

# Convolution
y = np.convolve(x, h, mode='full')

# Time indices (adjusting for initial points)
time_x = np.arange(-1, 3)    # x initial at index 1 -> n=-1
time_h = np.arange(0, 4)     # h initial at index 0 -> n=0
time_y = np.arange(-1, 6)    # y initial at n=-1+0=-1

# Create figur

# Plot x[n]
plt.subplot(3, 1, 1)
plt.stem(time_x, x, linefmt='b-', markerfmt='bo', basefmt=' ', label='Stem')
plt.plot(time_x, x, 'r--o', alpha=0.7, label='Line')
plt.title('Signal x[n] (initial point at n=0 is 2)')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Plot h[n]
plt.subplot(3, 1, 2)
plt.stem(time_h, h,label='Stem')
plt.plot(time_h, h, 'm--o', alpha=0.7, label='Line')
plt.title('Signal h[n] (initial point at n=0 is 1)')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Plot convolution result
plt.subplot(3, 1, 3)
plt.stem(time_y, y, linefmt='c-', markerfmt='co', basefmt=' ', label='Stem')
plt.plot(time_y, y, 'orange', marker='o', linestyle='--', alpha=0.7, label='Line')
plt.title('Convolution y[n] = x[n] * h[n]')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Print values
print("Signal x[n]:", x)
print("Signal h[n]:", h)
print("Convolution y[n]:", y)
print("\nInitial points:")
print(f"x[n] initial at n=0: {x[1]}")  # Since second value is at n=0
print(f"h[n] initial at n=0: {h[0]}")
print(f"y[n] initial at n=0: {y[1]}")  # Corresponding to n=0 in result
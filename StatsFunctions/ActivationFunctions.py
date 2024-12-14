import numpy as np
import matplotlib.pyplot as plt

# Define activation functions
def sigmoid(x): return 1 / (1 + np.exp(-x))
def tanh(x): return np.tanh(x)
def relu(x): return np.maximum(0, x)
def leaky_relu(x, alpha=0.01): return np.where(x > 0, x, alpha * x)

# Input range
x = np.linspace(-10, 10, 400)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x, sigmoid(x), label="Sigmoid")
plt.plot(x, tanh(x), label="Tanh")
plt.plot(x, relu(x), label="ReLU")
plt.plot(x, leaky_relu(x), label="Leaky ReLU (α=0.01)")
plt.title("Activation Functions")
plt.legend()
plt.grid()
plt.show()

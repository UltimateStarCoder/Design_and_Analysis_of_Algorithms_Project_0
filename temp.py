import numpy as np
import matplotlib.pyplot as plt

# Define the range of n values
n = np.linspace(1, 1e6, 1000)  # n ranges from 1 to 1e6

# Define the functions
f_n = np.sqrt(n**5) + 3*n + 1   # f(n) = √n^5 + 3n + 1
g_n = 5 * n**2                  # g(n) = 5n^2

# Create a 2x2 grid of plots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Plot f(n) separately (Top left)
axs[0, 0].plot(n, f_n, label="f(n) = √n^5 + 3n + 1", color='blue')
axs[0, 0].set_title('f(n) = √n^5 + 3n + 1')
axs[0, 0].set_xlabel('n (Input Size)')
axs[0, 0].set_ylabel('Operations')
axs[0, 0].grid(True)

# Plot g(n) separately (Top right)
axs[0, 1].plot(n, g_n, label="g(n) = 5n^2", color='red')
axs[0, 1].set_title('g(n) = 5n^2')
axs[0, 1].set_xlabel('n (Input Size)')
axs[0, 1].set_ylabel('Operations')
axs[0, 1].grid(True)

# Plot both functions together on linear scale (Bottom left)
axs[1, 0].plot(n, f_n, label="f(n) = √n^5 + 3n + 1", color='blue')
axs[1, 0].plot(n, g_n, label="g(n) = 5n^2", color='red')
axs[1, 0].set_title('Comparison on Linear Scale')
axs[1, 0].set_xlabel('n (Input Size)')
axs[1, 0].set_ylabel('Operations')
axs[1, 0].legend(loc="upper left")
axs[1, 0].grid(True)

# Plot both functions together on log-log scale (Bottom right)
axs[1, 1].plot(n, f_n, label="f(n) = √n^5 + 3n + 1", color='blue')
axs[1, 1].plot(n, g_n, label="g(n) = 5n^2", color='red')
axs[1, 1].set_xscale('log')
axs[1, 1].set_yscale('log')
axs[1, 1].set_title('Comparison on Log-Log Scale')
axs[1, 1].set_xlabel('n (Input Size)')
axs[1, 1].set_ylabel('Operations')
axs[1, 1].legend(loc="upper left")
axs[1, 1].grid(True)

# Adjust layout for better spacing between plots
plt.tight_layout()

# Show the figure
plt.show()
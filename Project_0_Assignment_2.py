import numpy as np
import matplotlib.pyplot as plt

# Define f(n) = 1/2 * n * (n - 1) + 10
def f(n):
    return (1/2) * n * (n - 1) + 10

# Define g(n) = n^2
def g(n):
    return n ** 2

def limit(n):
    f_of_n = f(n)
    g_of_n = g(n)
    return f_of_n / g_of_n

# Function to plot graphs
def plot_functions(ax, xpoints, ypoints, function_label):
    ax.plot(xpoints, ypoints, label=function_label)

    # Add legend and grid
    ax.legend()
    ax.grid(True)

def main():
    # Create a figure with 2 subplots (1 row, 2 columns)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    # Plot for n from 1 to 10 on the first subplot
    n_to_ten = np.arange(1, 11)
    plot_functions(ax1, n_to_ten, limit(n_to_ten), 'limit (n) for n from 1 to 10')

    # Plot for n from 1 to 10^6 on the second subplot
    n_to_ten_pow_six = np.arange(1, np.power(10, 6) + 1)
    plot_functions(ax2, n_to_ten_pow_six, limit(n_to_ten_pow_six), 'limit (n) for n from 1 to 10^6')

    # Adjust layout and display the plots
    plt.tight_layout()
    plt.show()

# Execute the main function
if __name__ == "__main__":
    main()
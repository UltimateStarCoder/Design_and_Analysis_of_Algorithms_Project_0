import numpy as np
import matplotlib.pyplot as plt

# Define f(n) = 1/2 * n * (n - 1) + 10
def f(n):
    return (1/2) * n * (n - 1) + 10

# Define g(n) = n^2
def g(n):
    return n ** 2

# Function to plot f(n) and g(n)
def plot_functions(ax, xpoints, ypoints_f, ypoints_g, function_label_f, function_label_g):
    ax.plot(xpoints, ypoints_f, label=function_label_f)
    ax.plot(xpoints, ypoints_g, label=function_label_g, linestyle='--')
    
    # Add legend and grid
    ax.legend()
    ax.grid(True)

def main():
    # Create a figure with 2 subplots (1 row, 2 columns)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    # Plot for n from 1 to 10 on the first subplot
    n_to_ten = np.arange(1, 11)
    plot_functions(ax1, n_to_ten, f(n_to_ten), g(n_to_ten), 'f(n) for n from 1 to 10', 'g(n) for n from 1 to 10')

    # Plot for n from 1 to 10^6 on the second subplot
    n_to_ten_pow_six = np.arange(1, np.power(10, 6) + 1)
    plot_functions(ax2, n_to_ten_pow_six, f(n_to_ten_pow_six), g(n_to_ten_pow_six), 'f(n) for n from 1 to 10^6', 'g(n) for n from 1 to 10^6')
  
    # Adjust layout and display the plots
    plt.tight_layout()
    plt.show()

# Execute the main function
if __name__ == "__main__":
    main()
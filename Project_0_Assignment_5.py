import numpy as np
import matplotlib.pyplot as plt

# Define f(n) = log2(n)
def f(n):
    return np.log2(n)

# Define g(n) = log10(n)
def g(n):
    return np.log10(n)

def limit(n):
    f_of_n = f(n)
    g_of_n = g(n)
    return f_of_n / g_of_n

# Function to plot f(n) and g(n)
def plot_functions_f_g(ax, xpoints, ypoints_f, ypoints_g, function_label_f, function_label_g):
    ax.plot(xpoints, ypoints_f, label=function_label_f)
    ax.plot(xpoints, ypoints_g, label=function_label_g, linestyle='--')
    
    # Add legend and grid
    ax.legend()
    ax.grid(True)

def plot_functions_limit(ax, xpoints, ypoints, function_label):
    ax.plot(xpoints, ypoints, label=function_label)

    # Add legend and grid
    ax.legend()
    ax.grid(True)

def main():
     # Create a figure with 4 subplots (2 rows, 2 columns)
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # Unpack the axes array
    ax1, ax2, ax3, ax4 = axes.flatten()

    # Plot for n from 1 to 10 on the first subplot
    n_to_ten = np.arange(1, 11)
    plot_functions_f_g(ax1, n_to_ten, f(n_to_ten), g(n_to_ten), 'f(n) for n from 1 to 10', 'g(n) for n from 1 to 10')

    # Plot for n from 1 to 10^6 on the second subplot
    n_to_ten_pow_six = np.arange(1, np.power(10, 6) + 1)
    plot_functions_f_g(ax2, n_to_ten_pow_six, f(n_to_ten_pow_six), g(n_to_ten_pow_six), 'f(n) for n from 1 to 10^6', 'g(n) for n from 1 to 10^6')
  
#=============================================================================================================

    # Plot for n from 1 to 10 on the first subplot
    n_to_ten = np.arange(1, 11)
    plot_functions_limit(ax3, n_to_ten, limit(n_to_ten), 'limit (n) for n from 1 to 10')

    # Plot for n from 1 to 10^6 on the second subplot
    n_to_ten_pow_six = np.arange(1, np.power(10, 6) + 1)
    plot_functions_limit(ax4, n_to_ten_pow_six, limit(n_to_ten_pow_six), 'limit (n) for n from 1 to 10^6')

#=============================================================================================================
   # Add a title to the entire figure
    fig.suptitle('Comparison of Functions f(n), g(n), and Their Limits')

    # Adjust layout and display the plots
    plt.tight_layout()
    plt.show()

# Execute the main function
if __name__ == "__main__":
    main()
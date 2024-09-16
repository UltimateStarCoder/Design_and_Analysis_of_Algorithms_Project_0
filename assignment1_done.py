import numpy as np
import matplotlib.pyplot as plt

# Define f(n) = 1/2 * n * (n - 1) + 10
def f(n):
    return (1/2) * n * (n - 1) + 10

# Define g(n) = n^2
def g(n):
    return n ** 2

# Function to plot f(n) and g(n)
def plot_functions(xpoints, ypoints, function_label):
  
    # Plot
    plt.plot(xpoints,ypoints,label= function_label)
    
    # Add legend and grid
    plt.legend()
    plt.grid(True)

def main():

    # Plot for n from 1 to 10
    n_to_ten = np.arange(1, 11)
    plot_functions(n_to_ten, f(n_to_ten), 'f(n) for n from 1 to 10')

    # Plot for n from 1 to 10^6
    n_to_tem_pow_six = np.arange(1, np.power(10, 6) + 1)
    plot_functions(n_to_tem_pow_six, f(n_to_tem_pow_six), 'f(n) for n from 1 to 10^6')
  
    # Adjust layout and display the plots
    plt.tight_layout()
    plt.show()

# Execute the main function
if __name__ == "__main__":
    main()
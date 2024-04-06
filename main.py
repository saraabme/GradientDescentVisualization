import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys

# Function definitions
def f(x):
    """
    Define the function to minimize.
    
    Args:
        x (float): Input value.

    Returns:
        float: Output of the function f(x) = x^2.
    """
    return x**2

def df(x):
    """
    Derivative of the function f, representing the gradient.

    Args:
        x (float): Input value.

    Returns:
        float: Derivative f'(x) = 2x.
    """
    return 2*x

def gradient_descent(derivative_func, start_point, learning_rate=0.1, n_iter=50, tolerance=1e-05):
    """
    Perform gradient descent to find the minimum of a function.

    Args:
        derivative_func (function): Derivative function of the function to minimize.
        start_point (float): Starting point for the descent.
        learning_rate (float): Step size for each iteration.
        n_iter (int): Maximum number of iterations.
        tolerance (float): Convergence tolerance.

    Returns:
        list: History of points visited during descent.
    """
    history = [start_point]
    current_point = start_point
    
    for _ in range(n_iter):
        gradient = derivative_func(current_point)
        next_point = current_point - learning_rate * gradient
        if abs(next_point - current_point) < tolerance:
            break
        current_point = next_point
        history.append(current_point)
    
    return history

def main(start_point=10, learning_rate=0.1, n_iter=50):
    """
    Main function to run the gradient descent algorithm and visualize the results.

    Args:
        start_point (float): Starting point for the descent.
        learning_rate (float): Learning rate for the descent.
        n_iter (int): Number of iterations for the descent.
    """
    history = gradient_descent(df, start_point, learning_rate, n_iter)

    # Plotting and animation setup
    fig, ax = plt.subplots()
    x = np.linspace(-10, 10, 400)
    y = f(x)
    ax.plot(x, y, 'r', label='Function f(x) = x^2')
    point, = ax.plot([], [], 'bo', label='Gradient Descent')
    value_display = ax.text(0.02, 0.95, '', transform=ax.transAxes)

    def init():
        point.set_data([], [])
        value_display.set_text('')
        return point, value_display

    def update(frame):
        xdata = history[frame]
        ydata = f(history[frame])
        point.set_data(xdata, ydata)
        value_display.set_text(f'Minimizing: x={xdata:.2f}, f(x)={ydata:.2f}')
        return point, value_display

    ani = FuncAnimation(fig, update, frames=range(len(history)), init_func=init, blit=True, interval=200)

    plt.legend()
    plt.show()

if __name__ == "__main__":
    try:
        start_point = float(sys.argv[1]) if len(sys.argv) > 1 else 10
        learning_rate = float(sys.argv[2]) if len(sys.argv) > 2 else 0.1
        n_iter = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    except ValueError as e:
        print(f"Error: {e}. Please ensure that the inputs are of the correct type.")
        sys.exit(1)

    main(start_point, learning_rate, n_iter)

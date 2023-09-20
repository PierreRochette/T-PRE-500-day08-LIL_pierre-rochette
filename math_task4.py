import matplotlib.pyplot as plt 
import numpy as np
import math


def plot_fct (func, x_min, x_max) :

    x = np.linspace(x_min, x_max, 1000)
    y = np.vectorize(func)(x)

    #np.vectorize est utilisé pour appliquer à func chaque valeur de x.
    #cela m'a permis de résoudre un problème de code sur les valeurs
    # assignées à y. 

    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Graph')
    plt.show()

    return None


def f(x) : 
    return x ** 2 + x * 3 + 2


plot_fct(math.sin, 0, 50)
plot_fct(f, -100, 200)
plot_fct(lambda x: x**2, -10, 10)
plot_fct(lambda x: 1/x, -100, 100)

# Lambda allows to create a singular function that will only be
# used in this case. 
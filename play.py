import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))

def plot_mandelbrot(xmin, xmax, ymin, ymax, width=800, height=800, max_iter=256):
    _, _, mandelbrot_array = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.imshow(mandelbrot_array.T, extent=[xmin, xmax, ymin, ymax], cmap='hot') # type: ignore
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.show()

plot_mandelbrot(-2.0, 1.0, -1.5, 1.5)

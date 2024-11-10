import numpy as np
import matplotlib.pyplot as plt

width, height = 800, 800
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = 100 
def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n

image = np.zeros((height, width))

for x in range(width):
    for y in range(height):
   
        real = x_min + (x / width) * (x_max - x_min)
        imag = y_min + (y / height) * (y_max - y_min)
        c = complex(real, imag)
        color = mandelbrot(c)
        image[y, x] = color

plt.imshow(image, cmap='twilight', extent=(x_min, x_max, y_min, y_max))
plt.colorbar()
plt.title("Mandelbrot Set")
plt.show()

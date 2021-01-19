# Imports - standard modules
import scipy as sc
import matplotlib as mpl
from matplotlib import pyplot as plt

# Standard EM params
wl = 555  # Wavelength = 555 nm
phi = sc.pi / 4  # Initial phase = 90 degrees
ampl = 1  # Wave amplitute = 1

# calculate the wave
x = sc.linspace(0, 1, 256)
y = ampl * sc.sin(2 * sc.pi * x / (wl / 1000) + phi)

# Create the matplotlib figure
fig, ax = plt.subplots(1, 1)
plt.plot(x, y)
plt.show()

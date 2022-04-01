import numpy as np
import matplotlib.pyplot as plot

L = 0.6
H = 0.001

n = 30 # 3 10 30

An = lambda i: H * 32 / 3 / np.pi**2 / i**2 * np.sin(3*np.pi/4 * i)

x = np.linspace(0, L, 100)

explicit = np.append(np.linspace(0, 3*L/4, 75) * 4*H/3/L, (1-(np.linspace(3*L/4, L, 25)/L))*4*H)
fourier = np.zeros(100)
for i in range(1, n+1):
    fourier += An(i) * np.sin(i*np.pi*x/L)

plot.ylabel('Displacement (m)')
plot.xlabel('Position (m)')

plot.plot(x, explicit, label='Explicit')
plot.plot(x, fourier, label='n=%s Fourier series' % n)

plot.legend()

plot.show()


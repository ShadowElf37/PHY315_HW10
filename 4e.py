import numpy as np
import matplotlib.pyplot as plot

L = 0.6
H = 0.001
T = 160
m = 1.8 / 1000

n = 50 # 3 10 30

An = lambda i: H * 32 / 3 / np.pi**2 / i**2 * np.sin(3*np.pi/4 * i)

x = np.linspace(0, L, 100)

explicit = np.append(np.linspace(0, 3*L/4, 75) * 4*H/3/L, (1-(np.linspace(3*L/4, L, 25)/L))*4*H)

w_1 = np.sqrt(T/m)*np.pi/L

def F(t):
    fourier = np.zeros(100)
    for i in range(1, n+1):
        fourier += An(i) * np.sin(i*np.pi*x/L) * np.cos(i*w_1*t)
    return fourier

plot.ylabel('Displacement (m)')
plot.xlabel('Position (m)')

ts = [0, np.pi/4/w_1, np.pi/2/w_1, 3*np.pi/4/w_1, np.pi/w_1]

t = ts[4]

plot.plot(x, explicit, label='Explicit')
plot.plot(x, F(t), label='n=%s Fourier series' % n)

plot.text(0, 0.0007, 't=%s' % t, color='green')

plot.legend()

plot.show()


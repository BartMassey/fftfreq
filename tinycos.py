import numpy as np
from numpy.fft import *

sr = 24000
tf = 250
n = 512

ntf = 2 * tf / sr
b = round(ntf * n / 2)
freqs = fftfreq(n, d=1/sr)
f0 = freqs[b]
assert freqs[b] == -freqs[n - b]

fc = f0
# fc = f0 * (n - 1) / n

t = np.linspace(0, n / sr, n, dtype=np.float64)
y0 = np.cos(2 * np.pi * fc * t)

f = np.zeros(n, dtype=np.complex128)
f[b] = 1.0
f[n - b] = 1.0
y = 0.5 * n * ifft(f)

print(np.max(np.abs(y0 - np.real(y))))

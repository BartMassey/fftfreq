import argparse
import numpy as np
from numpy.fft import *

ap = argparse.ArgumentParser()
ap.add_argument("--correction", help="Frequency correction", action="store_true")
ap.add_argument("--plot", help="Output table for plotting", action="store_true")
ap.add_argument("--sr", help="Sample rate", type=int, default=24000)
ap.add_argument("--tf", help="Target frequency", type=float, default=250)
ap.add_argument("--n", help="Window size", type=int, default=512)
args = ap.parse_args()

# Imputed sample rate in samples/sec.
sr = args.sr
# Target frequency in cycles/sec.
tf = args.tf
assert 2 * tf < sr
# Window size in samples.
n = args.n

# Get a Nyquist target frequency.
ntf = 2 * tf / sr
# Get the closest FFT bin index.
b = round(ntf * n / 2)
# Get the bin center frequency.
freqs = fftfreq(n, d=1/sr)
f0 = freqs[b]
assert freqs[b] == -freqs[n - b]

if args.correction:
    # Correct the center frequency for time-domain cos().
    fc = f0 * (n - 1) / n
else:
    fc = f0

# Generate time-domain cos().
t = np.linspace(0, n / sr, n, dtype=np.float64)
y0 = np.cos(2 * np.pi * fc * t)

# Generate FFT cos().
f = np.zeros(n, dtype=np.complex128)
f[b] = 1.0
f[n - b] = 1.0
y = 0.5 * n * ifft(f)

# Show difference.
assert len(y) == len(y0)
if args.plot:
    for i in range(len(y)):
        print(i / sr, y0[i] - y[i].real)
    #   print(i / sr, abs(y[i].real) - np.abs(y[i]))
else:
    e = np.max(np.abs(y0 - np.real(y)))
    print(e)

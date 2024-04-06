import argparse
import numpy as np
from scipy.fft import *

ap = argparse.ArgumentParser()
ap.add_argument("--correction", help="Frequency correction", action="store_true")
ap.add_argument("--sr", help="Sample rate", type=int, default=24000)
ap.add_argument("--tf", help="Target frequency", type=int, default=250)
ap.add_argument("--w", help="Window size", type=int, default=512)
args = ap.parse_args()

# Imputed sample rate in samples/sec.
sr = args.sr
# Target frequency in cycles/sec.
tf = args.tf
assert 2 * tf < sr
# Window size in samples.
w = args.w

# Get a Nyquist target frequency.
ntf = 2 * tf / sr
# Get the closest FFT bin index.
b = round(ntf * w / 2)
# Get the bin center frequency.
freqs = fftfreq(w, d=1/sr)
f0 = freqs[b]
assert freqs[b] == -freqs[w - b]

if args.correction:
    # Correct the center frequency for time-domain cos().
    fc = f0 * (w - 1) / w
else:
    fc = f0

# Generate time-domain cos().
t = np.linspace(0, w / sr, w, dtype=np.float64)
y0 = np.cos(2 * np.pi * fc * t)

# Generate FFT cos().
f = np.zeros(w, dtype=np.complex128)
f[b] = 1.0
f[w - b] = 1.0
y = 0.5 * w * ifft(f)

# Show difference.
assert len(y) == len(y0)
for i in range(len(y)):
    print(i / sr, y0[i] - y[i].real)
#    print(i / sr, abs(y[i].real) - np.abs(y[i]))

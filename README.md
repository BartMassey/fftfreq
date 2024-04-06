# fftfreq-issue
Bart Massey 2024-04-09

This code *purports* to show that `scipy.fft.fftfreq` is
returning wrong answers. I don't believe it, but that's what
I'm seeing. Assistance appreciated.

* `cos.py` compares the time-domain and FFT-based generation
  of a cosine wave. See the code for details.

* `plotcos.sh` can be used to invoke `gnuplot` to show the
  differences graphically.

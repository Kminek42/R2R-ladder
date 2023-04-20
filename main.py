import ladder as ldr
import thd
import matplotlib.pyplot as plt
import numpy as np
import math
import time

y = []
x = []
a = []
compute_time = 10
t_stop = time.time_ns() * 1e-9 + compute_time
t_start = time.time_ns() * 1e-9
samples = 0
while t_start < t_stop:
    ladder1 = ldr.create_ladder(12, 1)

    data = thd.generate_wave(ladder1, 96)
    harmonics = []

    for i in range(1, 20):
        harmonics.append(thd.get_harmonic(data, i))
    
    a.append(100 * thd.get_thd(harmonics))
    samples += 1
    t_start = time.time_ns() * 1e-9
    if samples % 1000 == 0:
        print("Time remainig:", round(t_stop - t_start, 2), "[s]")


print("samples:", samples)
print("mean:", np.mean(a))
print("std:", np.std(a))
print("25%:", np.quantile(a, 0.25))
print("50%:", np.quantile(a, 0.50))
print("75%:", np.quantile(a, 0.75))
print("90%:", np.quantile(a, 0.90))
print("95%:", np.quantile(a, 0.95))
plt.hist(a, bins = math.isqrt(samples), density=True, stacked=True, cumulative=False)
plt.show()
plt.hist(a, bins = math.isqrt(samples), density=True, stacked=True, cumulative=True)
plt.show()
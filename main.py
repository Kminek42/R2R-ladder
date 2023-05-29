import ladder as ldr
import thd
import matplotlib.pyplot as plt
import numpy as np
import math
import time

y = []
x = []
a = []
compute_time = 4
t_stop = time.time() + compute_time
t_start = time.time()
samples = 0
while t_start < t_stop:
    ladder1 = ldr.create_ladder(8, 1)

    data = thd.generate_wave(ladder1, 96)
    harmonics = []

    for i in range(1, 20):
        harmonics.append(thd.get_harmonic(data, i))
    
    a.append(100 * thd.get_thd(harmonics))
    samples += 1
    t_start = time.time()
    if samples % 1000 == 0:
        print("Time remainig:", round(t_stop - t_start, 2), "[s]")


print("samples:", samples)
print("mean:", np.round(np.mean(a), 3))
print("std:", np.round(np.std(a), 3))
for i in range(5, 100, 5):
    print(f"{i}%: {np.round(np.quantile(a, i / 100), 3)}")

plt.hist(a, bins = math.isqrt(samples // 10), density=True, stacked=True, cumulative=False)
plt.xlabel("THD [%]")
plt.ylabel("Probability Density")
plt.show()
plt.hist(a, bins = math.isqrt(samples // 10), density=True, stacked=True, cumulative=True)
plt.xlabel("THD [%]")
plt.ylabel("Probability")
plt.show()
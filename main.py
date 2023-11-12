import ladder as ldr
import thd
import matplotlib.pyplot as plt
import numpy as np
import math
import time

def show_stats(a):
    samples = len(a)
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

# this script creates many ladders with certain resolution and tolerance
# and test their quality (THD)

a = []
compute_time = 30
t_stop = time.time() + compute_time
t_start = time.time()
samples = 0

while t_start < t_stop:
    # create ladder
    l1 = ldr.Ladder(resolution=8, tolerance=1)

    # generate samples based on ladder's resistors
    X = np.array(thd.generate_wave(l1, 512)) - 0.5
    A = np.abs(np.fft.fftshift(np.fft.fft(X)))

    # save THD of generated signal
    a.append(100 * thd.get_thd(A[len(A) // 2 + 1:]))

    samples += 1
    t_start = time.time()
    if samples % 1000 == 0:
        print("Time remainig:", round(t_stop - t_start, 2), "[s]")


show_stats(a)
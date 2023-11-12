import ladder as ldr
import math
import random


def generate_wave(ladder, samples, dithering = False):
    # this functoin generates one full sine cycle with length of N
    output = []
    res = ladder.resolution

    for i in range(samples):
        v = 0.5 + 0.4 * math.sin(2 * math.pi * i / samples)
        v = int(v * (2**res))
        output.append(ladder.get_output(v))

    return output


def get_harmonic(data, k):
    # this function calculates amplitude of k-th amplitude in signal

    N = len(data)
    a = 0
    b = 0

    for i in range(N):
        a += data[i] * math.sin(2 * math.pi * i * k / N)
        b += data[i] * math.cos(2 * math.pi * i * k / N)

    return 2 * math.sqrt(a * a + b * b) / N


def get_thd(amplitude_spectrum):
    # this function calculates THD based on amplitude spectrum
    return (sum(amplitude_spectrum[1:] ** 2) ** 0.5) / amplitude_spectrum[0]

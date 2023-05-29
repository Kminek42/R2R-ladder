import ladder as ldr
import math
import random


def generate_wave(ladder, samples, dithering = False):
    # this functoin generates one full sine cycle with length of N
    output = []
    res = len(ladder[0])

    for i in range(samples):
        v = 0.5 + 0.4 * math.sin(2 * math.pi * i / samples)
        v = int(v * (2**16))
        bit_reduction = 16 - res
        if dithering:
            v += random.randrange(0, 2**(bit_reduction))
        
        v //= (2 ** bit_reduction)
        pin = ldr.generate_pins(v, res)
        output.append(ldr.get_output(ladder, pin) - 0.5)

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


def get_thd(harmonics):
    # this function calculates THD based on harmonics' amplitude
    output = 0
    for i in range(len(harmonics) - 1):
        output += harmonics[i + 1] ** 2
    
    output = math.sqrt(output)
    return output / harmonics[0]

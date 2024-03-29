import random
import numpy as np

class Ladder:
    def __init__(self, resolution = 8, tolerance = 1, voltage = 1) -> None:
        self.resolution = resolution
        self.GND = np.random.normal(2, 2 * tolerance * 0.02)
        self.R = np.random.normal(1, tolerance * 0.01, resolution)
        self.R2 = np.random.normal(2, tolerance * 0.02, resolution)
        self.voltage = voltage


    def get_output(self, value):
        # this function calculates output voltage of R2R ladder based on
        # resistors' value

        pins = self.generate_pins(value)
        
        output = pins[0] * self.voltage * self.GND / (self.GND + self.R2[0])
        temp_res = 1 / (1 / self.GND + 1 / self.R2[0])

        for i in range(len(pins) - 1):
            temp_res += self.R[i]
            output += (pins[i + 1] * self.voltage - output) * temp_res / (self.R2[i + 1] + temp_res)
            temp_res = 1 / (1 / temp_res + 1 / self.R2[i + 1])

        return output


    def generate_pins(self, value):
        # this function converts decimal number into 
        # array with next digits of binary number starting from LSB to MSB

        value = int(value)
        output = []
        for i in range(self.resolution):
            output.append(value % 2)
            value //= 2
        
        return output


def create_ladder(resolution = 8, tolerance = 1):
    # this function generates pins' resistance based on their
    # target value and tolerance (tolerance is relative std)

    R = []
    R2 = []
    GND = np.random.normal(2, 2 * tolerance * 0.02)

    R = np.random.normal(1, tolerance * 0.01, resolution)
    R2 = np.random.normal(2, tolerance * 0.02, resolution)

    return [R, R2, GND]


def get_output(ladder, pins, voltage = 1):
    # this function calculates output voltage of R2R ladder based on
    # which inputs are on low and high state (from LSB to MSB)

    output = pins[0] * voltage * ladder[2] / (ladder[2] + ladder[1][0])
    temp_res = 1 / (1 / ladder[2] + 1 / ladder[1][0])

    for i in range(len(pins) - 1):
        temp_res += ladder[0][i]
        output += (pins[i + 1] * voltage - output) * temp_res / (ladder[1][i + 1] + temp_res)
        temp_res = 1 / (1 / temp_res + 1 / ladder[1][i + 1])

    return output


def generate_pins(value, resolution = 8):
    # this function converts decimal number into 
    # array with next digits of binary number starting from LSB to MSB

    output = []
    for i in range(resolution):
        output.append(value % 2)
        value //= 2
    
    return output

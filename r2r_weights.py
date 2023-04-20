import ladder as ldr
import matplotlib.pyplot as plt

# this script calculates weight of each pin and test 
# if they behave properly (weight[i] = 2^(i - res))

res = 16
ladder1 = ldr.create_ladder(res, 1)
y = []
y2 = []
for i in range(res):
    pin = ldr.generate_pins(2**i, res)
    print(i, ldr.get_output(ladder1, pin))
    y.append(ldr.get_output(ladder1, pin))

plt.plot(y)
plt.show()

for i in range(len(y) - 1):
    y2.append(y[i + 1] / y[i])

plt.plot(y2)
plt.show()

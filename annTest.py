import numpy as np
import matplotlib.pyplot as plt


def relu(x):
    return x * (x > 0)


def linear(x):
    return x


def activate(fx):
    plt.plot(x, relu(fx), "r", linewidth=4)
    plt.axvline(0, color="k")
    plt.axhline(0, color="k")
    plt.xticks(range(-5, 6))
    plt.grid(True)
    plt.show()


def linActivate(fx):
    plt.plot(x, linear(fx), "r", linewidth=4)
    plt.plot(x, np.sin(6 * x))
    plt.axvline(0, color="k")
    plt.axhline(0, color="k")
    plt.ylim((-2, 2))
    # plt.xticks(range(-5,6))
    plt.grid(True)
    plt.show()


# x = np.linspace(-5, 5, 200)
# activate(-2 * relu(-x + 0.5) + 1)

x = np.linspace(0, np.pi / 3, 200)

outputs = []

# hidden layer pair1
n1y1 = relu(6 * x)
n1y2 = relu(-1 * n1y1 + 0.7)
n1out = -1 * n1y2
outputs.append(n1out)

# hidden layer pair2
n2y1 = relu(3.5 * x - 0.42)
n2y2 = relu(-1 * n2y1 + 0.27)
n2out = -1 * n2y2
outputs.append(n2out)

# hidden layer pair3
n3y1 = relu(-3.5 * x + 1.35)
n3y2 = relu(-1 * n3y1 + 0.3)
n3out = -0.75 * n3y2
outputs.append(n3out)

# hidden layer pair8
n8y1 = relu(0 * x)
n8y2 = relu(0 * n8y1 + 1)
n8out = 0.97 * n8y2
outputs.append(n8out)

linActivate(sum(outputs))

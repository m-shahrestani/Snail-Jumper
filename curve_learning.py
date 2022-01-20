import matplotlib.pyplot as plt


def ploting():
    file = open("curve_learning.txt", "r")
    lines = file.readlines()
    min = []
    max = []
    avg = []
    for line in lines:
        data = line.split(" ")
        min.append(float(data[0]))
        max.append(float(data[1]))
        avg.append(float(data[2]))

    x = list(range(1, len(lines) + 1))
    plt.plot(x, min)
    plt.title("min neuron fitness")
    plt.show()
    plt.plot(x, max)
    plt.title("max neuron fitness")
    plt.show()
    plt.plot(x, avg)
    plt.title("avg neuron fitness")
    plt.show()


if __name__ == '__main__':
    ploting()

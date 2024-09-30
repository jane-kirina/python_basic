import matplotlib.pyplot as plt
import numpy as np


def func1(x):
    return -3 * x + 5


def func2(x):
    return 3 * x ** 2 + 3 * x - 6


def func3(x):
    return 2 * x ** 4 + x ** 3 - 6 * x ** 2 + 7 * x + 1


def func4(x):
    return (x ** 2) ** x


def create_graph(num_of_func):
    plt.rcParams["figure.figsize"] = [7, 3]
    plt.rcParams["figure.autolayout"] = True
    x = np.linspace(-10, 10, 100)
    plt.plot(x, functions[num_of_func](x), color='red')
    plt.show()


functions = {
    1: func1,
    2: func2,
    3: func3,
    4: func4
}

flag = True

while (flag):
    choice = input("What kind of function graph do you need?\n"
                   "1 -> -3x + 5\n"
                   "2 -> 3x^2 + 3x - 6\n"
                   "3 -> 2x^4 + x^3 - 6x^2 + 7x + 1\n"
                   "4 -> (x^2)^x\n"
                   "5 -> exit\n")
    if not choice.isdigit() or int(choice) not in range(1, 6):
        print("Please choose from the list")
    elif int(choice) == 5:
        flag = False
    else:
        create_graph(int(choice))

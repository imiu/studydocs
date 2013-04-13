import matplotlib.pyplot as plt
import numpy as np


def i5_loop(n):
    cnt = 0
    i = 1
    while i < 5 * n:
        cnt += 1
        i = i * 2
    return cnt


def plot_func():
    # plot common math function
    x_s = np.arange(0.1, 5., 0.1)
    x = np.arange(0.1, 1501., 1.)
    plt.plot(x_s, pow(x_s, 2), 'r-', label='x^2')
    plt.plot(x, pow(x, 0.5), 'b-', label='x^0.5')
    plt.plot(x, np.log2(x), 'g-', label='log2x')
    # plt.plot(x, x * np.log2(x), 'y-', label='n * log2x')
    # plt.plot(x, x, 'y-', label='n')

    # plot our function
    # plt.plot(range(0, 501), map(iin_loop, range(0, 501)), 'c-', label='i*i')
    # plt.plot(range(0, 501), map(ii4n_loop, range(0, 501)), 'c-', label='i*i')
    plt.plot(range(0, 1501), map(i5_loop, range(0, 1501)), 'c-', label='i*i')
    plt.legend()
    plt.show()


def plot_log_scale_func():
    x_s = np.arange(0.1, 25., 0.5)
    x = np.arange(0., 501., 1.)
    plt.plot(x_s, pow(2, x_s), 'r-', label='log2x')
    plt.plot(x, pow(x, 2), 'b-', label='x^2')
    plt.plot(x, x * np.log2(x), 'c-', label='xlog2x')
    plt.plot(x, x, 'g-', label='x')
    plt.plot(x, pow(x, 0.5), 'r-', label='x^0.5')
    plt.plot(x, np.log2(x), 'b-', label='log2x')

    plt.yscale('log')
    plt.xscale('log')
    plt.legend()
    plt.show()

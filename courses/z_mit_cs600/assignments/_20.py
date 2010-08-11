from matplotlib import pyplot
from numpy import array
import random, math

def flip_trial(num_flips):
    """docstring for flip_trial"""
    heads, tails = 0, 0
    for i in xrange(0, num_flips):
        coin = random.randint(0, 1)
        if coin == 0:
            heads += 1
        else:
            tails += 1
    return heads, tails

def sim_flip(num_flips, num_trials):
    """docstring for sim_flip"""
    diffs = []
    for i in range(0, num_trials):
        heads, tails = flip_trial(num_flips)
        diffs.append(abs(heads - tails))
    diffs = array(diffs)
    diff_mean = sum(diffs) / len(diffs)
    diff_percent = (diffs / float(num_flips)) * 100
    percent_mean = sum(diff_percent) / len(diff_percent)
    
    pyplot.hist(diffs)
    pyplot.axvline(diff_mean, label = 'Mean')
    pyplot.legend()
    title_string = str(num_flips) + ' flips ' + str(num_trials) + ' trials'
    pyplot.title(title_string)
    pyplot.xlabel('Difference between heads and tails')
    pyplot.ylabel('Number of Trials')
    pyplot.figure()
    pyplot.plot(diff_percent)
    pyplot.axhline(percent_mean, label = '...')
    pyplot.legend()
    pyplot.title(title_string)
    pyplot.xlabel('Trial Number')
    pyplot.ylabel('Percent Difference between heads and tails')

sim_flip(1000, 100)
pyplot.show()
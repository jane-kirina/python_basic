import math
from random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.special as sps
import warnings
from scipy.stats import kurtosis
from scipy.stats import skew

plt.rcParams["figure.figsize"] = (10.0, 7.0)
warnings.filterwarnings("ignore")

separator_header = '-------------------------'

'''Descriptive Statistics'''
print(separator_header + 'Descriptive Statistics')

# Mean
sample = [90, 63, 70, 87]

mean = sum(sample) / len(sample)
print(f'Mean: {mean}')

# Weighted Mean
weights = [.20, .20, .20, .40]
print(f'Sample: {sample}')
print(f'Weights: {weights}')

weighted_mean = sum(s * w for s, w in zip(sample, weights)) / sum(weights)
print(f'Weighted Mean: {weighted_mean}')

# Median
sample = [1, 2, 3, 4, 4, 4, 2, 7, 8, 3]


def median(values):
    ordered = sorted(values)
    print(ordered)
    length = len(ordered)
    mid = int(length / 2) - 1 if length % 2 == 0 else int(length / 2)

    if length % 2 == 0:
        return (ordered[mid] + ordered[mid + 1]) / 2.0
    else:
        return ordered[mid]


print(median(sample))

# Mode
from collections import defaultdict

sample = [1, 3, 3, 2, 6, 7, 2, 4, 5, 7]


def mode(values):
    counts = defaultdict(lambda: 0)

    for i in values:
        counts[i] += 1

    max_count = max(counts.values())
    modes = [i for i in set(values) if counts[i] == max_count]
    return modes


print(mode(sample))

# Variance

sample = [1, 2, 3, 6, 4, 0, 3, 9]


def variance(values):
    mean = sum(values) / len(values)
    var = sum((v - mean) ** 2 for v in values) / len(values)
    return var


print(variance(sample))

# Standard Deviation
from math import sqrt

sample = [1, 3, 5, 7, 1, 0, 2]


def variance(values):
    mean = sum(values) / len(values)
    var = sum((v - mean) ** 2 for v in values) / len(values)
    return var


def std_dev(values):
    return sqrt(variance(values))


print(std_dev(sample))

'''The Normal Distribution'''
print(separator_header + 'Descriptive Statistics')


def normal_distribution(x: float, std_dev: float) -> float:
    return (1.0 / (2.0 * math.pi * std_dev ** 2) ** 0.5) * math.exp(-1.0 * ((x - mean) ** 2 / (2.0 * std_dev ** 2)))


'''Analysis of the distribution of random variables'''
print(separator_header + 'Analysis of the distribution of random variables')
n = 10000
n_mean = 500
n_sigma = 1000

v = np.random.normal(n_mean, n_sigma, n)
v = pd.DataFrame(v, columns=['volume'])
v.volume = round(v.volume, 0)
print(v.head())

print('Estimation of mean, standard deviation and quantiles(using numpy and pandas)')

print('Mean: ' + str(v.volume.mean()))
print('Median: ' + str(v.volume.median()))
print('Mode: ')
print(v.volume.value_counts().nlargest(10))
print('Standard deviation(std): ' + str(v.volume.std()))
print('Quantile - median(0.5): ' + str(np.percentile(v.volume, 50)))
print('Quantile - 0.75: ' + str(np.percentile(v.volume, 75)))
print('Built-in pandas describe() method returns description of the data in the DataFrame:')
print(v.volume.describe())

print('Excess: ' + str(kurtosis(v.volume)))
print('Asymmetry: ' + str((v.volume)))

sns.distplot(v)
plt.title("Distribution histogram(using seaborn)")
plt.show()

v.volume.hist(bins=100)
plt.title("Distribution histogram(using pandas)")
plt.show()


def analysis(df=v, column="volume"):
    print("Basic metrics")
    print(df[column].describe())
    print(separator_header)

    print("Top 5 most popular metric values:")
    print(df[column].value_counts().nlargest(5))
    print(separator_header)

    print('Excess: ', kurtosis(df[column]))
    print('Asymmetry: ', skew(df[column]))

    sns.distplot(df[column])
    plt.title("Distribution histogram(using seaborn)")
    plt.show()


print('Analysis method:')
analysis()

'''Asymmetric distribution'''
print(separator_header + 'Asymmetric distribution')


def gamma_params(mean, std):
    shape = round((mean / std) ** 2, 4)
    scale = round((std ** 2) / mean, 4)
    return (shape, scale)


shape, scale = gamma_params(n_mean, n_sigma)
df = np.random.gamma(shape, scale, n)
df = pd.DataFrame(df, columns=["volume"])
df.volume = round(df.volume, 0)

print(df.head())
analysis(df=df, column="volume")

print('Comparison of two datasets')
print(v[v.volume < 0].count() / len(v))
print(df[df.volume < 0].count() / len(df))
sum_1 = v[v.volume >= np.percentile(v.volume, 50)].volume.sum() / 10 ** 6
sum_2 = df[df.volume >= np.percentile(df.volume,50)].volume.sum()/10**6
print(sum_1)
print(sum_2)


import warnings
from sklearn.datasets import load_boston
plt.rcParams["figure.figsize"] = (10.0, 7.0)
warnings.filterwarnings("ignore")
boston = load_boston()

print(boston.DESCR)






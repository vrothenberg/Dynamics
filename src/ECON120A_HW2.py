import numpy as np
from scipy import stats 
import math 

def quartiles(data):
    data = np.sort(data)
    n = len(data)
    print("Range: %.4f" % (data[-1] - data[0]))

    q1_pos = (n + 1) * 0.25
    pos1 = math.floor(q1_pos)
    rem = q1_pos - pos1
    q1 = data[pos1-1] + rem * (data[pos1] - data[pos1-1])

    q3_pos = (n+1) * 0.75
    pos3 = math.floor(q3_pos)
    rem = q3_pos - pos3 
    q3 = data[pos3-1] + rem * (data[pos3] - data[pos3-1])

    iqr = q3 - q1
    print("Quartile 1: %.4f" % q1)
    print("Quartile 3: %.4f" % q3)
    print("IQR: %f" % iqr)

    lower = q1 - 1.5 * iqr
    print("Lower limit: %.4f" % lower)

    num_lower = sum([1 for element in data if element < lower])
    print("Num lower: %.4f" % num_lower)

    upper = q3 + 1.5 * iqr
    print("Upper limit: %.4f" % upper)

    num_upper = sum([1 for element in data if element > upper])
    print("Num upper: %.4f" % num_upper)

def sample_variance(data):
    mean = np.mean(data)
    total = 0
    for element in data:
        total += (element - mean)**2
    return total / (len(data) - 1)

def summary(data):
    np.sort(data)
    n = len(data)

    print("Minimum: %.4f" % min(data))

    q1_pos = (n + 1) * 0.25
    pos1 = math.floor(q1_pos)
    rem = q1_pos - pos1
    q1 = data[pos1-1] + rem * (data[pos1] - data[pos1-1])

    q3_pos = (n+1) * 0.75
    pos3 = math.floor(q3_pos)
    rem = q3_pos - pos3 
    q3 = data[pos3-1] + rem * (data[pos3] - data[pos3-1])

    iqr = q3 - q1
    print("Quartile 1: %.4f" % q1)
    print("Median: %.4f" % np.median(data))
    print("Quartile 3: %.4f" % q3)
    print("Maximum: %.4f" % max(data))


data = np.sort(np.array([7,2,5,4,7,3,1,3,2,3,5,2,3,4,2,1,6,6,3,1]))
print(data)

print("Mean: %.4f" % np.mean(data))
print("Median: %.4f" % np.median(data))
print("Mode: %.4f" % stats.mode(data)[0][0])
print("Variance: %.4f" % sample_variance(data))
print("Std: %.4f" % sample_variance(data) ** (1/2))

quartiles(data)

summary(data)

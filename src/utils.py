
import sys

def accuracy(lst, truth):
    s = 0
    for value in lst:
        s += value / truth
    return round((1-abs(((s / len(lst)))-1))*100, 3)

def mre(lst, truth):
    s = 0
    for value in lst:
        s += abs(value-truth)/truth
    return round(s/len(lst)*100, 3)


def mae(lst, truth):
    s = 0
    for value in lst:
        s += abs(value-truth)
    return round(s/len(lst), 3)

def mad(lst):
    avg = sum(lst)/len(lst)
    s = 0
    for v in lst:
        s += abs(v-avg)
    return round(s/len(lst), 3)

def max_deviation(lst):
    avg = sum(lst)/len(lst)
    return round(max([abs(v-avg) for v in lst]), 3)

def num_bits(lst):
    s = 0
    for value in lst:
        for i, char in enumerate(str(bin(value))):
            if char == '1':
                s += len(bin(value))-i
                break
    return s/len(lst)

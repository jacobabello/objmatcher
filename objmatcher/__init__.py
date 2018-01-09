from __future__ import print_function
from math import*
from collections import OrderedDict
import numpy as np


def match(obj1, obj2):
    vector = OrderedDict()
    similarity_average = []

    for key, value in obj1.iteritems():
        vector.update({key: str.split(value)})

    for key, value in obj2.iteritems():
        vector.update({key: vector[key] + list(set(str.split(value)) - set(vector[key]))})

    for key in vector.keys():
        vector.update({key + "Vector": list(np.zeros(len(vector[key]), dtype=np.int))})
        print(obj1[key])

    print(vector)


def get_similarity(x, y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = round(sqrt(sum([a*a for a in x])), 3) * round(sqrt(sum([a*a for a in y])), 3)

    return numerator/float(denominator)



# print(numpy.mean([cosine_similarity([2, 2, 2, 3, 3, 2, 2], [2, 2, 2, 2, 2, 2, 2]), 1]))
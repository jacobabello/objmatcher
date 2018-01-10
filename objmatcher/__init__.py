from __future__ import print_function
from math import*
from collections import OrderedDict, Counter
import numpy as np


def match(obj1, obj2):
    word_lists = OrderedDict()
    similarity_average = []

    for key, value in obj1.iteritems():
        word_lists.update({key: str.split(value)})

    for key, value in obj2.iteritems():
        word_lists.update({key: word_lists[key] + list(set(str.split(value)) - set(word_lists[key]))})

    print(word_lists)

    for _ in word_lists:
        vector1 = list(np.zeros(len(word_lists[_]), dtype=np.int))
        vector2 = list(np.zeros(len(word_lists[_]), dtype=np.int))

        print(word_lists[_])
        print(str.split(obj1[_]))
        print(str.split(obj2[_]))

        for x in range(len(word_lists[_])):
            if word_lists[_][x] in str.split(obj1[_]):
                vector1[x] = 1
            if word_lists[_][x] in str.split(obj2[_]):
                if vector1[x] == 1:
                    vector1[x] = 2
                    vector2[x] = 2
                else:
                    vector2[x] = 1

        similarity_average.append(get_similarity(vector1, vector2))

    return round(np.mean(similarity_average), 3)


def get_similarity(x, y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)


def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)




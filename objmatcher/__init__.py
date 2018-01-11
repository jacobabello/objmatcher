from __future__ import print_function
from math import*
from collections import OrderedDict, Counter
import numpy as np


def match(obj1, obj2):
    word_lists = OrderedDict()
    similarity_average_list = []

    for key, value in obj1.iteritems():
        word_lists.update({key: [str.split(x) for x in value]})

    for key, value in obj2.iteritems():
        for index in range(len(word_lists[key])):
            for x in range(len(value)):
                word_lists[key][index] += list(set(str.split(value[x])) - set(word_lists[key][index]))

    for key in word_lists:
        for x in range(len(word_lists[key])):
            vector1 = list(np.zeros(len(word_lists[key][x]), dtype=np.int))
            vector2 = list(np.zeros(len(word_lists[key][x]), dtype=np.int))

            print(word_lists[key][x])
            print(obj1[key][x])
            print(obj2[key][0])

            for index in range(len(word_lists[key][x])):
                if word_lists[key][x][index] in str.split(obj1[key][x]):
                    vector1[index] = 1
                if word_lists[key][x][index] in str.split(obj2[key][0]):
                    if vector1[index] == 1:
                        vector1[index] = 2
                        vector2[index] = 2
                    else:
                        vector2[index] = 1


            print(vector1)
            print(vector2)
            print(get_similarity(vector1, vector2))
            print('---')


def get_similarity(x, y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)


def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)




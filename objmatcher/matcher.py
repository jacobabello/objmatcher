from __future__ import print_function

import json
from math import*
from collections import OrderedDict
import numpy as np
import re
import sys
from data import Data
import distance


class Matcher(object):
    def __init__(self, object1, object2):
        """
        :type object1 Data
        :type object2 Data
        """
        self.object1 = object1
        self.object2 = object2
        self.top_similarity_score = 0.0

    def match(self):
        word_lists = OrderedDict()

        print(self.object1.to_json())
        print(self.object2.to_json())

        for key, value in self.object1.to_json().iteritems():
            if key in self.object2.to_json().keys():
                word_lists.update({key: [str.split(self.__remove_special_char(x)) for x in value]})

        for key, value in self.object2.to_json().iteritems():
            if key in self.object1.to_json().keys():
                if key in word_lists:
                    for index in range(len(word_lists[key])):
                        for x in range(len(value)):
                            word_lists[key][index] += list(set(str.split(self.__remove_special_char(value[x]))) - set(word_lists[key][index]))

        for key in word_lists:
            for x in range(len(word_lists[key])):
                for master_word in self.object2.to_json()[key]:
                    vector1 = list(np.zeros(len(word_lists[key][x]), dtype=np.int))
                    vector2 = list(np.zeros(len(word_lists[key][x]), dtype=np.int))

                    print(self.object1.to_json()[key][x])
                    print(master_word)

                    for index in range(len(word_lists[key][x])):
                        if word_lists[key][x][index] in str.split(self.__remove_special_char(self.object1.to_json()[key][x])):
                            vector1[index] = 1
                        if word_lists[key][x][index] in str.split(self.__remove_special_char(master_word)):
                            if vector1[index] == 1:
                                vector1[index] = 2
                                vector2[index] = 2
                            else:
                                vector2[index] = 1

                    print(vector1)
                    print(vector2)

            print(word_lists[key])
            print(len(word_lists[key]))
            print('---------------------------------------')

    def get_scores(self):
        pass

    def get_average_scores(self):
        pass

    @staticmethod
    def __compare(string, word_list):
        pass

    @staticmethod
    def __remove_special_char(string):
        string = str(string)
        string = str(string.upper())

        return re.sub('[^A-Za-z0-9]+', ' ', string)

    @staticmethod
    def __get_similarity(x, y):
        def square_rooted(x):
            return round(sqrt(sum([a * a for a in x])), 3)

        numerator = sum(a * b for a, b in zip(x, y))
        denominator = square_rooted(x) * square_rooted(y)
        return round(numerator / float(denominator), 3)

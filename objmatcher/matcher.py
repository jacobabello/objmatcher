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
        self.average_score = []
        self.results = OrderedDict()

    def match(self):
        word_lists = OrderedDict()

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

                    for index in range(len(word_lists[key][x])):
                        if word_lists[key][x][index] in str.split(self.__remove_special_char(self.object1.to_json()[key][x])):
                            vector1[index] = 1
                        if word_lists[key][x][index] in str.split(self.__remove_special_char(master_word)):
                            if vector1[index] == 1:
                                vector1[index] = 2
                                vector2[index] = 2
                            else:
                                vector2[index] = 1

                    similarity = self.__get_similarity(vector1, vector2)

                    if similarity != 0.0:
                        self.__add_similarity_score(key, self.object1.to_json()[key][x], similarity)

    def __add_similarity_score(self, key, word, score):
        self.average_score.append(score)
        if key in self.results:
            self.results[key].append({word: score})
        else:
            self.results[key] = [{word: score}]

    def get_similarity_score(self):
        return self.results

    def get_average_scores(self):
        if len(self.average_score) == 0:
            return 0.0

        return round(sum(self.average_score)/len(self.average_score), 3)

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

from __future__ import print_function

import json
from math import*
from collections import OrderedDict
import numpy as np
import re


def match(obj1, obj2):
    def remove_special_char(string):
        string = str(string)
        string = str(string.upper())
        return re.sub('[^A-Za-z0-9]+', ' ', string)

    word_lists = OrderedDict()

    for key, value in obj1.iteritems():
        if key in obj2.keys():
            word_lists.update({key: [str.split(remove_special_char(x)) for x in value]})

    for key, value in obj2.iteritems():
        if key in obj1.keys():
            if key in word_lists:
                for index in range(len(word_lists[key])):
                    for x in range(len(value)):
                        word_lists[key][index] += list(set(str.split(remove_special_char(value[x]))) - set(word_lists[key][index]))

    match_result = MatchResult()

    for key in word_lists:
        top_similarity_score = 0.0

        for x in range(len(word_lists[key])):
            vector1 = list(np.zeros(len(word_lists[key][x]), dtype=np.int))
            vector2 = list(np.zeros(len(word_lists[key][x]), dtype=np.int))

            for index in range(len(word_lists[key][x])):
                if word_lists[key][x][index] in str.split(remove_special_char(obj1[key][x])):
                    vector1[index] = 1

                if word_lists[key][x][index] in str.split(remove_special_char(obj2[key][0])):
                    if vector1[index] == 1:
                        vector1[index] = 2
                        vector2[index] = 2
                    else:
                        vector2[index] = 1

            similarity = get_similarity(vector1, vector2)
            if similarity > top_similarity_score:
                top_similarity_score = similarity

        match_result._add_result_by_key(key, top_similarity_score)

    return match_result


def get_similarity(x, y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)


def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)


class Data(object):

    def __init__(self):
        self.metadata = OrderedDict()

    def add_meta_data(self, key, value):
        if key in self.metadata.keys():
            if value not in self.metadata[key]:
                self.metadata[key].append(value)
        else:
            self.metadata[key] = [value]

    def get_all_meta_data(self):
        return self.metadata.keys()

    def get_meta_data_by_key(self, key):
        try:
            return self.metadata[key]
        except KeyError:
            raise KeyError()

    def to_json(self):
        return json.loads(json.dumps(self.metadata))


class MatchResult(object):

    def __init__(self):
        self.results = OrderedDict()
        self.average_scores = []

    def _add_result_by_key(self, key, result):
        self.results[key] = result
        self.average_scores.append(result)

    def get_scores(self):
        return self.results

    def get_score_by_key(self, key):
        try:
            return self.results[key]
        except KeyError:
            raise KeyError()

    def get_average_scores(self):
        return round(np.mean(self.average_scores), 3)

    def get_keys(self):
        return self.results.keys()
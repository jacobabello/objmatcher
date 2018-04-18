from __future__ import print_function
from data import Data
from matcher import Matcher


class ObjectMatcher(object):

    def generate_object(self):
        return Data()

    def match(self, object1, object2):
        """
        :type object1 Data
        :type object2 Data
        """

        return Matcher(object1, object2).match()

import unittest
from objmatcher import ObjectMatcher
from objmatcher.matcher import Matcher


class test_matcher(unittest.TestCase):
    def setUp(self):
        self.object_matcher = ObjectMatcher()

    def test_matching_object_with_high_similarity(self):
        data1 = self.object_matcher.generate_object()
        data1.add_meta_data('name', 'bee gees')
        data1.add_meta_data('song', 'how deep is your love')
        data1.add_meta_data('song', 'should be dancing')

        data2 = self.object_matcher.generate_object()
        data2.add_meta_data('name', 'bee gees')
        data2.add_meta_data('song', 'how deep is your love')
        data2.add_meta_data('song', 'you should be dancin')
        data2.add_meta_data('song', 'stayin\' alive')
        data2.add_meta_data('genre', 'disco')
        data2.add_meta_data('genre', 'pop')

        matcher = Matcher(data1, data2)
        matcher.match()

        self.assertGreaterEqual(matcher.get_average_scores(), 0.9)

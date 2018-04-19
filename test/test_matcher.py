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

    def test_matching_data1_has_more_key(self):
        data1 = self.object_matcher.generate_object()
        data1.add_meta_data('name', 'red hot chili peppers')
        data1.add_meta_data('song', 'can\'t stop')
        data1.add_meta_data('song', 'hey oh!')

        data2 = self.object_matcher.generate_object()
        data2.add_meta_data('name', 'red hot chili peppers')
        data2.add_meta_data('song', 'can\'t stop')
        data2.add_meta_data('song', 'snow hey oh!')
        data2.add_meta_data('song', 'californication')
        data2.add_meta_data('vocalist', 'Anthony Kiedis')

        matcher = Matcher(data1, data2)
        matcher.match()

        self.assertGreaterEqual(matcher.get_average_scores(), 0.9)

    def test_handling_blank_value(self):
        data1 = self.object_matcher.generate_object()
        data1.add_meta_data('name', 'red hot chili peppers')
        data1.add_meta_data('song', 'can\'t stop')
        data1.add_meta_data('song', 'hey oh!')
        data1.add_meta_data('vocalist', '')

        data2 = self.object_matcher.generate_object()
        data2.add_meta_data('name', 'red hot chili peppers')
        data2.add_meta_data('song', 'can\'t stop')
        data2.add_meta_data('song', 'snow hey oh!')
        data2.add_meta_data('song', 'californication')

        matcher = Matcher(data1, data2)
        matcher.match()

        self.assertGreaterEqual(matcher.get_average_scores(), 0.9)

    def test_completely_different_data(self):
        data1 = self.object_matcher.generate_object()
        data1.add_meta_data('name', 'foo fighters')
        data1.add_meta_data('song', 'best of you')

        data2 = self.object_matcher.generate_object()
        data2.add_meta_data('name', 'nirvana')
        data2.add_meta_data('song', 'smell like teen spirit')
        data2.add_meta_data('genre', 'grunge')

        matcher = Matcher(data1, data2)
        matcher.match()

        self.assertEqual(matcher.get_average_scores(), 0.0)

    def test_high_match_because_only_one_data_is_matching(self):
        data1 = self.object_matcher.generate_object()
        data1.add_meta_data('name', 'foo fighters')
        data1.add_meta_data('song', 'best of you')
        data1.add_meta_data('song', 'the pretender')
        data1.add_meta_data('genre', 'grunge')

        data2 = self.object_matcher.generate_object()
        data2.add_meta_data('name', 'nirvana')
        data2.add_meta_data('song', 'smell like teen spirit')
        data2.add_meta_data('genre', 'grunge')

        matcher = Matcher(data1, data2)
        matcher.match()

        self.assertLess(matcher.get_average_scores(), 0.3)

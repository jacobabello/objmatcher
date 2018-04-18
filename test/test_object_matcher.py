import unittest
from objmatcher import ObjectMatcher
from objmatcher.data import Data


class test_object_matcher(unittest.TestCase):
    def setUp(self):
        self.object_test = ObjectMatcher()

    def test_it_can_generate_objects_with_objdata_type(self):
        self.assertIsInstance(self.object_test.generate_object(), Data)

    def test_it_can_get_all_generated_objects(self):
        generated_objects = self.object_test.get_all_objects()
        self.assertIsInstance(generated_objects, list)

        for object in generated_objects:
            self.assertIsInstance(object, Data)

    def test_matching_single_object_to_all_generated_objects(self):
        data1 = self.object_test.generate_object()
        data1.add_meta_data('name', 'kiss')
        data1.add_meta_data('song', 'detroit rock city')

        data2 = self.object_test.generate_object()
        data2.add_meta_data('name', 'KISS')
        data2.add_meta_data('song', 'detroit rock city')

        data3 = self.object_test.generate_object()
        data3.add_meta_data('name', 'kizz')
        data3.add_meta_data('song', 'detroit rock city')

        self.object_test.match_generated_objects_to(data1)
        remaining_data = self.object_test.get_all_objects()

        self.assertEqual(len(remaining_data), 2)

        for _ in remaining_data:
            self.assertIsInstance(_, Data)
            self.assertNotEqual(data1, _, 'not data1')
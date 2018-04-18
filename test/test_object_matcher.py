import unittest
from objmatcher import ObjectMatcher
from objmatcher.data import Data


class test_matcher(unittest.TestCase):
    def setUp(self):
        self.object_test = ObjectMatcher()

    def test_it_can_generate_objects_with_objdata_type(self):
        self.assertIsInstance(self.object_test.generate_object(), Data)

    def test_it_can_get_all_generated_objects(self):
        generated_objects = self.object_test.get_all_objects()
        self.assertIsInstance(generated_objects, list)

        for object in generated_objects:
            self.assertIsInstance(object, Data)

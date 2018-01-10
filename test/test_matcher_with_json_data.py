import unittest
from objmatcher import match


class TestMatcherWithJsonData(unittest.TestCase):
    def test_two_json_with_high_similarity(self):
        data1 = {
            'Name': 'MSI COMPUTER CORP USA',
            # 'Address': '601 NORTH WALTON BLVD BENTONVILLE AR 72716 USA'
        }

        data2 = {
            'Name': 'MSI COMPUTER CORP',
            # 'Address': '601 N WALTON BLVD BENTONVILLE AR 72716 USA'
        }

        self.assertGreaterEqual(match(data1, data2), 0.9)

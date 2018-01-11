import unittest
from objmatcher import match


class TestMatcherWithJsonData(unittest.TestCase):
    def test_two_json_with_high_similarity(self):
        data1 = {
            'Name': [
                'SAMS CLUB WALMART STORES INC',
                'WALMART STORES INC WALMART STORE',
                'WALMART STORES S A'
            ],
            'Address': [
                '601 NORTH WALTON BLVD BENTONVILLE AR 72716 USA'
            ]
        }

        data2 = {
            'Name': [
                'WALMART STORES INC XXX'
            ],
            'Address': [
                '601 NORTH WALTON BLVD BENTONVILLE AR 72712 USA'
            ]
        }

        self.assertGreaterEqual(match(data1, data2), 0.9)

    # def test_json_with_list_of_data(self):
    #     data1 = {
    #         'Name': ['HEWLETT PACKARD ENTERPRISE COMPANY'],
    #         'Address': [
    #             '3000 HANOVER STREET PALO ALTO CA 94304 USA',
    #             '6701 LEGACY BLVD, OLIVE BRANCH, MS 38654, USA',
    #             '11445 COMPAQ CENTER DR HOUSTON TX 77070 USA',
    #             '4501 BLALOCK, HOUSTON, TX 77041, USA'
    #         ]
    #     }
    #
    #     data2 = {
    #         'Name': ['HPE'],
    #         'Address': ['11445 COMPAQ CENTER DR HOUSTON TX 77070 USA']
    #     }
    #
    #     print(match(data1, data2))
    #     assert False

import unittest
from objmatcher import match
from objmatcher import Data


class TestMatcherWithJsonData(unittest.TestCase):
    def test_case_sensitivity(self):
        data1 = {
           u'names':[
              u'POTATO BARN'
           ],
           u'clean address':[
              u'17131E WILLIAMS FIELD RD HIGLEY AZ 85236 USA',
              u'1713 EAST WILLIAMS FIELD HIGLEY AZ 85236 USA',
              u'3545 EAST WILLIAMS FIELD RD GILBERT AZ 85296 USA',
              u'4900 SOUTH POWER RD GILBERT AZ 85296 USA',
              u'4900 SOUTH SPOWER RD GILBERT AZ 85296 USA',
              u'596 EAST GERMANN RD GILBERT AZ 85297 USA',
              u'596 GERMANN EAST 102 GILBERT AZ 85297 USA',
              u'596 GERMANN EAST 102 GILBERT AZ 85233 USA',
              u'7000 EAST MAYO BLVD PHOENIX AZ 85001 USA',
              u'4900 SOUTH POWER RD GILBERT AZ 85295 USA',
              u'8980 EAST BAHIA DR SCOTTSDALE AZ 85261 USA',
              u'8980 EAST BAHIA DR SCOTTSDALE AZ 85260 USA',
              u'596E GERMANN RD GILBERT AZ 85297 USA',
              u'4900 SOUTH POWER RD MESA AZ 85212 USA',
              u'596 EAST GERMANN RD GILBERT AZ 85233 USA'
           ]
        }

        data2 = {
           u'names':[
              u'Potato Barn'
           ],
           u'clean address':[
              u'8980 East BAHIA DR, Scottsdale, AZ 85260, USA'
           ]
        }

        self.assertGreaterEqual(match(data1, data2), 0.9)

    def test_key_not_matching(self):
        data1 = Data()
        data1.add_meta_data('names', 'WALMART STORES INC WALMART STORE INC INC')
        data2 = Data()
        data2.add_meta_data('names', 'WALMART STORES INC')
        data2.add_meta_data('addresses', '601 NORTH WALTON BLVD BENTONVILLE AR 72716 USA')

        self.assertGreaterEqual(match(data1.to_json(), data2.to_json()), 0.9)

    def test_matching_from_data(self):
        data1 = Data()
        data1.add_meta_data('names', 'WALMART STORES INC WALMART STORE INC INC')
        data1.add_meta_data('names', 'WALMART STORES S A')
        data1.add_meta_data('names', 'SAMS CLUB WALMART STORES INC')
        data1.add_meta_data('names', 'WAL MART STORES INC USA')
        data1.add_meta_data('names', 'WAL MART STORES INC 601 N')
        data1.add_meta_data('addresses', '601 NORTH WALTON BLVD BENTONVILLE AR 72716 USA')
        data1.add_meta_data('addresses', 'WALTON BLVD, BENTONVILLE, AR 72716, USA')

        data2 = Data()
        data2.add_meta_data('names', 'WALMART STORES INC')
        data2.add_meta_data('addresses', '601 NORTH WALTON BLVD BENTONVILLE AR 72716 USA')

        self.assertGreaterEqual(match(data1.to_json(), data2.to_json()), 0.9)

    def test_high_similarity(self):
        data1 = {
            'Name': [
                'SAMS CLUB WALMART STORES INC',
                'WALMART STORES INC WALMART STORE INC INC',
                'WALMART STORES S A',
                'WAL MART STORES INC USA',
                'WAL MART STORES INC 601 N'
            ],
            'Address': [
                '601 NORTH WALTON BLVD BENTONVILLE AR 72716 USA',
                'WALTON BLVD, BENTONVILLE, AR 72716, USA'
            ]
        }

        data2 = {
            'Name': [
                'WALMART STORES INC'
            ],
            'Address': [
                '601 NORTH WALTON BLVD BENTONVILLE AR 72716 USA'
            ]
        }

        self.assertGreaterEqual(match(data1, data2), 0.9)

    def test_remove_special_char(self):
        data1 = {
            'Name': [
                'THE FISHIN COMPANY'
            ],
            'Address': [
                '3714 MAIN STREET, HOMESTEAD, PA 15120, USA',
                '3714 MAIN STREET, PITTSBURGH, PA 15201, USA'
            ]
        }

        data2 = {
            'Name': [
                'FISHIN COMPANY (THE)'
            ],
            'Address': [
                '3714 MAIN STREET HOMESTEAD PA 15120 USA'
            ]
        }

        self.assertEqual(match(data1, data2), 1.0)

    def test_no_similarity(self):
        data1 = {
            'Name': [
                'AQUACHILE INC'
            ],
            'Address': [
                '5200 BLUE LAGOON DRIVE, MIAMI, FL 33126, USA'
            ]
        }

        data2 = {
            'Name': [
                'SEAHORSE CONTAINER LINES'
            ],
            'Address': [
                '10731 WALKER STREET, CYPRESS, CA 90630, USA'
            ]
        }

        self.assertLess(match(data1, data2), 0.4)

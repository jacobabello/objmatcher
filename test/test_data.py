# import unittest
# from objmatcher import Data
#
#
# class TestData(unittest.TestCase):
#     def test_adding_meta_data(self):
#         data = Data()
#         data.add_meta_data("Name", "WALLMART STORES INC")
#         data.add_meta_data("Name", "WALMART STORES INC, WALMART STORE")
#         data.add_meta_data("Name", "WALMART STORES INC")
#         data.add_meta_data("Address", "601 NORTH WALTON BLVD, BENTONVILLE, AR 72716, USA")
#         data.add_meta_data("Address", "702 SOUTH 8 STREET, BENTONVILLE, AR 72716, USA")
#         data.add_meta_data("Address", "508 SOUTH WEST 8TH STREET, BENTONVILLE, AR 72712, USA")
#
#         real_json = {
#             'Name': [
#                 'WALLMART STORES INC',
#                 'WALMART STORES INC, WALMART STORE',
#                 'WALMART STORES INC'
#             ],
#             'Address': [
#                 '601 NORTH WALTON BLVD, BENTONVILLE, AR 72716, USA',
#                 '702 SOUTH 8 STREET, BENTONVILLE, AR 72716, USA',
#                 '508 SOUTH WEST 8TH STREET, BENTONVILLE, AR 72712, USA'
#             ]
#         }
#
#         self.assertEqual(data.to_json(), real_json)
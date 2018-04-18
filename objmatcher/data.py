import json
from collections import OrderedDict


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

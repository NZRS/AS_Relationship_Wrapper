__author__ = 'secastro'

import csv

class AsRelationshipService:
    as_rel = {}
    rel2class = {'-': 'p2p',
                 '>': 'p2c',
                 '<': 'c2p',
                 '=': 's2s',
                 '?': 'unk'}

    def __init__(self, file_list):
        for filename in file_list:
            with open(filename, 'r') as as_rel_file:
                as_rel_csv = csv.reader(filter(lambda row: row[0] != '#',
                                               as_rel_file), delimiter="|")
                for as_rel_entry in as_rel_csv:
                    [prov_as, cust_as, rel] = as_rel_entry
                    self.as_rel["{0}+{1}".format(prov_as, cust_as)] = int(rel)

    def find_rel(self, s, d):
        rv = '?'

        key = "{0}+{1}".format(s, d)
        key_rev = "{0}+{1}".format(d, s)
        if key in self.as_rel:
            if self.as_rel[key] == 0:
                rv = '-'
            elif self.as_rel[key] < 0:
                rv = '>'
            elif self.as_rel[key] == 1:
                rv = '<'
            else:
                rv = '='
        elif key_rev in self.as_rel:
            if self.as_rel[key_rev] == 0:
                rv = '-'
            elif self.as_rel[key_rev] < 0:
                rv = '<'
            elif self.as_rel[key_rev] == 1:
                rv = '>'
            else:
                rv = '='

        return rv

    def rel_char2class(self, rel):
        return self.rel2class.get(rel, 'unk')

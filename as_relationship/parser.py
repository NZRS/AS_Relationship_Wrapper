#!/usr/bin/env python

#    This file is part of 'AS Relationship Handler'
#
#    'IP Topology Map' is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    'AS Relationship Handler' is distributed in the hope that it will be
#    useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public
#    License along with 'AS Relationship Handler'.  If not, see
#    <http://www.gnu.org/licenses/>.

import re


class AsRelationship:
    as_rel = {}
    tier1 = []
    _rel2class = {'-': 'p2p',
                  '>': 'p2c',
                  '<': 'c2p',
                  '=': 's2s',
                  '?': 'unk'}

    def __init__(self, rel_file=None):
        with open(rel_file, 'r') as as_rel_file:
            for line in as_rel_file.readlines():
                if re.search('^# (input|inferred) clique:', line):
                    self.tier1 = [n for n in line.rstrip("\n").split(':')[-1].split(' ') if n != '']
                elif re.search('^#', line):
                    continue
                else:
                    [prov_as, cust_as, rel] = line.rstrip("\n").split('|')
                    self.as_rel["%s+%s" % (prov_as, cust_as)] = int(rel)

    def rel_char(self, src, dst):
        rv = '?'
        key = "{0}+{1}".format(src, dst)
        key_rev = "{0}+{1}".format(dst, src)
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

    def rel2class(self, src, dst):
        return self._rel2class[self.rel_char(src, dst)]

    def peering(self):
        return self._rel2class['-']

    def tier1_asn(self):
        return self.tier1

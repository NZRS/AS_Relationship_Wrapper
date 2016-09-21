__author__ = 'secastro'


import as_relationship.parser
import as_relationship.fetcher

s = as_relationship.parser.AsRelationship(rel_file='test-data.txt')
print s.rel_char(42, 5413)
print s.rel_char(5413, 42)
print s.rel_char(42, 715)
print s.rel_char(715, 42)
print s.rel_char(4771, 4648)

print "Test file Clique"
print s.tier1_asn()

new_file = as_relationship.fetcher.get_as_relationship_file(datadir='data')
s2 = as_relationship.parser.AsRelationship(rel_file=new_file)
print "New File Clique"
print s2.tier1_asn()


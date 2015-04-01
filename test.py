__author__ = 'secastro'


from as_relationship import AsRelationshipService

s = AsRelationshipService(['test-data.txt'])
print s.find_rel(42, 5413)
print s.find_rel(5413, 42)
print s.find_rel(42, 715)
print s.find_rel(715, 42)
print s.find_rel(4771, 4648)

print s.rel_char2class(s.find_rel(35, 5691))
print s.rel_char2class(s.find_rel(5691, 35))
print s.rel_char2class(s.find_rel(4771, 4648))

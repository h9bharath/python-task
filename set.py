# s={1,2,3,4,2,3,6}
# print(s)
# s.add(67)
# print(s)
# s.remove(67)
# print(s)
# s.pop()
# s.pop()
# print(s)
# s.update([10,20,30])
# print(s)
# #discard()
# s.discard(8)
# print(s)

# '''set operations'''
# #union()
# s1={33,44,55,66,1,3,5,6,8,10}
# print(s.union(s1))
# #inresection of sets
# print(s.intersection(s1))
# #difference of set
# print(s.difference(s1))  #s-s1
# print(s1.difference(s))  #s1-s
# #symmetric difference of set
# print(s.symmetric_difference(s1))
a={1,2,3,4}
b={3,4,5,6}
print(a.symmetric_difference(b))  # a-b
print(a.difference(b))
print(b.difference(a))
#print(a)
#print(b)
c=frozenset({1,2,3})
c.add(4)
print(c)

"""
Solution to extendList problem
This issue comes from the way the values are
assigned in memory.

Original:
def extendList(val, list=[]):
    list.append(val)
    return list

"""

def extendList(val):
    list = []
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123)
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3

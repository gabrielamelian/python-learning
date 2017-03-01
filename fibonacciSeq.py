
"""
Solution to Fibonacci problem for a single number.
Takes a long time to run.
"""

# def F(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return F(n-1)+F(n-2)
#
# print F(34)

"""
Solution to Fibonacci sequence.
Made to run up to 100 times
"""

def Fseq():
    i = 0
    a, b = 0, 1
    print a
    print b
    while i < 100:
        i += 1
        a, b = b, a + b
        print b

Fseq()

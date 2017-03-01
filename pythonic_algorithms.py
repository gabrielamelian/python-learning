"""Code snippets from CodeAcademy Pythonic Algorithms course."""

# i = 100
#
# while True:
#     i -= 1
#     if i == 0:
#         break
#
# print i

"""
First, run this code, noticing its slow running speed.
Then, change the loop so that it utilizes an infinite
loop to accomplish the same task.


j = 0
for i in range(1, 1000001):
    j += 1
    print j

"""

j = 0
while True:
    j += 1
    if j == 1000000:
        break
print j

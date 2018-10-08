import bisect
import random

SIZE = 7
random.seed(1729)

my_lst = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_lst, new_item)
    print('%2d ->' % new_item, my_lst)
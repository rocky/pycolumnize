#!/usr/bin/env python

from random import randint

from columnize import columnize

lst = []
for i in range(200):
    num_digits = randint(1, 6)
    lst.append(randint(0, 10 ** num_digits))

output = columnize(lst, opts={'ljust': True})
print(output)

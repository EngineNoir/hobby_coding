import itertools
from itertools import permutations
import random as rd
import math

string_list = ["1001010", "001010010", "10010", "1111001"]
print(string_list)

smallest_string_length = min([len(element) for element in string_list])
print(smallest_string_length)

partitioned_strings = []

partition_length = rd.randint(2, math.floor(smallest_string_length/2) + 1)

for string in string_list:
    x = [string[i: i+partition_length] for i in range(0, len(string), partition_length)]
    partitioned_strings.append(x)

print(partitioned_strings)

trial_list = list(itertools.product(*partitioned_strings))


print(rd.sample(trial_list, 4))

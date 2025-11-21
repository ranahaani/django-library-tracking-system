import random

rand_list = random.sample(range(100), 10)

list_comprehension_below_10 = [num for num in rand_list if num < 10]

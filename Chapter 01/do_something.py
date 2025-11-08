import random

def do_something(size, out_list):
   
    for _ in range(size):
        num = random.randint(1, 100)
        out_list.append(num * num)
    return out_list

import random

def do_something(size, out_list):
    """
    Random numbers ke square nikalta hai aur list me daalta hai.
    Ye function sirf ek example hai — tum yahan koi bhi calculation karwa sakte ho.
    """
    for _ in range(size):
        num = random.randint(1, 100)
        out_list.append(num * num)
    return out_list

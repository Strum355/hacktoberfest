import random

def efficientSort(arr):
    while not(arr == sorted(arr)):
        random.shuffle(arr)
    return arr

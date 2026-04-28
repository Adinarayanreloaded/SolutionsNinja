# solution.py

def find_GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

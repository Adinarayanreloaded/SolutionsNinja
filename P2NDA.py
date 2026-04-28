from os import *
from sys import *
from collections import *
from math import *

def p_p(n,matrix):
    for i in range(n):
        for _ in range(n-i):
            print (' '.join(map(str,matrix[i])))

if __name__ == "__main__":
    import sys 
    input= sys.stdin.read
    data=input().strip().split('\n')
    n,m= map(int,data[0].split())
    matrix= [list(map(int,line.split())) for line in data[1:]]
    p_p(n,matrix)  
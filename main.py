import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    set1 = set(s.lower())
    print(set1)
    if ' ' in set1:
        set1.remove(' ')
    if len(set1) == 26:
        res = 'pangram'
    else: 
        res = 'not pangram'
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

#!/usr/bin/python

"""
Coded by lorddarthvader
Version 1.1
"""

import re, random

class Translator:
    def oe(self, no):
        if no%2==0:
            return True

    def filter(self, string):
        return re.sub('[^0-9a-zA-Z]+',' ',string)
    
    def __init__(self, usrin):
        usrin = self.filter(usrin).lower()
        s_arr = usrin.split(' ')
        n_arr = []
        yoda_s=''
        r=0
        convert=False
        if len(s_arr) < 4:
            yoda_s=usrin
        else:
            convert=True
            l = len(s_arr)
            if l >= 4 and l <= 10:
                r=2
            elif l > 10 and not self.oe(l):
                r=random.randint(3, 4)
            else:
                for no in range(1, 11):
                    if l%no==0:
                        r=int(no/2)
        if convert:
            n_arr.append(s_arr[r:])
            n_arr.append(s_arr[:r])
            for a in n_arr[0]:yoda_s += ' ' + a
            yoda_s += ','.strip()
            for b in n_arr[1]:yoda_s += ' ' + b

        print "[Yoda] : %s." % (yoda_s)

while True:
    Translator(raw_input("=> "))
        

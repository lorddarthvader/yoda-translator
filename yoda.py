#!/usr/bin/python

"""
Coded by lorddarthvader
Version 1.0
"""

class Translator:
    def __init__(self, usrin):
        usrin = usrin.lower()
        s_arr = usrin.split(' ')
        n_arr = []
        yoda_s=''
        convert=False
        if len(s_arr) < 4:
            yoda_s=usrin
        else:
            convert=True
            l = len(s_arr)
            for no in range(1, 11):
                if l%no==0:
                    r=int(round(no/2))
        if convert:
            n_arr.append(s_arr[r:])
            n_arr.append(s_arr[:r])
            for a in n_arr[0]:yoda_s += ' ' + a
            yoda_s += ','
            for b in n_arr[1]:yoda_s += ' ' + b

        print "[Yoda] : %s." % (yoda_s)

while True:
    try:
        Translator(raw_input("=> "))
    except:
        break

#!/bin/python3

w,h = [ int (x) for x in input().split() ]
f1_w, f1_h = [ int (x) for x in input().split() ]
f2_w, f2_h = [ int (x) for x in input().split() ]


if ((f1_h+f2_w <= h) and (f2_h <= w) and (f1_w <= w)) or ((f1_h+f2_w <= w) and (f2_h <= h) and (f1_w <= h)):
    print("S")
elif ((f1_w <= w) and (f2_w <= w) and (f1_h + f2_h <= h)) or ((f1_w <= h) and (f2_w <= h) and (f1_h + f2_h <= w)):
    print("S")
elif ((f1_h <= w) and (f2_w <= w) and (f1_w + f2_h <= h)) or ((f1_h <= h) and (f2_w <= h) and (f1_w + f2_h <= w)):
    print("S")
elif ((f1_h <= w) and (f2_h <= w) and (f1_w + f2_w <= h)) or ((f1_h <= h) and (f2_h <= h) and (f1_w + f2_w <= w)):
    print("S")
else:
    print("N")

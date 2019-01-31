#! /usr/local/bin/python3
#  -*- coding: utf-8 -*-


import math


jahr = int(input("Jahr: "))

if math.fmod(jahr,400)==0:
    print(jahr, "ist ein Schaltjahr")
elif math.fmod(jahr,100)==0:
    print(jahr, "ist kein Schaltjahr")
elif math.fmod(jahr,4)==0:
    print(jahr, "ist ein Schaltjahr")
else:
    print(jahr, "ist kein Schaltjahr")

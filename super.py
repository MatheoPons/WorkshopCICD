#!/usr/bin/env python3

#
# EPITECH PROJECT, 2019
# my convert base
# File description:
# convertisseur d'une base n à une base m
#

import math
import sys

def print_h():
    print("USAGE")
    print("    ./101pong x0 y0 z0 x1 y1 z1 n")
    print("")
    print("DESCRIPTION")
    print("    x0  ball abscissa at time t - 1")
    print("    y0  ball ordinate at time t - 1")
    print("    z0  ball altitude at time t - 1")
    print("    x1  ball abscissa at time")
    print("    y1  ball ordinate at time")
    print("    z1  ball altitude at time")
    print("    n  time shift (greater than or equal to zero, integer)")

def cal_velocity (argv1, argv2, argv3, x0, y0, z0, argv7,
 argv4, argv5, argv6, angle):
    xv = float(x0 - argv1)
    yv = float(y0 - argv2)
    zv = float(z0 - argv3)
    print("The velocity vector of the ball is:")
    print("({0:0.2f}, {1:0.2f}, {2:0.2f})".format(xv, yv, zv))
    for loop in range(argv7):
        x0 = x0 + xv
        y0 = y0 + yv
        z0 = z0 + zv
        loop = loop
    print("At time t + {0}, ball coordinates will be:".format(argv7))
    print("({0:0.2f}, {1:0.2f}, {2:0.2f})".format(x0, y0, z0))
    if (z0 == 0 and argv3 == 0):
        print("The incidence angle is:\n0.00 degrees")
    elif (z0 < 0 and argv6 > 0) or (z0 > 0 and argv6 < 0):
        print("The incidence angle is:")
        try:
            angle = (((180/math.pi)*(math.acos(zv/(math.sqrt((xv ** 2) + (yv ** 2) + (zv ** 2)))))) - 90)
        except ZeroDivisionError:
            exit (84)
        if angle < 0:
            angle = angle * -1
        else:
            angle = angle * 1
        print("{0:0.2f} degrees".format(angle))
    else:
        print("The ball won't reach the paddle.")

def launch (argc, argv):
    if (argc == 2):
        try:
            str1 = str(sys.argv[1])
            if str1 == "-h":
                print_h()
            else:
                exit (84)
        except ValueError:
            exit (84)
    elif (argc != 8):
        exit (84)
    else:
        try:
            argv1 = float(sys.argv[1])
       	    argv2 = float(sys.argv[2])
            argv3 = float(sys.argv[3])
            argv4 = float(sys.argv[4])
            argv5 = float(sys.argv[5])
            argv6 = float(sys.argv[6])
            x0 = float(sys.argv[4])
            y0 = float(sys.argv[5])
            z0 = float(sys.argv[6])
            argv7 = int(sys.argv[7])
            angle = float(0)
        except ValueError:
            exit (84)
        if argv7 < 0:
            exit (84)
        else:
            cal_velocity(argv1, argv2, argv3, x0, y0, z0, argv7,
             argv4, argv5, argv6, angle)

launch (len (sys.argv), sys.argv)

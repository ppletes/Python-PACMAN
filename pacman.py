#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from spade.agent import Agent
from spade import quit_spade
from random import randint
import argparse
from ast import literal_eval
from time import sleep
import functools
import inspect
import traceback
import time
import turtle
from math import *
from tkinter import *
from tkinter import ttk
from random import choice
from turtle import *
from freegames import floor, vector
from datetime import datetime


stanje = {'rezultat': 0}
put = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0)
pacman = [[vector(-40, -80), vector(0, 5)]]
pacman2 = vector(-40, -80)
duh = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
polje = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
    
    
def square(x, y):
    #crtanje kvadrata puta uz (x, y)
    put.up()
    put.goto(x, y)
    put.down()
    put.begin_fill()
    for count in range(4):
        put.forward(20)
        put.left(90)
    put.end_fill()

def offset(point):
    #vrati offset tocke u polju
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

def valid(point):
    #vrati True ako je validirana tocka u polju
    index = offset(point)
    if polje[index] == 0:
        return False
    index = offset(point + 19)
    if polje[index] == 0:
        return False
    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    #stvaranje labirinta
    Screen().title("VAS - PACMAN")
    bgcolor('black')
    put.color('blue')
    for index in range(len(polje)):
        tile = polje[index]
        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)
            if tile == 1:
                put.up()
                put.goto(x + 10, y + 10)
                put.dot(2, 'yellow')
    
def move():
    #kretnja pacmana i duhova - samostalno
    writer.undo()
    writer.write(stanje['rezultat'])

    clear()

    for ve in pacman:
        index = offset(ve[0])

    if polje[index] == 1:
        polje[index] = 2
        stanje['rezultat'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)
    elif polje==0:
        print("POBJEDA, ovo je kraj igre!")

    for point, course in pacman:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y
        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'yellow')
        
    for point, course in duh:
        for point2, course2 in pacman:
            opposite=point.y-point2.y
            adjacent=point.x-point2.x
            try:
                angle = atan(adjacent/opposite)
                if point2.x < point.x:
                    backward(100)
            except ZeroDivisionError:
                angle = 0
                
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y
        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'white')

    update()
    
    
    for point, course in duh:
        if abs(ve[0] - point) < 20:
            print("UDAR, izgubio sam.")
            f = open("Rezultat.txt", "a+")
            f.write("\ns: " + str(stanje['rezultat']))
            bye()
            return
            
    ontimer(move, 100)

def move2():
    #kretnja pacmana i duhova - tipke
    writer.undo()
    writer.write(stanje['rezultat'])

    clear()

    if valid(pacman2 + aim):
        pacman2.move(aim)

    index = offset(pacman2)

    if polje[index] == 1:
        polje[index] = 2
        stanje['rezultat'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)
    elif polje==0:
        print("POBJEDA, ovo je kraj igre!")

    up()
    goto(pacman2.x + 10, pacman2.y + 10)
    dot(20, 'red')

    for point, course in duh:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'white')

    update()

    for point, course in duh:
        if abs(pacman2 - point) < 20:
            print("UDAR, izgubio sam.")
            f = open("Rezultat.txt", "a+")
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write("\n" + dt_string)
            f.write("\nt: " + str(stanje['rezultat']))
            bye()
            return

    ontimer(move2, 100)

def change(x, y):
    #mjenjanje pacman-a s obzirom na tipke
    if valid(pacman2 + vector(x, y)):
        aim.x = x
        aim.y = y
                            
class Igra(Agent):
    def __init__(self, *args, vrsta, **kwargs):
        super().__init__(*args, **kwargs)
        self.vrsta = vrsta
        self.say("Krećem sa igrom!")
        if self.vrsta in ["tipka", "t"]:
            move2()
        else:
            move()   
              
    def say(self, msg):
            print(f"{self.name}: {msg}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Primjer pokretanja: #python3 pacman.py -v t -jid agent@rec.foi.hr -pwd tajna")
    parser.add_argument("-v", "--vrsta", type=str, help="Vrsta agenta (s - samostalno ili t - tipkovnica)")
    parser.add_argument("-jid", type=str, help="JID agenta")
    parser.add_argument("-pwd", type=str, help="Lozinka agenta", default="tajna")
    args = parser.parse_args()

    agent = Igra(args.jid, args.pwd, vrsta=args.vrsta)
    agent.start()

    setup(800, 500, 300, 100)
    hideturtle()
    tracer(False)
    writer.goto(160, 160)
    writer.color('white')
    writer.write(stanje['rezultat'])
    listen()
    onkey(lambda: change(5, 0), 'Right')
    onkey(lambda: change(-5, 0), 'Left')
    onkey(lambda: change(0, 5), 'Up')
    onkey(lambda: change(0, -5), 'Down')
    world()
                    
    input("Press ENTER to exit.\n")
    agent.stop()
    quit_spade()

from playsound import playsound
import turtle as t
from time import time, sleep
from random import uniform
from fireworks import Firework, g
from math import *

screen = t.Screen()
brush = t.Turtle()

START = 0
before = 0

def wait():
    global timeStamp, before
    after = timeStamp.pop()
    sleep(after - before)
    before = after
    
def init():
    global screen, brush, START, before
    screen.setup(1024, 600, 150, 75)
    
    screen.setworldcoordinates(0, 0, 1024, 600)
    screen.bgcolor("#000000")

    brush.ht()
    brush.speed(0)
    brush.pu()
    brush.color("#FFD700", "#FFD700")
    screen.title("Happy New Year")
    playsound("JoyToTheWorld.mp3", False)
    START = time()
    before = START

    screen.tracer(0, 0)
    scene1()

def scene1():
    global screen, brush, timeStamp, before

    before = timeStamp.pop()
    sleep(before)
    happy = ("Snowballs", 150, "normal")
    newYear = ("Snowballs", 200, "normal")
    brush.goto(256, 300)
    brush.write("Happy", align = "center", font = happy)
    wait()
    wait()
    brush.goto(256, 0)
    brush.write("New", align = "center", font = newYear)
    wait()
    wait()
    brush.goto(768, 0)
    brush.write("Year", align = "center", font = newYear)
    wait()
    wait()
    brush.color("#B29700", "#B29700")
    brush.goto(261, 295)
    brush.write("Happy", align = "center", font = happy)
    brush.goto(261, -5)
    brush.write("New", align = "center", font = newYear)
    brush.goto(773, -5)
    brush.write("Year", align = "center", font = newYear)
    wait()
    scene3()

def drawFunction(org, fin, iteration, f, fInterval, force = 1):
    start = min(org[0], fin[0])
    end = max(org[0], fin[0])
    if start == org[0]:
        startY = org[1]
        endY = fin[1]
    else:
        startY = fin[1]
        endY = org[1]
    interLen = end - start
    
    ratio = abs(endY - startY)
    endF = max(fInterval[0], fInterval[1])
    startF = min(fInterval[0], fInterval[1])
    finterLen = endF - startF
    
    T = [startF + (finterLen / iteration) * t for t in range(iteration + 1)]
    X = [start + (interLen / finterLen) * (t - startF) for t in T]
    if f(endF) != 0:
        Y = [startY + force * (ratio / f(endF)) * (f(t) - f(T[0])) for t in T]
    else:
        Y = [startY + force * (ratio) * (f(t) - f(T[0])) for t in T]
    return X, Y

def iterationXY(X, Y, Iteration):
    brush.pu()
    brush.goto(X[0], Y[0])
    brush.pd()
    for idx in range(Iteration + 1):
        brush.goto(X[idx], Y[idx])
    screen.update()

def decoration(locX, locY):
    global brush
    brush.pu()
    brush.goto(locX, locY)
    brush.pensize(2)
    brush.pd()
    brush.begin_fill()
    brush.circle(10)
    brush.end_fill()

def star(length, fill = True):
    global brush
    brush.pd()
    if fill:
        brush.begin_fill()
    for i in range(5):
        brush.lt(144)
        brush.fd(length)
        brush.rt(72)
        brush.fd(length)
    brush.end_fill()

def scene3():
    global brush, screen
    brush.clear()
    brush.setheading(180)
    brush.ht()
    brush.speed(0)
    brush.pensize(30)
    brush.pu()
    brush.color("#FFFFFF", "#FFFFFF")
    brush.goto(204.8, 600)
    brush.pd()
    brush.goto(204.8, 250)
    brush.color("#DF0000", "#FF0000")
    brush.begin_fill()
    brush.pensize(10)
    brush.circle(80)
    brush.end_fill()
    screen.update()
    wait()  
    brush.pu()
    brush.pensize(15)
    brush.color("#FFFFFF", "#FFFFFF")
    brush.goto(409.6, 600)
    brush.pd()
    brush.goto(409.6, 480)
    brush.color("#00DF00", "#00FF00")
    brush.begin_fill()
    brush.pensize(5)
    brush.circle(40)
    brush.end_fill()
    screen.update()
    wait() 
    brush.pu()
    brush.pensize(45)
    brush.color("#FFFFFF", "#FFFFFF")
    brush.goto(614.4, 600)
    brush.pd()
    brush.goto(614.4, 150)
    brush.color("#B29700", "#FFD700")
    brush.begin_fill()
    brush.pensize(15)
    brush.circle(120)
    brush.end_fill()
    screen.update()
    wait()
    brush.pu()
    brush.pensize(20)
    brush.color("#FFFFFF", "#FFFFFF")
    brush.goto(819.2, 600)
    brush.pd()
    brush.goto(819.2, 350)
    brush.color("#0000DF", "#0000FF")
    brush.begin_fill()
    brush.pensize(7)
    brush.circle(50)
    brush.end_fill()
    screen.update()
    wait()
    scene4()

def scene4():
    global brush, screen
    brush.clear()
    brush.setheading(0)
    brush.ht()
    brush.speed(0)
    brush.pensize(1)
    brush.pu()
    brush.goto(512, 150)
    brush.color("#FFD700", "#FFD700")
    brush.write("2", align="center", font=("Snowballs",200,"normal"))
    wait()
    brush.clear()
    brush.write("20", align="center", font=("Snowballs",200,"normal"))
    wait()
    brush.clear()
    brush.write("202", align="center", font=("Snowballs",200,"normal"))
    wait()
    brush.clear()
    brush.write("2022", align="center", font=("Snowballs",200,"normal"))
    wait()
    brush.clear()
    brush.write("2022☆", align="center", font=("Snowballs",200,"normal"))
    wait()
    brush.clear()
    brush.write("2022★", align="center", font=("Snowballs",200,"normal"))
    wait()
    screen.setup(1024, 600, 25, 25)
    wait()
    screen.setup(1024, 600, 150, 125)
    wait()
    screen.setup(1024, 600, 275, 225)
    wait()
    screen.setup(1024, 600, 150, 75)
    wait()
    scene5()

def gradation(initial, final, count):
    cSet = []
    rRange = final[0] - initial[0]
    gRange = final[1] - initial[1]
    bRange = final[2] - initial[2]
    for c in range(count):
        cSet.append([initial[0] + ((rRange * c) // count),
                     initial[1] + ((gRange * c) // count),
                     initial[2] + ((bRange * c) // count)])
    return cSet

def scene5():
    global brush, screen, point
    brush.clear()
    screen.update()
    initial = [185, 14, 10]
    final = [248, 222, 126]
    sun = gradation(initial, final, 300)
    initial = [221, 87, 28]
    final = [99, 197, 218]
    sky = gradation(initial, final, 300)
    t.colormode(255)
    brush.pu()
    for idx in range(300):
        brush.color(sky[idx])
        brush.goto(-20, 2 * idx)
        brush.begin_fill()
        brush.goto(-20, 2 * (idx + 1))
        brush.goto(1044, 2 * (idx + 1))
        brush.goto(1044, 2 * idx)
        brush.goto(-20, 2 * idx)
        brush.end_fill()
        if idx % 50 == 49:
            screen.update()
            wait()
    brush.color(sky[-1])
    brush.goto(-20, 600)
    brush.begin_fill()
    brush.goto(-20, 700)
    brush.goto(1044, 700)
    brush.goto(1044, 600)
    brush.goto(-20, 600)
    brush.end_fill()
    screen.update()

    wait()
    wait()
    wait()
    wait()

    R = 250

    X = [-R + (R / 300) * t for t in range(301)]
    Y = [pow(R**2 - pow(x, 2), 0.5) for x in X]
    for idx in range(len(X)):
        X[idx] += 512
    for idx in range(len(Y)):
        Y[idx] -= 240

    for idx in range(300):
        brush.color(sun[idx])
        brush.goto(X[idx], Y[idx])
        brush.begin_fill()
        brush.goto(X[idx], Y[idx + 1])
        brush.goto(1024 - X[idx], Y[idx + 1])
        brush.goto(1024 - X[idx], Y[idx])
        brush.goto(X[idx], Y[idx])
        brush.end_fill()
        if idx % 100 == 99:
            screen.update()
            wait()

    for k in range(4):
        for idx in range(len(Y)):
            Y[idx] += 60

        for idx in range(300):
            brush.color(sun[idx])
            brush.goto(X[idx], Y[idx])
            brush.begin_fill()
            brush.goto(X[idx], Y[idx + 1])
            brush.goto(1024 - X[idx], Y[idx + 1])
            brush.goto(1024 - X[idx], Y[idx])
            brush.goto(X[idx], Y[idx])
            brush.end_fill()
            if idx % 75 == 74:
                screen.update()
                wait()

    brush.color("#FFFFFF", "#FFFFFF")
    brush.goto(204.8, 350)
    brush.write("2", align = "center", font = ("Snowballs", 150, "normal"))
    wait()
    brush.goto(409.6, 250)
    brush.write("0", align = "center", font = ("Snowballs", 150, "normal"))
    wait()
    brush.goto(614.4, 410)
    brush.write("2", align = "center", font = ("Snowballs", 150, "normal"))
    wait()
    brush.goto(819.2, 320)
    brush.write("2", align = "center", font = ("Snowballs", 150, "normal"))
    wait()
    brush.color("#000000", "#000000")
    brush.goto(409.6, 250)
    brush.write("0", align = "center", font = ("Snowballs", 150, "normal"))
    wait()
    brush.goto(819.2, 320)
    brush.write("2", align = "center", font = ("Snowballs", 150, "normal"))
    wait()
    brush.goto(204.8, 350)
    brush.write("2", align = "center", font = ("Snowballs", 150, "normal"))
    wait()
    brush.goto(614.4, 410)
    brush.write("2", align = "center", font = ("Snowballs", 150, "normal"))
    wait()
    brush.color("#FFFFFF", "#FFFFFF")
    brush.goto(409.6, 250)
    brush.write("0", align = "center", font = ("Snowballs", 150, "normal"))
    wait()
    brush.goto(819.2, 320)
    brush.write("2", align = "center", font = ("Snowballs", 150, "normal"))
    wait()
    screen.setup(1024, 600, 500, 75)
    wait()
    screen.setup(1024, 600, 300, 150)
    wait()
    screen.setup(1024, 600, 100, 225)
    wait()
    screen.setup(1024, 600, 300, 25)
    wait()
    screen.setup(1024, 600, 300, 100)
    wait()
    screen.setup(1024, 600, 300, 175)
    wait()
    screen.setup(1024, 600, 300, 250)
    wait()
    screen.setup(1024, 600, 150, 75)
    wait()
    screen.setworldcoordinates(1024, 600, 0, 0)
    wait()
    screen.setworldcoordinates(0, 0, 1024, 600)
    wait()
    scene6Preparing()

def scene6Preparing():
    brush.clear()
    for i in range(12):
        Firework([uniform(0, 1024), 0], 20, uniform(pi/6,5*pi/6), 1, (uniform(0.3,1), uniform(0.3,1), uniform(0.3,1)), 4)
    screen.ontimer(scene6, 1000//60)
    screen.mainloop()

def scene6():
    global brush, screen
    t.colormode(1.0)
    Firework.processing()
    for f in Firework.fireworks:
        brush.color(f.c)
        brush.goto(f.p)
        brush.dot()
    if len(Firework.fireworks) == 0:
        finale()
    else:
        screen.update()
        screen.ontimer(scene6, 1000//60)

def finale():
    global brush, screen
    brush.goto(512, 160)
    brush.pu()
    brush.color("#FFD700", "#FFD700")
    brush.write("Zakariyan Coding Society!", align = "center", font = ("Snowballs", 95, "normal"))
    brush.color("#B29700", "#B29700")
    brush.goto(515, 157)
    brush.write("Zakariyan Coding Society!", align = "center", font = ("Snowballs", 95, "normal"))
    screen.update()
    screen.onclick(end)

def end(x, y):
    global brush, screen
    brush.clear()
    screen.bye()
    print("Thanks For Watching!")
    print('Credit goes to "Bucket1572"')
    sleep(3)
    quit()
    
if __name__=="__main__":
    timeStamp = []
    with open("Timings.txt") as f:
        f = f.readlines()
        for i in range(len(f)):
            f[i] = float(f[i])
    timeStamp = f[::-1]
    init()

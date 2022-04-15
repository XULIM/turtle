from functools import lru_cache
import turtle
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
def plot(): 
    for i in range(4):
        t.forward(a * f[0])
        t.left(v)
    t.right(v)
    s.penup()
    s.goto(a * f[0], 0)
    s.pendown()
    s.left(v)
    s.circle(a * f[0], v)
    for i in range(1, len(f)):
        t.back(f[i - 1] * a)
        t.right(v)
        for x in range(3):
            t.forward(f[i] * a)
            t.left(v)
        t.right(v)
        s.circle(a * f[i], v)
ifend = False
while not ifend: 
    try: 
        print("Recommended to enter value between 4 to 10")
        f = [fib(n) for n in range(1, int(input("Steps: ")) + 1)]
        turtle.bgcolor("#000000")
        scr = turtle.Screen()
        #scr.screensize(1920, 1080)
        scr.setup(width=0.8, height=0.8)
        t = turtle.Turtle()
        t.pencolor("#FFFF00")
        t.hideturtle()
        t.speed(8)
        s = turtle.Turtle()
        s.pencolor("#00FFFF")
        a = 16 if len(f) <= 8 else 8
        v = 90
        plot()
        s.hideturtle()
        ifend = True
    except IndexError:
        print("Input Value Out Of Range: ]1, inf[")
        s.hideturtle()
    except ValueError:
        print("Invalid Value Type: Integer Only")
    except TypeError:
        print("Invalid Input Type: Integer Only")
input()
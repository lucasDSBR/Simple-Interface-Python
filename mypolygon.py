import turtle
import math
bob = turtle.Turtle()

def polygon(t, n, length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# polygon(bob, n=7, length=70)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)
    
def polyline(t, n, length, angle):
    """Desenha n segmentos de reta com o comprimento dado e 
    ângulo (em graus) entre eles. t é um turtle"""
    for i in range(n):
        t.fd(length)
        t.lt(angle)
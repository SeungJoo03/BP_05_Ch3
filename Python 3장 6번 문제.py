Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Turtle()
>>> t.shape("turtle")
>>> 
>>> x1 = int(input("x1 : "))
x1 : 0\
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x1 = int(input("x1 : "))
ValueError: invalid literal for int() with base 10: '0\\'
>>> x1 = int(input("x1 : "))
x1 : 0
>>> y1 = int(input("y1 : "))
y1 : 0
>>> x2 = int(input("x2 : "))
x2 : 100
>>> y2 = int(input("y2 : "))
y2 : 100
>>> 
>>> dis = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
>>> 
>>> t.up()
>>> t.goto(x1, y1)
>>> t.down()
>>> t.goto(x2,y2)
>>> 
>>> t.write("점의 길이 ="+ str(dis))

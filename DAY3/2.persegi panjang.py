import turtle

t = turtle.Turtle()
t.speed(3)

def persegi_panjang(p, l, warna):
    t.color(warna)
    t.begin_fill()
    for i in range(2):
        t.forward(p)
        t.right(90)
        t.forward(l)
        t.right(90)
    t.end_fill()

def segitiga(s, warna):
    t.color(warna)
    t.begin_fill()
    for i in range(3):
        t.forward(s)
        t.left(120)
    t.end_fill()

def trapesium(a, b, tinggi, warna):
    t.color(warna)
    t.begin_fill()
    t.forward(a)
    t.left(60)
    t.forward(tinggi)
    t.left(120)
    t.forward(b)
    t.left(60)
    t.forward(tinggi)
    t.left(120)
    t.end_fill()

def jajar_genjang(p, l, warna):
    t.color(warna)
    t.begin_fill()
    for i in range(2):
        t.forward(p)
        t.left(60)
        t.forward(l)
        t.left(120)
    t.end_fill()

def segilima(s, warna):
    t.color(warna)
    t.begin_fill()
    for i in range(5):
        t.forward(s)
        t.left(72)
    t.end_fill()

persegi_panjang(100, 60, "red")
t.penup(); t.goto(150, 0); t.pendown()
segitiga(100, "yellow")
t.penup(); t.goto(-150, -150); t.pendown()
trapesium(120, 60, 60, "green")
t.penup(); t.goto(150, -150); t.pendown()
jajar_genjang(100, 60, "blue")
t.penup(); t.goto(0, 150); t.pendown()
segilima(80, "purple")

turtle.done()
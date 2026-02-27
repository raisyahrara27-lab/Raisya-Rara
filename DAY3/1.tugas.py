import turtle

t = turtle.Turtle()
t.speed(3)

# Persegi Panjang
def persegi_panjang(p, l):
    for i in range(2):
        t.forward(p)
        t.right(90)
        t.forward(l)
        t.right(90)

# Segitiga
def segitiga(s):
    for i in range(3):
        t.forward(s)
        t.left(120)

# Trapesium
def trapesium(a, b, tinggi):
    t.forward(a)
    t.left(60)
    t.forward(tinggi)
    t.left(120)
    t.forward(b)
    t.left(60)
    t.forward(tinggi)
    t.left(120)

# Jajar Genjang
def jajar_genjang(p, l):
    for i in range(2):
        t.forward(p)
        t.left(60)
        t.forward(l)
        t.left(120)

# Belah Ketupat
def belah_ketupat(s):
    for i in range(2):
        t.forward(s)
        t.left(60)
        t.forward(s)
        t.left(120)

# Gambar
persegi_panjang(100, 60)
t.penup()
t.goto(150, 0)
t.pendown()
segitiga(100)
t.penup()
t.goto(-150, -150)
t.pendown()
trapesium(120, 60, 60)
t.penup()
t.goto(150, -150)
t.pendown()
jajar_genjang(100, 60)
t.penup()
t.goto(0, 150)
t.pendown()
belah_ketupat(80)

turtle.done()
import turtle

t = turtle.Turtle()
t.speed(3)

# Ukuran bendera
panjang = 300
tinggi = 200

# ==============================
# BAGIAN MERAH (atas)
# ==============================
t.penup()
t.goto(-panjang/2, tinggi/2)
t.setheading(0)
t.pendown()

t.color("black", "red")  # garis hitam, isi merah
t.begin_fill()
for i in range(2):
    t.forward(panjang)
    t.right(90)
    t.forward(tinggi/2)
    t.right(90)
t.end_fill()

# ==============================
# BAGIAN PUTIH (bawah)
# ==============================
t.penup()
t.goto(-panjang/2, 0)
t.setheading(0)
t.pendown()

t.color("black", "white")  # garis hitam, isi putih
t.begin_fill()
for i in range(2):
    t.forward(panjang)
    t.right(90)
    t.forward(tinggi/2)
    t.right(90)
t.end_fill()

# ==============================
# GARIS LUAR (BORDER HITAM)
# ==============================
t.penup()
t.goto(-panjang/2, tinggi/2)
t.setheading(0)
t.pendown()

t.pensize(3)
t.color("black")
for i in range(2):
    t.forward(panjang)
    t.right(90)
    t.forward(tinggi)
    t.right(90)

turtle.done()
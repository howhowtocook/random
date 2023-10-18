import turtle
turtle.screensize(3024,2768)
#从东4开始
e4 = turtle.pos()
turtle.left(90)
turtle.forward(125) #到东6了
e6 = turtle.pos()
turtle.right(15)
turtle.forward(51) #到东7了
e7 = turtle.pos()
turtle.left(15)
turtle.forward(156) #到东10了
e10 = turtle.pos()
turtle.left(90)     #左拐90
turtle.forward(223)
w1 = turtle.pos()
turtle.penup()
turtle.goto(e4)     #回东6
turtle.pendown()
turtle.left(90)
turtle.forward(125)  #到东2了
e2 = turtle.pos()
turtle.left(15)
turtle.forward(48)   #到东1了
e1 = turtle.pos()
turtle.right(15)
turtle.forward(55)   #到东0了
e0 = turtle.pos()
turtle.right(90)     #右拐
turtle.forward(223)
w0 = turtle.pos()
turtle.goto(w1)
turtle.penup()
turtle.goto(e4)
turtle.right(180)
turtle.forward(123)
b = turtle.pos()
turtle.pendown()
turtle.left(90)
turtle.forward(92)
c = turtle.pos()

turtle.right(90)
turtle.forward(78)
d = turtle.pos()
turtle.right(90)
turtle.forward(47)
e = turtle.pos()
turtle.right(90)
turtle.forward(33)
f = turtle.pos()
turtle.left(90)
turtle.forward(117)
g = turtle.pos()
turtle.right(90)
turtle.forward(45)
a = turtle.pos()
turtle.right(90)
turtle.forward(82)
turtle.penup()
turtle.goto(a)
turtle.right(180)
turtle.forward(102)
turtle.pendown()

#消防栓1
turtle.forward(49)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(49)
xfs1 = turtle.pos()
turtle.left(90)
turtle.fd(45)
turtle.penup()

#消防栓2
turtle.left(90)
turtle.forward(80)
turtle.pendown()
turtle.forward(44)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(44)
print(turtle.position())
turtle.left(90)
turtle.fd(45)



q = [30,0]


turtle.penup()
turtle.goto(q)
turtle.pendown()
turtle.right(90)
turtle.forward(350)
turtle.left(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(300)




mw1=(30,-400)
turtle.goto(mw1)
turtle.left(180)
turtle.fd(100)
turtle.left(90)
turtle.forward(25)
turtle.pencolor("blue")
turtle.left(90)
turtle.circle(-20,90)
turtle.right(90)
turtle.forward(20)
turtle.pencolor('black')
turtle.left(90)
turtle.fd(25)
turtle.left(90)
turtle.fd(100)

turtle.up()
turtle.goto(330,350)
turtle.pendown()
turtle.goto(330,-400)

#画门
turtle.goto(310,-400)
turtle.goto(310,-395)
turtle.goto(300,-395)
turtle.goto(300,-405)
turtle.goto(310,-405)
turtle.goto(310,-400)
turtle.penup()
turtle.goto(260,-400)
turtle.pendown()
turtle.goto(260,-395)
turtle.goto(250,-395)
turtle.goto(250,-405)
turtle.goto(260,-405)
turtle.goto(260,-400)
turtle.penup()
turtle.goto(250,-400)
turtle.pendown()
turtle.goto(mw1)

turtle.penup()
mw2 = [w0[0]-20,w0[1]-80]
turtle.goto(mw2)
turtle.pendown()
turtle.left(90)
turtle.fd(70)
turtle.left(90)
turtle.forward(25)
turtle.pencolor("blue")
turtle.left(90)
turtle.circle(-20,90)
turtle.right(90)
turtle.forward(20)
turtle.pencolor('black')
turtle.left(90)
turtle.fd(25)
turtle.left(90)
turtle.fd(70)
turtle.left(90)
turtle.fd(70)

















turtle.speed(60)








# 画虚线
turtle.penup()
turtle.goto(a)
turtle.pencolor('orange')
line1=[e1[0]-a[0],e1[1]-a[1]]
i=1
while i < abs(line1[0])/5 :
    turtle.pendown()
    x1 = a[0] + 5*line1[0]/abs(line1[0])*i 
    y1 = a[1] + 5*line1[1]/abs(line1[0])*i
    turtle.goto(x1 , y1)
    turtle.penup()
    i=i+1
    x1 = a[0] + 5*line1[0]/abs(line1[0])*i 
    y1 = a[1] + 5*line1[1]/abs(line1[0])*i
    turtle.goto(x1 , y1)
    i=i+1


turtle.penup()
turtle.goto(c)
line1=[e7[0]-c[0],e7[1]-c[1]]
i=1
while i < abs(line1[0])/5 :
    turtle.pendown()
    x1 = c[0] + 5*line1[0]/abs(line1[0])*i 
    y1 = c[1] + 5*line1[1]/abs(line1[0])*i
    turtle.goto(x1 , y1)
    turtle.penup()
    i=i+1
    x1 = c[0] + 5*line1[0]/abs(line1[0])*i 
    y1 = c[1] + 5*line1[1]/abs(line1[0])*i
    turtle.goto(x1 , y1)
    i=i+1

turtle.penup()
turtle.goto(g)
line1=[xfs1[0]-g[0],xfs1[1]-g[1]]
i=1
while i < abs(line1[1])/5 :
    turtle.pendown()
    y1 = g[1] + 5*i*abs(line1[1])/line1[1]
    turtle.goto(g[0] , y1)
    turtle.penup()
    i=i+1
    y1 = g[1] + 5*i*abs(line1[1])/line1[1]
    turtle.goto(g[0] , y1)
    i=i+1

turtle.penup()
turtle.goto(b)
line1=[q[0]-b[0],q[1]-b[1]]
i=1
while i < abs(line1[0])/5 :
    turtle.pendown()
    x1 = b[0] + 5*line1[0]/abs(line1[0])*i 
    y1 = b[1] + 5*line1[1]/abs(line1[0])*i
    turtle.goto(x1 , y1)
    turtle.penup()
    i=i+1
    x1 = b[0] + 5*line1[0]/abs(line1[0])*i 
    y1 = b[1] + 5*line1[1]/abs(line1[0])*i
    turtle.goto(x1 , y1)
    i=i+1

ee = [0,30]
qq = [30,30]
turtle.penup()
turtle.goto(ee)
line1=[qq[0]-ee[0],qq[1]-ee[1]]
i=1
while i < abs(line1[0])/5 :
    turtle.pendown()
    x1 = ee[0] + 5*line1[0]/abs(line1[0])*i 
    y1 = ee[1] + 5*line1[1]/abs(line1[0])*i
    turtle.goto(x1 , y1)
    turtle.penup()
    i=i+1
    x1 = ee[0] + 5*line1[0]/abs(line1[0])*i 
    y1 = ee[1] + 5*line1[1]/abs(line1[0])*i
    turtle.goto(x1 , y1)
    i=i+1

turtle.penup()
turtle.forward(1000)
turtle.right(90)
turtle.forward(1000)
turtle.right(80)


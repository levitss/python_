import turtle

# t=turtle.Turtle()
# t.shape("turtle")
# s=turtle.textinput("title","input")
# t.write(s)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)


'''
반지름이 100인 원을 그려라
60도만큼 터틀을 왼쪽으로 회전하라'''
t=turtle.Turtle()
for i in range(6):
    t.circle(100)
    t.left(60)

turtle.exitonclick()
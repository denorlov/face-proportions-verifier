import turtle

# изображение с портретом лица
img_path = './images/woman.gif'

# нижний кончик носа, координаты по x и y
bottom_nose_x, bottom_nose_y = 0, 0
# подбородок, координаты по x и y
chin_x, chin_y = 0, 0
# левый глаз, правый угол глаза, координаты по x и y
left_eye_x, left_eye_y = 0, 0
# правый глаз, левый угол глаза, координаты по x и y
right_eye_x, right_eye_y = 0, 0

# координаты центра рабочего окна  (0,0)
# верхняя горизонталь рабочего окна: +screensize_y
# нижняя горизонталь рабочего окна: -screensize_y

# левая вертикаль рабочего окна: -screensize_x
# правая вертикаль рабочего окна: +screensize_x
screensize_x, screensize_y = 0, 0

def draw_horizontal_proportions():
    delta = chin_y - bottom_nose_y

    turtle.up()
    turtle.color("lime")
    turtle.goto(-screensize_x, chin_y)
    turtle.down()
    turtle.goto(screensize_x, chin_y)
    turtle.up()

    turtle.up()
    turtle.color("blue")
    turtle.goto(-screensize_x, bottom_nose_y + delta / 3)
    turtle.down()
    turtle.goto(screensize_x, bottom_nose_y + delta / 3)
    turtle.up()

    turtle.up()
    turtle.color("lime")
    turtle.goto(-screensize_x, bottom_nose_y)
    turtle.down()
    turtle.goto(screensize_x, bottom_nose_y)
    turtle.up()

    turtle.up()
    turtle.goto(-screensize_x, bottom_nose_y - delta)
    turtle.down()
    turtle.goto(screensize_x, bottom_nose_y - delta)
    turtle.up()

    turtle.up()
    turtle.goto(-screensize_x, bottom_nose_y - 2 * delta)
    turtle.down()
    turtle.goto(screensize_x, bottom_nose_y - 2 * delta)
    turtle.up()

    turtle.up()
    turtle.color('blue')
    turtle.goto(-screensize_x, bottom_nose_y - 2 * delta - delta / 2)
    turtle.down()
    turtle.goto(screensize_x, bottom_nose_y - 2 * delta - delta / 2)
    turtle.up()

    turtle.up()
    turtle.goto(-screensize_x, chin_y - (delta / 2) * 7 / 2)
    turtle.down()
    turtle.goto(screensize_x, chin_y - (delta / 2) * 7 / 2)
    turtle.up()


def draw_vertical_proportions():
    delta = abs(left_eye_x - right_eye_x)

    turtle.color('orange')

    turtle.up()
    turtle.goto(left_eye_x, -screensize_y)
    turtle.down()
    turtle.goto(left_eye_x, screensize_y)
    turtle.up()

    turtle.up()
    turtle.goto(right_eye_x, -screensize_y)
    turtle.down()
    turtle.goto(right_eye_x, screensize_y)
    turtle.up()

    turtle.up()
    turtle.goto(left_eye_x - delta, -screensize_y)
    turtle.down()
    turtle.goto(left_eye_x - delta, screensize_y)
    turtle.up()

    turtle.up()
    turtle.goto(left_eye_x - 2 * delta, -screensize_y)
    turtle.down()
    turtle.goto(left_eye_x - 2 * delta, screensize_y)
    turtle.up()

    turtle.up()
    turtle.goto(right_eye_x + delta, -screensize_y)
    turtle.down()
    turtle.goto(right_eye_x + delta, screensize_y)
    turtle.up()

    turtle.up()
    turtle.goto(right_eye_x + 2 * delta, -screensize_y)
    turtle.down()
    turtle.goto(right_eye_x + 2 * delta, screensize_y)
    turtle.up()

def setup():
    global bottom_nose_x, bottom_nose_y, chin_x, chin_y, eye_x, eye_y
    global left_eye_x, left_eye_y
    global right_eye_x, right_eye_y
    global screensize_x, screensize_y

    screensize_x, screensize_y = turtle.screensize()

    bottom_nose_x, bottom_nose_y = 0, 0
    chin_x, chin_y = 0, 0
    left_eye_x, left_eye_y = 0, 0
    right_eye_x, right_eye_y = 0, 0

    screen = turtle.Screen()

    screen.clear()
    screen.bgpic(img_path)

    # the coordinates
    # of each corner
    cross_shape = ((0, 0), (20, 0), (0, 0), (-20, 0), (0, 0), (0, 20), (0, 0), (0, -20))

    # registering the new shape
    turtle.register_shape('cross', cross_shape)

    # changing the shape
    turtle.shape('cross')
    turtle.shapesize(10)
    turtle.color('red')

    screen.onkey(setup, 'c')
    screen.onscreenclick(get_mouse_click_coor)
    screen.listen()

def get_mouse_click_coor(x, y):
    global bottom_nose_x, bottom_nose_y, chin_x, chin_y, eye_x, eye_y
    global left_eye_x, left_eye_y, right_eye_x, right_eye_y

    if bottom_nose_x == 0 and bottom_nose_y == 0:
        bottom_nose_x = x
        bottom_nose_y = y

        turtle.up()
        turtle.goto(bottom_nose_x, screensize_y)
        turtle.down()
        turtle.goto(bottom_nose_x, -screensize_y)
        turtle.up()
        turtle.goto(bottom_nose_x, bottom_nose_y)
        turtle.down()
        turtle.dot(10)
        turtle.up()

    elif chin_x == 0 and chin_y == 0:
        chin_x, chin_y = x, y

        turtle.up()
        turtle.goto(chin_x, chin_y)
        turtle.down()
        turtle.dot(10)
        turtle.up()

        draw_horizontal_proportions()

        turtle.hideturtle()

    elif left_eye_y == 0 and left_eye_y == 0:
        left_eye_x, left_eye_y = x, y

        turtle.showturtle()

        turtle.up()
        turtle.color('red')
        turtle.goto(-screensize_x, left_eye_y)
        turtle.down()
        turtle.goto(screensize_x, left_eye_y)
        turtle.up()
        turtle.goto(left_eye_x, left_eye_y)
        turtle.down()
        turtle.dot(10)
        turtle.up()

    elif right_eye_x == 0 and right_eye_y == 0:
        right_eye_x, right_eye_y = x, y

        turtle.up()
        turtle.goto(right_eye_x, right_eye_y)
        turtle.down()
        turtle.dot(10)
        turtle.up()

        draw_vertical_proportions()

        turtle.hideturtle()

setup()
turtle.mainloop()
import turtle

def draw_bkg(size, color, target_turtle):
	retColor = target_turtle.color()
	target_turtle.color(color)
	target_turtle.penup()
	target_turtle.goto(target_turtle.xcor() - size.X / 2, target_turtle.ycor() - size.Y / 2 + 5)

	diameter = 5 * 2
	heading = target_turtle.heading()

	target_turtle.pendown()

	for _ in range(2):
		target_turtle.circle(5, 90)
		target_turtle.forward(size.X - diameter)
		target_turtle.circle(5, 90)
		target_turtle.forward(size.Y - diameter)

	target_turtle.penup()
	target_turtle.goto(target_turtle.xcor() + size.X / 2, target_turtle.ycor() + size.Y / 2 - 5)
	if target_turtle.isdown():
		target_turtle.pendown()
	target_turtle.setheading(heading)
	#target_turtle.color(retColor)

def draw_n_fill(size, color, target_turtle):
	retColor = target_turtle.color()
	target_turtle.color(color)
	target_turtle.penup()

	target_turtle.goto(target_turtle.xcor() - size.X / 2, target_turtle.ycor() - size.Y / 2 + 5)

	diameter = 5 * 2
	heading = target_turtle.heading()

	target_turtle.pendown()
	target_turtle.begin_fill()

	for _ in range(2):
		target_turtle.circle(5, 90)
		target_turtle.forward(size.X - diameter)
		target_turtle.circle(5, 90)
		target_turtle.forward(size.Y - diameter)

	target_turtle.end_fill()
	target_turtle.penup()
	target_turtle.goto(target_turtle.xcor() + size.X / 2, target_turtle.ycor() + size.Y / 2 - 5)
	
	target_turtle.setheading(heading)



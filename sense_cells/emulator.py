#!/usr/bin/python3
import threading
import turtle
import random
import time
import init
import sys
import re

global sensor
global window
global funcs
global isinfunc
global incomment

funcs = dict()
currentfunc = None

isinfunc = False

incomment = False

class Cell:
	def __init__(self):
		self.color = None
		self.t_obj = turtle.Turtle(shape='circle')
		self.t_obj.shapesize(3)
		self.t_obj.speed(0)
		self.t_obj.penup()
		self.t_obj.ht()

	def initialize(self, color='#787878'):
		self.color = color
		self.t_obj.color(color)
	
	def set_color(self, color):
		self.color = color
		self.t_obj.color(self.color)

class Vector2:
	def __init__(self, x = -1, y = -1):
		self.X = x
		self.Y = y
	
	def __repr__(self):
		return (self.X, self.Y)
	
	def __str__(self):
		return f"({self.X}, {self.Y})"

class Senser:
	def __init__(self, countx, county):
		self.cells = [[Cell() for x in range(countx)] for y in range(county)]
		self.cell_count = Vector2(countx, county)
		
	def initialize_all(self):
		self.initializeAll()

	def initializeAll(self):
		px = -390/2
		py = 390/2 - 10
		for j in range(self.cell_count.Y):
			px = -390/2
			for i in range(self.cell_count.X):
				self.cells[j][i].initialize()
				self.cells[j][i].t_obj.goto(px, py)
				self.cells[j][i].t_obj.showturtle()
				px += 80
				
				if px >= 390:
					print("Too many x Objects")
					print(self.cell_count)
			if py <= -390/2:
				print("Too many y objects!")
				print(self.cell_count)
				print("current y:", j+1)
				sys.exit(1)
			py -= 90

sensor = Senser(6, 5)
			
def matchesColor(obj: str) -> bool:
	for color in ("yellow, gold, orange, red, maroon, violet, magenta, purple, navy, blue, skyblue, cyan, turquoise, lightgreen, green, darkgreen, chocolate, brown, black, gray, white".split(', ')):
		if obj == color or re.match(r"#([0-9A-F]{6})", obj):
			return True
	return False

def gen_random_color():
	rstr = '#'
	for _ in range(6):
		rstr += random.choice(list('0123456789ABCDEF'))
	return rstr

def InterpretInput(str_input: str) -> None:
	global currentfunc
	global incomment
	global isinfunc
	global window
	global sensor
	global funcs

	# check if insdie comments
	if incomment:
		if '*/' in str_input:
			str_input = str_input[str_input.find('*/')+2:]
			incomment = False
		else:
			return

	str_input = str_input.strip().lower()
	# current adding words to a function
	if isinfunc:
		if str_input == "end":
			isinfunc = False
			currentfunc = None
		else:
			funcs[currentfunc].append(str_input)

	# call help command
	elif str_input == "help":
		print("set [cell.../color] <color>")

	# single line comment
	elif str_input.startswith('//'):
		return
	#multiline comment
	elif str_input.startswith('/*'):
		incomment = True

	# set a cell to a certain color
	elif str_input.startswith("set "):
		splitinput = str_input.split(' ')
		if len(splitinput) < 2:
			print("invalid input!")
		elif matchesColor(splitinput[-1]) or splitinput[-1] == 'rand_color':
			if len(splitinput) == 2:
				for y in range(sensor.cell_count.Y):
					for x in range(sensor.cell_count.X):
						if splitinput[-1] == 'rand_color':
							sensor.cells[y][x].set_color(gen_random_color())
						else:
							sensor.cells[y][x].set_color(splitinput[1])
			else:
				newinp = splitinput[1:len(splitinput)-1]
				#currentcell = []
				#try:
				for cell in newinp:
					line = list(cell)[0].upper()
					#print(enumerate(list("ABCDE")))
					for i in enumerate(list("ABCDE")):
						if line == i[1]:
							line = i[0]
							break
					else:
						print("Out of range!")
						sys.exit(1)
					
					if len(list(cell)) == 1:
						for i in range(6):
							print(i)
							if splitinput[-1] == 'rand_color':
								sensor.cells[line][i].set_color(gen_random_color())
							else:
								sensor.cells[line][i].set_color(splitinput[-1])
					else:
						col = int(list(cell)[1])

						if splitinput[-1] == 'rand_color':
							randomcolor = gen_random_color()
							sensor.cells[line][col].set_color(randomcolor)
						else:
							sensor.cells[line][col].set_color(splitinput[-1])

	# check for the sleep function
	elif str_input.startswith("sleep") or str_input.startswith("slp"):
		if len(str_input.strip().split()) < 2:
			print("Invalid use for sleep command!")
		else:
			time.sleep(float(str_input.split()[1]))

	# creates functions
	elif str_input.startswith("func "):
		if len(str_input.split())  != 2:
			print("failed to create function. Template: \"func myfunc:\"")
		elif isinfunc:
			print("already in function. cannot create nested functions.")
		else:
			isinfunc = True
			currentfunc = str_input.split()[1].replace(':', '')
			funcs[currentfunc]=list()

	# user wants to exit
	elif str_input == "exit":
		sys.exit(0)

	# user called a function
	elif str_input in funcs.keys():
		for com in funcs[str_input]:
			InterpretInput(com)

	# user entered nothing
	elif len(str_input.strip()) == 0:
		return

	# invalid input
	else:
		print(f"invalid command: {str_input}")

	window.update()

def CreateGUI():
	global sensor
	global window
	window = turtle.Screen()
	window.screensize(800, 710)
	#window.update()
	filler = turtle.Turtle()
	filler.speed(0)
	filler.hideturtle()
	filler.penup()
	filler.pensize(4)
	filler.fd(600)
	init.draw_n_fill(Vector2(600, 600), '#474747', filler)
	filler.penup()
	filler.goto(500, 0)
	init.draw_n_fill(Vector2(500, 500), 'green', filler)
	window.update()
	sensor.initializeAll()

def InteractiveSession():
	global sensor
	global window
	global funcs
	global isinfunc
	global currentfunc
	CreateGUI()
	TakeInput()

def PostFileInteractiveSession():
	global sensor
	global funcs
	global isinfunc
	global currentfunc
	TakeInput()
	
def TakeInput():
	while True:
		str_input = input("~>: ")
		InterpretInput(str_input)

	# sensor = Senser(5, 5)
	# sensor.initialize_all()


if __name__ == '__main__':
	if len(sys.argv) <= 1:
		
		InteractiveSession()
		
	else:
		CreateGUI()
		with open(sys.argv[1], 'r') as f:
			for line in f.readlines():
				InterpretInput(line.replace('\n', ''))
		PostFileInteractiveSession()
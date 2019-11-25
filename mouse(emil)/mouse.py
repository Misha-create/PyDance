import pygame
import threading
import time
class Main_screen():
	def __init__(self):
		global pygame
		pygame.init()
		self.path = "C:/Users/DNS/Desktop/pydance/"
		self.path.replace('/','\\')
		self.screen = pygame.display.set_mode((500,400))
		self.screen.fill(pygame.Color("yellow"))
		pygame.display.set_caption('pydance')
screen = Main_screen()




class point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


points = []
pressed = []

def new_point():
	global pressed
	pos = pygame.mouse.get_pos()
	dot = point(pos[0], pos[1])
	points.append(dot)
	pressed = pygame.mouse.get_pressed()

new_point()

while pressed[0] and not pressed[2]:
	threading.Timer(100, new_point).start()





is_it_left = True
is_it_right = True
is_it_up = True
is_it_down = True

min_x = points[0].x
max_x = points[0].x
min_y = points[0].y
max_y = points[0].y


for i in range(1, len(points)):
	if points[i].x > points[i - 1].x:
		is_it_left = False
	elif points[i].x != points[i - 1].x:
		is_it_right = False

	if points[i].y < points[i - 1].y:
		is_it_up = False
	elif points[i].y != points[i - 1].y:
		is_it_down = False

	min_x = min(points[i].x, min_x)
	max_x = max(points[i].x, max_x)
	min_y = min(points[i].y, min_y)
	max_y = max(points[i].y, max_y)


is_it_round = not(is_it_left + is_it_right + is_it_up + is_it_down)

if max_x == min_x:
	restangle_sides_ratio = 1
else:
	restangle_sides_ratio = (max_y - min_y)/(max_x - min_x)


curvature = []


for i in range(2, len(points)):
	a = ((points[i-2].x - points[i-1].x) ** 2 + (points[i-2].y - points[i-1].y) ** 2) ** 0.5
	b = ((points[i-1].x - points[i].x) ** 2 + (points[i-1].y - points[i].y) ** 2) ** 0.5
	c = ((points[i-2].x - points[i].x) ** 2 + (points[i-2].y - points[i].y) ** 2) ** 0.5
	p = (a + b + c) / 2
	S = (p * (p - a) * (p - b) * (p - c)) ** 0.5

	if S != 0:
		k = 4 * S / a / b / c

	curvature.append(k)


k_min = curvature[0]
k_max = curvature[0]
for i in range(1, len(K)):
	k_min = min(curvature[i], k_min)
	k_max = max(curvature[i], k_max)
e = k_max / k_min - 1


it_is = 'I do not know'

if is_it_round:
	if e < 0.5:
		it_is = 'round'
elif is_it_left:
	if restangle_sides_ratio < 0.5:
		it_is = 'left'
elif is_it_right:
	if restangle_sides_ratio < 0.5:
		it_is = 'right'
elif is_it_up:
	if restangle_sides_ratio > 2:
		it_is = 'up'
elif is_it_down:
	if restangle_sides_ratio > 2:
		it_is = 'down'


print(it_is)
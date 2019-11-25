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
class Animaton_person(Main_screen):
	def __init__(self):
		global pygame
		super().__init__()
		self.surf = pygame.Surface((0, 0))
		self.coords = []
		self.one_shot_time = 0
		self.imgs_animations = []
		self.animations_movies = []
	def do_animation(self,type):
		global pygame
		#img = None
		def draw_shot(type,i):
			img = None
			self.surf.fill(pygame.Color("yellow"))
			self.screen.blit(self.surf, (self.coords[0],self.coords[1]))
			if type == 0:
					self.coords[0]+=self.animations_movies[0][i]
					img = self.imgs_animations[0][i]
			else:
					self.coords[0]+=self.animations_movies[1][i]
					img = self.imgs_animations[1][i]
			self.surf.fill(pygame.Color("yellow"))
			self.surf.blit(img, (0,0))
			self.screen.blit(self.surf, (self.coords[0],self.coords[1]))
			pygame.display.update()
		for j in range(len(self.imgs_animations[0])):
			t = threading.Timer(j*50.00/1000,draw_shot,(type,j))
			t.start()
class Snoop(Animaton_person):
	def __init__(self):
		super().__init__()
		self.surf = pygame.Surface((48, 104))
		self.coords = [200,200]
		self.one_shot_time = 100
		self.imgs_animations = []
		self.imgs_animations.append([
		pygame.image.load(self.path+'1_right.png'),
		pygame.image.load(self.path+'2_right.png'),
		pygame.image.load(self.path+'3_right.png'),
		pygame.image.load(self.path+'4_right.png'),
		pygame.image.load(self.path+'5_right.png'),
		pygame.image.load(self.path+'6_right.png'),
		pygame.image.load(self.path+'7_right.png'),
		pygame.image.load(self.path+'8_right.png')
		])
		self.imgs_animations.append([
		pygame.image.load(self.path+'1_left.png'),
		pygame.image.load(self.path+'2_left.png'),
		pygame.image.load(self.path+'3_left.png'),
		pygame.image.load(self.path+'4_left.png'),
		pygame.image.load(self.path+'5_left.png'),
		pygame.image.load(self.path+'6_left.png'),
		pygame.image.load(self.path+'7_left.png'),
		pygame.image.load(self.path+'8_left.png')
		])
		self.animations_movies.append([2,2,2,2,2,2,2,2])
		self.animations_movies.append([-2,-2,-2,-2,-2,-2,-2,-2])
screen = Main_screen()
anim  =Animaton_person()
def main():
	sd1 = Snoop()
	sd2 = Snoop()
snoop_dogs =[]
for i in range(10):
	snoop_dogs.append(Snoop())
	snoop_dogs[i].coords[0] = 0+i*50
in_move = False
while 1:
	for i in pygame.event.get():
			if i.type == pygame.KEYDOWN:
				if i.key == pygame.K_LEFT and not in_move:
					pygame.event.set_blocked(pygame.KEYDOWN)
					for j in snoop_dogs:
						j.do_animation(1)
					pygame.event.set_allowed(pygame.KEYDOWN)
				if i.key == pygame.K_RIGHT and not in_move:
					pygame.event.set_blocked(pygame.KEYDOWN)
					for j in snoop_dogs:
						j.do_animation(0)
					pygame.event.set_allowed(pygame.KEYDOWN)
			if i.type == pygame.QUIT:
				exit()
import pygame
import threading
import time
class Main_screen():
	def __init__(self):
		pygame.init()
		self.path = "C:/Users/DNS/Desktop/pydance/"
		self.path.replace('/','\\')
		self.screen = pygame.display.set_mode((500,500))	
		self.goals = pygame.Surface((500,50))
		self.symbols = pygame.Surface((100,30))
		pygame.display.set_caption('pydance')
	def set_scene(self):
		#self.screen.fill((204,255,51))
		self.screen.blit(pygame.image.load(self.path + "bg.png" ), (0,0))
		self.goals.fill((255,0,102))
		#self.incsription_above.fill((255,0,102))
		self.goals.blit(pygame.image.load(self.path + "goals.png" ), (220,0))#добавить центрирование
		#self.screen.blit(self.incsription_above,(0,5))
		self.screen.blit(self.goals,(0,60))
class Animaton_person():
	def __init__(self,screen,path,is_scene):
		self.screen =screen
		self.path = path
		self.is_scene = is_scene
		self.surf = pygame.Surface((0, 0))
		self.coords = []
		self.one_shot_time = 0
		self.imgs_animations = []
		self.animations_movies = []
	def do_animation(self,type,num):
		def draw_shot(type,i):
			img = None
			self.surf.fill((255,0,102))
			self.screen.blit(self.surf, (self.coords[0],self.coords[1]))
			self.coords[0]+=self.animations_movies[type][i]
			img = self.imgs_animations[type][i]
			self.surf.fill((255,0,102))
			self.surf.blit(img, (0,0))
			self.screen.blit(self.surf, (self.coords[0],self.coords[1]))
			pygame.display.update()
		if not self.is_scene:
			block_timer = threading.Timer(0,pygame.event.set_blocked,[pygame.KEYDOWN])
			allow_timer = threading.Timer(len(self.imgs_animations[type])*self.one_shot_time/1000 -200/1000,pygame.event.set_allowed,[pygame.KEYDOWN])
			allow_timer.start()
			block_timer.start()
		for i in range(num):
			for j in range(len(self.imgs_animations[type])):
				t = threading.Timer(i*len(self.imgs_animations[type])*self.one_shot_time/1000 +  j*self.one_shot_time/1000,draw_shot,(type,j))
				t.start()
class Sheep(Animaton_person):
	def __init__(self,screen,path,is_scene):
		super().__init__(screen,path,is_scene)
		self.surf = pygame.Surface((100,100))
		self.coords = [0,100]
		self.one_shot_time = 50
		self.imgs_animations = []
		self.imgs_animations.append([])
		self.animations_movies.append([])
		for i in range(99):
			self.imgs_animations[0].append(pygame.image.load(self.path + 'd3/5011a4d85853406fe543643984c44bb7-'+str(i)+'.png'))	
			self.animations_movies[0].append(2)
class Start_scene():
	def __init__(self,screen,path):
		self.path = path
		self.screen = screen
		self.surf = pygame.Surface((500,500))
		self.surf.blit(pygame.image.load(self.path + "start.png" ), (0,0))
		self.screen.blit(self.surf,(0,0))
class Girl(Animaton_person):
	def __init__(self,screen,path,is_scene):
		super().__init__(screen,path,is_scene)
		self.surf = pygame.Surface((110,128))
		self.coords = [245,250]
		self.one_shot_time = 95
		self.imgs_animations = []
		self.imgs_animations.append([])
		self.animations_movies.append([])
		for i in range(4):
			self.imgs_animations[0].append(pygame.image.load(self.path + '/2d/0/'+str(i)+'.png'))	
			self.animations_movies[0].append(1)
		self.imgs_animations.append([])
		self.animations_movies.append([])
		for i in range(4):
			self.imgs_animations[1].append(pygame.image.load(self.path + '/2d/1/'+str(i)+'.png'))	
			self.animations_movies[1].append(-1)
		self.imgs_animations.append([])
		self.animations_movies.append([])
		for i in range(7):
			self.imgs_animations[2].append(pygame.image.load(self.path + '/2d/2/'+str(i)+'.png'))	
			self.animations_movies[2].append(0)
		self.imgs_animations.append([])
		self.animations_movies.append([])
		for i in range(7):
			self.imgs_animations[3].append(pygame.image.load(self.path + '/2d/3/'+str(i)+'.png'))	
			self.animations_movies[3].append(0)
		self.imgs_animations.append([])
		self.animations_movies.append([])
		for i in range(7):
			self.imgs_animations[4].append(pygame.image.load(self.path + '/2d/4/'+str(i)+'.png'))	
			self.animations_movies[4].append(0)
		self.imgs_animations.append([])
		self.animations_movies.append([])
		for i in range(4):
			self.imgs_animations[5].append(pygame.image.load(self.path + '/2d/5/'+str(i)+'.png'))	
			self.animations_movies[5].append(0)
		self.imgs_animations.append([])
		self.animations_movies.append([])
		for i in range(4):
			self.imgs_animations[6].append(pygame.image.load(self.path + '/2d/6/'+str(i)+'.png'))	
			self.animations_movies[6].append(0)
screen = Main_screen()
file = open('text.txt', 'r')
def set_symbol(symbol):
	global screen
	screen.symbols.fill((255,153,153))
	screen.symbols.blit(pygame.image.load(screen.path + '/symbols/' + str(symbol) + '.png'),(0,0))
	screen.screen.blit(screen.symbols,(205,427))
	pygame.display.update()
def set_symbols():
	for line in file:
		print((line.split(' ')[1]))
		timer = threading.Timer(float(line.split(' ')[1]),set_symbol,[int(line.split(' ')[0])])
		timer.start()
	file.close()
start = Start_scene(screen.screen,screen.path)

pygame.display.update()
def play():
	girl = Girl(screen.screen,screen.path,False)
	screen.set_scene()
	sound2 = pygame.mixer.Sound('untitled.wav')
	#sound2.play()
	#start = time.time()
	set_symbols()
	snoop_dogs =[]
	sheep = Sheep(screen.screen,screen.path,True)
	#sheep.do_animation(0,3)
	goals =0
	while 1:
		for i in pygame.event.get():
				if i.type == pygame.KEYDOWN:
					if i.key == pygame.K_LEFT:
						girl.do_animation(1,1)
						
					if i.key == pygame.K_RIGHT:
						girl.do_animation(0,1)
					if i.key == pygame.K_UP:
						girl.do_animation(2,1)
					if i.key == pygame.K_DOWN:
						girl.do_animation(3,1)
					if i.key == pygame.K_SPACE:
						girl.do_animation(4,1)
					if i.key == pygame.K_a:
						girl.do_animation(5,1)
					if i.key == pygame.K_d:
						girl.do_animation(6,1)
				if i.type == pygame.QUIT:
					exit()
while 1 :
	for i in pygame.event.get():
		if i.type == pygame.MOUSEBUTTONDOWN and i.pos[0] < 294 and i.pos[0] > 215 and i.pos[1] < 205 and i.pos[1] > 180:
			play()
		if i.type == pygame.MOUSEBUTTONDOWN and i.pos[0] < 294 and i.pos[0] > 215 and i.pos[1] < 360 and i.pos[1] > 333:
			exit()

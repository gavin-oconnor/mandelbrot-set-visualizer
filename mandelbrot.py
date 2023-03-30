import pygame
import cmath

WIDTH = 500
HEIGHT = 500

START_I = -2
END_R = 2
END_I = 2
START_R = -2
x_offset = 0
y_offset = 0
win = pygame.display.set_mode((WIDTH,HEIGHT))
run = True
line_increment = 50

def pixel_to_complex(x,y):
	re = (x/WIDTH) * (END_R-START_R) - (END_R-START_R)/2 + x_offset
	im = (y/HEIGHT) * -1*(END_I-START_I) + (END_I-START_I)/2 + y_offset
	return (re, im)

def complex_to_pixel(re,im):
	x = (re+2)/4 * 500
	y = (im-2)/(-4) * 500
	return (x,y)
avg = 0
amt = 0
def mandelbrot(re,im):
	global avg, amt
	s = set()
	c = complex(re,im)
	z = complex(0,0)
	for i in range(40):
		if z in s:
			return (255,255,255)
		if abs(z) > 2:
			return (0,0,0)
		s.add(z)
		z = z**2 + c
		if z == 0:
			return (255,255,255)
	return (255,255,255)

pxls = []
for row in range(500):
	temp = []
	for col in range(500):
		temp.append((0,0,0))
	pxls.append(temp)

def calc():
	global avg, amt
	global pxls
	pxls = []
	for row in range(500):
		temp = []
		for col in range(500):
			temp.append((0,0,0))
		pxls.append(temp)
	for row in range(500):
		for col in range(500):
			re,im = pixel_to_complex(col,row)
			pxls[row][col] = mandelbrot(re,im)



def draw():
	win.fill((0,0,0))
	for row in range(500):
		for col in range(500):
			pygame.draw.rect(win, pxls[col][row],(row,col,1,1))
	pygame.display.update()




calc()

# print(pxls)

drawn = False
run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYUP:
			#LARGE ZOOM
			if event.key == pygame.K_g:
				START_I /= 2
				START_R /= 2
				END_I /= 2
				END_R /= 2
				drawn = False
			#LARGE ZOOM OUT
			elif event.key == pygame.K_h:
				START_I *= 2
				START_R *= 2
				END_I *= 2
				END_R *= 2
				drawn = False
			#MOVE CAM RIGHT
			elif event.key == pygame.K_RIGHT:
				x_offset += 0.1
				drawn = False
			#MOVE CAM LEFT
			elif event.key == pygame.K_LEFT:
				x_offset -= 0.1
				drawn = False
			#MOVE CAM UP
			elif event.key == pygame.K_UP:
				y_offset += 0.1
				drawn = False
			#MOVE CAM DOWN
			elif event.key == pygame.K_DOWN:
				y_offset -= 0.1
				drawn = False
			elif event.key == pygame.K_q:
				x_offset += 0.01
				drawn = False
			elif event.key == pygame.K_w:
				x_offset -= 0.01
				drawn = False
			elif event.key == pygame.K_e:
				y_offset += 0.01
				drawn = False
			elif event.key == pygame.K_r:
				y_offset -= 0.01
				drawn = False
			#LIL ZOOM
			if event.key == pygame.K_o:
				START_I /= 1.1
				START_R /= 1.1
				END_I /= 1.1
				END_R /= 1.1
				drawn = False
			elif event.key == pygame.K_p:
				START_I *= 1.1
				START_R *= 1.1
				END_I *= 1.1
				END_R *= 1.1
				drawn = False
			elif event.key == pygame.K_SPACE:
				pygame.image.save(win,f"PICTURE.jpg")
	if not drawn:
		calc()
		draw()











import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки. 

def r(int):
	return random.randint(0,int)

def rc(list):
	return random.choice(list)

def md(x,y,color):
	mDraw.point([x,y], color)

def mt(x,y,color):
	tDraw.point([x,y], color)

white = (255,255,255)
black = (0,0,0)


imgMap = Image.open("start.png") #Открываем изображение. 
mDraw = ImageDraw.Draw(imgMap) #Создаем инструмент для рисования. 
w1 = imgMap.size[0] #Определяем ширину. 
h1 = imgMap.size[1] #Определяем высоту. 	
pix1 = imgMap.load() #Выгрузка пикселей в массив

imgTiles = Image.open("tiles.png")
tDraw = ImageDraw.Draw(imgTiles)
w2 = imgTiles.size[0]
h2 = imgTiles.size[1]
pix2 = imgTiles.load()


# for x in range(w1):
# 	for y in range(h1):
# 		md(x, y, S)
x = int(w1/2)
y = int(h1/2)

for i in range(10000):
	x += rc([1,0,-1])
	y += rc([1,0,-1])

	md(x, y, white)
imgMap.save("finish.png", "PNG")








del mapDraw
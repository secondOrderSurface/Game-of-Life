import datetime
import numpy as np
from pygame import sprite
### Только для Windows
from win32api import GetSystemMetrics 

### Const

FPS = 60
WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
BLACK = (0, 0, 0)
ROCK = (101,83,83)
SKY = (66,170,255)
WIDTH = GetSystemMetrics(0)
HEIGHT = GetSystemMetrics(1)

### Groups

Grid = sprite.Group()
RedCells = sprite.Group()
Blocks = sprite.Group()
Clouds = sprite.Group()
Environment = sprite.Group()

### Game data

GridPos = []
WaterPos = np.array([])
CloudPos = np.array([])
SqS = 10

time = datetime.datetime(1, 12, 1, 10, 0, 0)

### Environment control
frequencyLet = 20
frequencyClouds = 25
speedOfClouds = 4
maxWater = 1000
chanceRain = 10
chanceStopRain = 50
averageRainIntensity = 50
standardDeviationRain = 5
evaporationRate = 5

### Cell Control

visionDistance = 2

### GUI

activeGrid = False
activeClouds = True
radiationMap = False
pause = False



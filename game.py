import pygame

#initialize  the python game
pygame.init()

# dimensions
screen_width = 1000
screen_height = 1000
play_area_width = 900
play_area_height = 900
block = 100

# colors
black = (0, 0, 0)
yellow = (255,255,0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0,255,0)
# white = (255,255,255)
brown = (139,69,19)

# coordinates
starting = (1,8)
ending = (8,1)
obstacle1 = [(1,1),(2,1),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(2,7),(1,7)]
obstacle2 = [(8,2),(7,2),(6,2),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(6,8),(7,8),(8,8)]
path = [(2, 8), (3, 8), (4, 8), (4, 7), (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (5, 1), (6, 1), (7, 1)]


# creating the screen with 1000 x 1000 dimension
screen = pygame.display.set_mode((screen_width,screen_height))

#setting name of game window
pygame.display.set_caption("Path Finding")

# 
def grid():
    for x  in range(100,play_area_width,block):
        for y in range(100,play_area_height,block):
            
            rect = pygame.Rect(x,y,block,block)

            # filling grid area with yellow color
            screen.fill(yellow,rect = rect)

            # starting point
            drawPoint(starting, blue)

            # ending point
            drawPoint(ending, red)

            # obstacles
            drawObstacles(obstacle1,obstacle2)

            # drawEndingPoint(rect, ending)
            pygame.draw.rect(screen,black,rect,1)
            

def drawPoint(point, color):
    x, y = point
    rect = pygame.Rect(x*block, y*block, block, block)
    screen.fill(color=color, rect=rect)

def drawPath(path):
    for point in path:
        drawPoint(point,green)
        
def fillPoints(points,color):
    for point in points:
        drawPoint(point,color)

def drawObstacles(*obstacles):
    for obstacle in obstacles:
        fillPoints(obstacle,brown)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    grid()

    drawPath(path)

    pygame.display.flip()
# pygame.quit()


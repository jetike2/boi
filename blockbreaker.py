import pygame
import random
import sys
#level1
global level1
level1 =[
        [0,0,0,0,1,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,0,0,0],
        [0,0,0,1,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0]
        ]
def reset_array(array):
    for line in array:
        for i,num in enumerate(line):
            if num == 2:
                line[i] = 1
            
#colour
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
#paddle
class paddle:
    def __init__(self,x,y,width,height,vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self. vel = vel
Paddle = paddle(350,550,80,20,5)
def draw_paddle():
    pygame.draw.rect(screen,red,(Paddle.x,Paddle.y,Paddle.width,Paddle.height))
#ball
class ball:
    def __init__(self,x,y,rad,velx,vely):
        self.x = x
        self.y = y
        self.rad = rad
        self.velx = velx
        self.vely = vely
Ball = ball(30,30,10,2,5)
def ball_move():
    Ball.x -= Ball.velx
    Ball.y -= Ball.vely
#block
class block:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
Block = block(0,0,75,35)
def draw_block(self,array):
    x = self.x
    y = self.y
    for line in array:
        for character in line:
            if character == 1:
                pygame.draw.rect(screen,white,(x,y,self.width,self.height))
                pygame.draw.rect(screen,red,(x,y,self.width,self.height),1)
            x += self.width
        y += self.height
        x = 0
def draw_ball():
    pygame.draw.circle(screen,white,(Ball.x,Ball.y), Ball.rad)
#init   
pygame.init()
#window
swidth = 800
sheight = 600
screen = pygame.display.set_mode((swidth,sheight))
 
def main():
    #gamestart bool
    global gamestart
    gamestart = False
    #player lives
    global player_lives
    player_lives = 3
    #main loop    
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()   
        if player_lives <= 0:
            reset_array(level1)
            player_lives = 3
        #paddlemove
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            Paddle.x -= Paddle.vel
        if key[pygame.K_d]:
            Paddle.x += Paddle.vel
        if Paddle.x + 80 < 0:
            Paddle.x += swidth
        if Paddle.x >= swidth:
            Paddle.x -= swidth
        #ballmove
        posx = Ball.y
        posy = Ball.x
        row = posx // 35
        column = posy // 75
        if level1[row][column] == 1:
           level1[row][column] = 2
           Ball.vely = -Ball.vely
        if gamestart == False:
            Paddle.x = 350
            Ball.x = Paddle.x + 40
            Ball.y = Paddle.y - 10
            Ball.velx = 2
            Ball.vely = 5    
        if key[pygame.K_SPACE]:
            gamestart = True
        if gamestart == True:
            ball_move()
        if Ball.y <= 0:
            Ball.vely = - Ball.vely
        if Ball.y >= 600:
            gamestart = False
            player_lives -= 1
            print(player_lives)
        if Ball.x <= 0:
            Ball.velx = - Ball.velx
        if Ball.x >= 800:
            Ball.velx = - Ball.velx
        #collision
        if Paddle.x <= Ball.x <= Paddle.x +44 and Paddle.y == Ball.y:
            Ball.vely = - Ball.vely
            if Ball.x > Paddle.x:
                Ball.velx =  Ball.velx
            if Ball.x < Paddle.x:
                Ball.velx = -Ball.velx
        if Paddle.x +45 <= Ball.x <= Paddle.x +80 and Paddle.y == Ball.y:
            Ball.vely = - Ball.vely
            if Ball.x < Paddle.x:
                Ball.velx = - Ball.velx
            if Ball.x > Paddle.x:
                Ball.velx = Ball.velx
        #game end
        victory = False
        for line in level1:
            for col in line:
                if all(all(item != 1 for item in item)for item in level1):
                    victory = True
        if victory == True:
            print("you win")
            break
        screen.fill(blue)
        draw_paddle()
        draw_ball()
        draw_block(Block,level1)
        pygame.display.flip()
        
main()

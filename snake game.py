
import pygame
import time
import random

# start the game
pygame.init()

#define some colors (RGB values)
white=[255,255,255]
red = [255,0,0]
blue = [0,0,255]
black = [0,0,0]
green = [0,255,0]

game_over = False

# define height and width of the window 
width = 1000
height = 500

# define size of each block in snake
block_size = 10
snake_speed =10
snake_list = []

# create a window object using set_mode() method
dis = pygame.display.set_mode((width,height))

# set title or caption for the window
pygame.display.set_caption("snake game using python")

# update the window everytime if you made any changes
pygame.display.update()

# create an object for clock
clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# function for displaying snake 
def snake(snake_list):
    for snake in snake_list:
        pygame.draw.rect(dis,black,[snake[0],snake[1],block_size,block_size])
        
        
# function to display text on the window after game over !
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width//4, height//2])

# function to display score 
def score(s):
    value = font_style.render("YOUR SCORE : " + str(s),True,green)
    dis.blit(value,[0,0])

# snake game main function 
def gameloop():
    game_over = False
    game_exit = False

    x1 = width // 2
    y1 = height // 2

    x1_change = 0
    y1_change = 0
    length_of_snake = 1
    
    foodx = round(random.randrange(5,width-block_size)/10.0)*10.0
    foody = round(random.randrange(0,height-block_size)/10.0)*10.0

    while not game_over:
        while game_exit==True:
            dis.fill(white)
            message("YOU LOST ENTER 'C' TO CONTINUE OR 'Q' TO QUIT",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key ==pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over= True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
        
        # setting boundaries 
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_exit = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis,blue,[foodx,foody,block_size,block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list)>length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x==snake_head:
                game_over=True

        snake(snake_list)
        score(length_of_snake)
        pygame.display.update()

        if x1==foodx and y1==foody:
            foodx = round(random.randrange(5, width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            length_of_snake+=1

        clock.tick(snake_speed)
    pygame.quit()
    quit()

gameloop()

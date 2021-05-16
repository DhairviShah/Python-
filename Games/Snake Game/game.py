import pygame
import random

pygame.mixer.init()
pygame.init()


# colors
white = (255,255,255)
red=(255,0,0)
black=(0,0,0)
green = (0,255,0)
blue = (0,0,255)


gameWindow = pygame.display.set_mode((900,600)) # game's window
pygame.display.set_caption("Snake Game") # title of our Game
pygame.display.update()
clock = pygame.time.Clock()


# presenting score on screen
font = pygame.font.SysFont(None,55)


def score_screen(text , color, x , y):
    screen_score = font.render(text,True,color)
    gameWindow.blit(screen_score,[x,y])

# plotting snake
def plot_snake(gameWindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])


# defining welcome st
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(green)
        score_screen("Welcome to Snake Game", black, 260, 250)
        score_screen("Press Space Bar To Play", black, 232, 290)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                exit_game = True
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    pygame.mixer.music.load("back.mp3")
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)



# defining  game_loop
def gameloop():

    # game variables
    exit_game = False
    game_over = False
    snake_x = 98
    snake_y = 112
    snake_size = 15
    snake_list = []
    snake_length = 1
    with open("high.txt","r") as f:
        high_score = f.read()

    fps = 50
    x_velo = 0
    y_velo = 0
    initial_velo = 5
    score = 0
    food_x = random.randint(30, 900/2.5)
    food_y = random.randint(30,600/2.5)

        
    while not exit_game:
       
        if game_over == True:
            gameWindow.fill(black)
            score_screen("Game Over ... Press Enter to continue!",white,100,250)

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    exit_game = True

                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_RETURN:
                        welcome()
        else:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    exit_game = True
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_RIGHT:
                        x_velo = initial_velo
                        y_velo = 0
                    elif events.key == pygame.K_LEFT:
                        x_velo = -initial_velo
                        y_velo = 0
                    elif events.key == pygame.K_UP:
                        y_velo = -initial_velo
                        x_velo = 0
                    elif events.key == pygame.K_DOWN:
                        y_velo = initial_velo
                        x_velo = 0
                    elif events.key == pygame.K_q:
                        score +=2
            snake_x += x_velo
            snake_y += y_velo

            if abs(snake_y - food_y)<10 and abs(snake_x - food_x)<10 :
                score += 1
                # print("your score is :", score )
                food_x = random.randint(30, 900/2.5)
                food_y = random.randint(30,600/2.5)
                snake_length +=5
                if score>int(high_score):
                    high_score = score

            gameWindow.fill(black)
            score_screen("your score is " + str(score) +  "  Highscore: "+str(high_score), white , 8,8)

            # increasing length of snake 
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]
            # print(head)
            # print(snake_list)

            # collision logic
            if head in snake_list[:-1]:
                
                game_over = True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()

            # if snake goes out of screen then game over
            if snake_x<0 or snake_x>900 or snake_y<0 or snake_y>600:
                game_over = True
                # print("okay")
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()

            plot_snake(gameWindow,red,snake_list,snake_size)
            pygame.draw.rect(gameWindow,blue,[food_x,food_y,snake_size,snake_size])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
import pygame
import random

pygame.init()

WIDTH = 400
HEIGHT = 600



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

def start():

    start_font = pygame.font.Font("freesansbold.ttf", 30)
    class StartButton():
        def __init__(self):
            self.x = 100
            self.y = 200
            self.width = 200
            self.height = 100

        def draw(self):
            pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
            score = start_font.render("Start Game", True, (255, 255, 255))
            screen.blit(score, (115, 235))

    button = StartButton()

    running = True

    while running:
        screen.fill((169,169,169))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.QUIT()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x >= button.x and x <= button.x+200 and y >= button.y and y <= button.y+100:
                    main()
                    running = False

        button.draw()
        pygame.display.update()

def main():
    score_font = pygame.font.Font("freesansbold.ttf", 50)

    clock = pygame.time.Clock()

    class Bird():
        def __init__(self):
            self.x = 40
            self.y = HEIGHT/2
            self.gravity = 0.7
            self.vel = 0
            self.lift = 16
            self.p_score = 0

        def draw(self):
            self.bird = pygame.draw.circle(screen, (0,0,0), (self.x,self.y), 15)

        def fall(self):
            self.vel += self.gravity
            self.y += self.vel
            if self.y > HEIGHT:
                self.y = HEIGHT
                self.vel = 0
                start()
                running = False
            elif self.y < 0:
                self.y = 0
                self.vel = 0

        def up(self):
            self.vel -= self.lift

        def hit(self):
            if self.x >= pipe1.x and self.y <= pipe1.y+pipe1.height:
                start()
                running = False

            elif self.x >= pipe1.x and self.y >= HEIGHT-pipe1.heightb:
                start()
                running = False

            elif self.x >= pipe1.x1 and self.y <= pipe1.y+pipe1.height1:
                start()
                running = False

            elif self.x >= pipe1.x1 and self.y >= HEIGHT-pipe1.height1b:
                start()
                running = False

        def point(self):
            score_num = score_font.render(str(self.p_score), True, (255, 255, 255))
            screen.blit(score_num, (190, 50))

            if self.x >= pipe1.x and self.x <= pipe1.x+1:
                self.p_score += 1

            elif self.x >= pipe1.x1 and self.x <= pipe1.x1+1:
                self.p_score += 1

    flappy = Bird()


    class Pipe():
        def __init__(self):
            self.p1 = True
            self.p2 = False
            self.x = 300
            self.y = 0
            self.width = 50
            self.height = random.randint(50,350)
            self.heightb = HEIGHT-self.height-150
            self.yb = 600 - self.heightb
            self.x1 = 400
            self.y1 = 0
            self.width1 = 50
            self.height1 = random.randint(50,350)
            self.height1b = HEIGHT-self.height1-150
            self.yb1 = 600 - self.height1b



        def draw1(self):
            if self.p1 == True:
                pygame.draw.rect(screen, (0,0,0), (self.x,self.y,self.width,self.height))
                self.x -= 1
                if self.x <= 150:
                    self.p2 = True
                if self.x < 0-self.width:
                    self.x = 400
                    self.p1 = False


            if self.p2 == True:
                self.image2 = pygame.draw.rect(screen, (0, 0, 0), (self.x1, self.y1, self.width1, self.height1))
                self.x1 -= 1
                if self.x1 <= 150:
                    self.p1 = True
                if self.x1 < 0 - self.width1:
                    self.x1 = 400
                    self.p2 = False


        def draw2(self):
            if self.p1 == True:
                pygame.draw.rect(screen, (0,0,0), (self.x,self.yb,self.width,self.heightb))
                self.x -= 1
                if self.x <= 150:
                    self.p2 = True
                if self.x < 0-self.width:
                    self.x = 400
                    self.height = random.randint(50, 350)
                    self.heightb = HEIGHT-self.height-150
                    self.yb = 600-self.heightb
                    self.p1 = False

            if self.p2 == True:
                pygame.draw.rect(screen, (0, 0, 0), (self.x1, self.yb1, self.width1, self.height1b))
                self.x1 -= 1
                if self.x1 <= 150:
                    self.p1 = True
                if self.x1 < 0 - self.width1:
                    self.x1 = 400
                    self.height1 = random.randint(50, 350)
                    self.height1b = HEIGHT-self.height1-150
                    self.yb1 = 600-self.height1b
                    self.p2 = False

    pipe1 = Pipe()


    running = True

    while running:
        clock.tick(60)
        screen.fill((169,169,169))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flappy.up()
            if event.type == pygame.MOUSEBUTTONDOWN:
                flappy.up()



        flappy.draw()
        flappy.fall()
        pipe1.draw1()
        pipe1.draw2()
        flappy.hit()
        flappy.point()


        pygame.display.update()


start()
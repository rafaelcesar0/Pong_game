import pygame
from sys import exit

pygame.init()
pygame.font.init()
width = 1280
height = 720
display = pygame.display.set_mode((width, height))
fps = pygame.time.Clock()
music = pygame.mixer.Sound('Games\Mortal_Pong\\assets\music.ogg')
stop = 0
def OpenGame(jogador):
    # quad = pygame.Rect(50, 200, 500, 100) ?

    while True:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        display.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        if jogador == 1:
           Game.twoPlayer()
        elif jogador == 2:
           Game.RunGame()
           
        fps.tick(60)
        pygame.display.flip()

class MainGame:
    score_PL_1 = 0
    score_PL_2 = 0
    vel_player1 = 6
    vel_player2 = 6
    run = True
    player1 = pygame.Rect(10, 0, 20, 100)
    player2 = pygame.Rect(1250, 0, 20, 100)

    ball_dir_P1_x = 5
    ball_dir_P1_y = 5

    ball_power_p1_x = 0
    ball_power_p1_y = 0

    ball_power_p1_img = pygame.image.load('Games\Mortal_Pong\\assets\\ball.png')
    ball_power_p1 = ball_power_p1_img.get_rect()
    ball_shoot = + 1

    font = pygame.font.Font(None, 50)
    ball = pygame.Rect(600, 356, 10, 10)
    ball_dir_x = 5
    ball_dir_y = 5
    imagem = pygame.image.load('Games\Mortal_Pong\\assets\ossos.png')
    def RunGame(self):
        # music.play()
        Game.moveBall()
        Game.movePlayer2()
        Game.movePlayer1()

        display.fill('black')

        Game.plac_PL_1 = Game.font.render(str(Game.score_PL_1), True, "white")
        Game.plac_PL_2 = Game.font.render(str(Game.score_PL_2), True, "white")

        display.blit(Game.plac_PL_1, (500, 50))
        display.blit(Game.plac_PL_2, (800, 50))
        display.blit(Game.imagem,(0,0))

        pygame.draw.rect(display, "white", Game.player1)
        pygame.draw.rect(display, "white", Game.player2)
        pygame.draw.circle(display, "white", Game.ball.center, 20)
        Game.ActionPlyer1()

        # Game.ball_power_p1.x += 10

    def twoPlayer(self):
        self.RunGame()
        Game.player2.y = Game.ball.y - 50

    def ActionPlyer1(self):
        self.ball_power_p1.x = self.player1.x
        self.ball_power_p1.y = self.player1.y


        key = pygame.key.get_pressed()
        val = 0
        if key[pygame.K_SPACE]:
            Game.ball_power_p1_x = 5
            Game.ball_power_p1_y = 5


        self.ball_power_p1.x = + Game.ball_power_p1_x

        self.ball_power_p1.y = + Game.ball_power_p1_y

        # print(self.ball_power_p1.x)
        display.blit(self.ball_power_p1_img, (self.ball_power_p1.x, self.ball_power_p1.y))

        pygame.display.flip()

    def movePlayer1(self):
        self.presskey_play1()
        if self.player1.y <= 0:
            self.player1.y = 0
        if self.player1.y >= 620:
            self.player1.y = 620
        if self.player1.x <= 0:
            self.player1.x = 0
        if self.player1.x >= 420:
            self.player1.x = 420

    def movePlayer2(self):
        self.presskey_play2()
        if self.player2.y <= 0:
            self.player2.y = self.vel_player2
        if self.player2.y >= 620:
            self.player2.y = 620
        if self.player2.x <= 860:
            self.player2.x = 860
        if self.player2.x >= 1260:
            self.player2.x = 1260

    def presskey_play1(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.player1.y -= self.vel_player1
        if key[pygame.K_s]:
            self.player1.y += self.vel_player1
        if key[pygame.K_a]:
            self.player1.x -= self.vel_player1
        if key[pygame.K_d]:
            self.player1.x += self.vel_player1

    def presskey_play2(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.player2.y -= self.vel_player2
        if key[pygame.K_DOWN]:
            self.player2.y += self.vel_player2
        if key[pygame.K_LEFT]:
            self.player2.x -= self.vel_player2
        if key[pygame.K_RIGHT]:
            self.player2.x += self.vel_player2
    def moveBall(self):
        self.limiBall()
        self.colisionBall()
        if self.ball.x <= 0:
            self.score_PL_2 += 1
            self.ball.x = 585
            self.ball_dir_x *= -1
        elif self.ball.x >= 1280:
            self.ball.x = 585
            self.score_PL_1 += 1
            self.ball_dir_x *= -1

    def limiBall(self):
        # inverte a posição da Bola quando bater em cima ou em baixo
        if self.ball.y <= 0:
            self.ball_dir_y *= -1
            self.sondsBall()
        elif self.ball.y >= 720:
            self.ball_dir_y *= -1
            self.sondsBall()
        # incrementa a direção para o aixo XY
        self.ball.x += self.ball_dir_x
        self.ball.y += self.ball_dir_y

    def colisionBall(self):
        if self.player2.colliderect(self.ball):
            self.ball_dir_x *= -1
            self.sondsBall()
        if self.player1.colliderect(self.ball):
            self.ball_dir_x *= -1

            self.sondsBall()

    def sondsBall(self):
        hit = pygame.mixer.Sound("Games\Mortal_Pong\\assets\\ball_song2.wav")
        hit.play()

class MainMenu():
    font = pygame.font.Font(None, 50)

    def RunMenu(self):
        self.vefifiaEventoss()
        display.fill((0, 0, 0))
        self.draw_text(" PONG ", width / 2, height / 10)
        self.draw_text("1 jogador", width / 2, height / 3)
        self.draw_text("2 Jogador", width / 2, height / 2.5)
        self.draw_text(" Sair ", width / 2, height / 2.15)
        pygame.display.update()

    def vefifiaEventoss(self):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if width / 2 - 40 <= mouse_pos[0] <= width / 2 + 40 and height / 2.15 - 18 <= mouse_pos[
                1] <= height / 2.15 + 18:
                pygame.quit()
                exit()

            if width / 2 - 60 <= mouse_pos[0] <= width / 2 + 60 and height / 3 - 18 <= mouse_pos[1] <= height / 3 + 18:
                print("player 1")
                var = 1
                OpenGame(var)

            if width / 2 - 80 <= mouse_pos[0] <= width / 2 + 80 and height / 2.5 - 18 <= mouse_pos[1] <= height / 2.5 + 18:
                print("player 2")
                var = 2
                OpenGame(var)

    def draw_text(self, text, x, y):
        text_obj = self.font.render(text, True, "white")
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        display.blit(text_obj, text_rect)

Menu = MainMenu()
Game = MainGame()
rumingGame = True

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    Menu.RunMenu()
    pygame.display.flip()
    fps.tick(60)
from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, speed, x, y, sizex, sizey):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (sizex, sizey))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def left_update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
    def right_update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed

window = display.set_mode((700, 500))
window.fill((0, 200, 255))

clock = time.Clock()

left_racket = Player('racket.png', 5, 50, 200, 20, 80)
right_racket = Player('racket.png', 5, 650, 200, 20, 80)
ball = GameSprite('ball.png', 5, 300, 200, 40, 40)

speed_x = 5
speed_y = 5

font.init()
font1 = font.Font(None, 36)
lose1 = font1.render('Player 1 lose!', None, (255, 0, 0))
lose2 = font1.render('Player 2 lose!', None, (255, 0, 0))

finish = False
game = True
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    if finish == False:
        window.fill((0, 200, 255))
        left_racket.left_update()
        left_racket.reset()
        right_racket.right_update()
        right_racket.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(ball, left_racket) or sprite.collide_rect(ball, right_racket):
            if speed_x > 0:
                speed_x = randint(3, 5)
                speed_x *= -1
            else:
                speed_x = randint(3, 5)
        if ball.rect.y <= 0:
            speed_y *= -1
        if ball.rect.y >= 460:
            speed_y *= -1
        if ball.rect.x <= 0:
            window.blit(lose1, (250, 220))
            finish = True
        if ball.rect.x >= 700:
            window.blit(lose2, (250, 220))
            finish = True
            
    clock.tick(60)
    display.update()

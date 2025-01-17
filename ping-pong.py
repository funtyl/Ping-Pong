from pygame import *

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
        if keys[K_s] and self.rect.y < 440:
            self.rect.y += self.speed
    def right_update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed

window = display.set_mode((700, 500))
window.fill((0, 200, 255))

clock = time.Clock()

left_racket = Player('racket.png', 5, 50, 200, 20, 80)
right_racket = Player('racket.png', 5, 650, 200, 20, 80)
ball = GameSprite('ball.png', 5, 300, 200, 40, 40)

game = True
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((0, 200, 255))
    left_racket.left_update()
    left_racket.reset()
    right_racket.right_update()
    right_racket.reset()
    ball.reset()

    clock.tick(60)
    display.update()
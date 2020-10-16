import pygame
import random
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
    
    def update(self, pressed_key):
        if pressed_key[K_UP]:
            self.rect.move_ip(0,-1)
        elif pressed_key[K_DOWN]:
            self.rect.move_ip(0,1)
        elif pressed_key[K_LEFT]:
            self.rect.move_ip(-1,0)
        elif pressed_key[K_RIGHT]:
            self.rect.move_ip(1,0)
        
        if self.rect.left <0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <=0:
            self.rect.top =0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20,10))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center =(
                random.randint(SCREEN_WIDTH+20, SCREEN_WIDTH+100),
                random.randint(0,SCREEN_HEIGHT)
            )
        )
        self.speed = float(random.randint(1,4)/2)

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right <0:
            self.kill()




pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ADDENEMY = pygame.USEREVENT+1
pygame.time.set_timer(ADDENEMY, 250)

player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(player)
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # print(f"{event.key}")
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    
    pressed_key = pygame.key.get_pressed()
    player.update(pressed_key)
    enemies.update()


    screen.fill((0,0,0))
    surf = pygame.Surface((100,100))
    surf.fill((0,0,0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    pygame.display.flip()

pygame.quit()
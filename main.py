import pygame
import random
import time

# =====================
# Classes
# =====================

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = PLAYER_IMG1
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.centery = SCREEN_HEIGHT / 2

        # Shrink the hitboxes as they are very unforgiving
        self.rect.width = 40
        self.rect.height -= 8

        # Used to swap between animation images every set interval
        self.animation_frame = 0

        # Used to cancel the animation when standing still
        self.moving = False

    def update(self):
        # Manage animation
        if self.moving:
            self.animation_frame += 1
            if self.animation_frame % 30 < 15:
                self.image = PLAYER_IMG2
            else:
                self.image = PLAYER_IMG1
        else:
            self.animation_frame = 0
            self.image = PLAYER_IMG1


class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = ZOMBIE_IMG1
        self.rect = self.image.get_rect()
        self.rect.height -= 12

        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

        self.speed = random.randint(2, 5)
        self.animation_frame = 0

    def update(self):
        self.rect.x -= self.speed

        # Kill zombie when it leaves screen
        if self.rect.right < 0:
            self.kill()

        # Manage animation
        self.animation_frame += 1
        if self.animation_frame % 60 < 30:
            self.image = ZOMBIE_IMG2
        else:
            self.image = ZOMBIE_IMG1


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, fire_mode=False):
        super().__init__()

        # Use fire bullet image if in fire mode
        if fire_mode:
            self.image = FIRE_BULLET_IMG
        else:
            self.image = BULLET_IMG

        self.rect = self.image.get_rect()

        # Offset to place over the player's gun
        self.rect.x = x + 52
        self.rect.y = y + 28

    def update(self):
        self.rect.x += self.rect.width
        if self.rect.x > SCREEN_WIDTH:
            self.kill()


class FloatingText(pygame.sprite.Sprite):
    def __init__(self, text, x, y, color=(255, 0, 0)):
        super().__init__()
        self.image = font.render(text, True, color)
        self.rect = self.image.get_rect(center=(x, y))
        self.timer = FPS // 2  # lasts 0.5 seconds

    def update(self):
        self.rect.y -= 1  # float upwards
        self.timer -= 1
        if self.timer <= 0:
            self.kill()


# =====================
# Functions
# =====================

def draw_score():
    score_text = font.render(str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


def draw():
    # Apply random shake offset
    offset_x = random.randint(-shake_amount, shake_amount) if shake_timer > 0 else 0
    offset_y = random.randint(-shake_amount, shake_amount) if shake_timer > 0 else 0

    screen.blit(BACKGROUND_IMG, (offset_x, offset_y))
    all_sprites.draw(screen)
    floating_texts.draw(screen)
    draw_score()

    # Darken screen during slow-mo
    if slowmo:
        dark_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        dark_surface.set_alpha(120)
        dark_surface.fill((0, 0, 0))
        screen.blit(dark_surface, (0, 0))


def get_input():
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Shooting
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullet = Bullet(player.rect.x, player.rect.y, fire_mode=fire_mode)
                all_sprites.add(bullet)
                bullets.add(bullet)
                SHOOT_SOUND.play()

    # Movement
    player.moving = False
    keystate = pygame.key.get_pressed()

    if keystate[pygame.K_w]:
        player.rect.y -= 9
        player.moving = True
    if keystate[pygame.K_s]:
        player.rect.y += 9
        player.moving = True
    if keystate[pygame.K_a]:
        player.rect.x -= 9
        player.moving = True
    if keystate[pygame.K_d]:
        player.rect.x += 9
        player.moving = True

    # Clip player to screen
    player.rect.x = max(player.rect.x, 0)
    player.rect.y = max(player.rect.y, 0)
    player.rect.right = min(player.rect.right, SCREEN_WIDTH)
    player.rect.bottom = min(player.rect.bottom, SCREEN_HEIGHT)


def update(tick):
    global score, running, fire_mode, fire_mode_end
    global shake_timer, shake_amount
    global slowmo, slowmo_end

    all_sprites.update()
    floating_texts.update()

    # Fire mode logic (every 20 seconds)
    if tick % (20 * FPS) == 0 and not fire_mode:
        fire_mode = True
        fire_mode_end = tick + (5 * FPS)

    if fire_mode and tick >= fire_mode_end:
        fire_mode = False

    # Bullet-zombie collisions
    collisions = pygame.sprite.groupcollide(bullets, zombies, True, True)

    for bullet, hit_zombies in collisions.items():
        for z in hit_zombies:
            zombie_head_line = z.rect.y + (z.rect.height // 3)

            if bullet.rect.y <= zombie_head_line:
                score += 2
                floating_texts.add(
                    FloatingText("HEADSHOT!", z.rect.centerx, z.rect.centery, (255, 220, 0))
                )
                HEADSHOT_SOUND.play()
                shake_amount = 6
                shake_timer = 6
            else:
                score += 1

    # Zombie hits player → slow-mo
    hit = pygame.sprite.spritecollide(player, zombies, False)
    if hit and not slowmo:
        slowmo = True
        slowmo_end = tick + SLOWMO_DURATION

    # End slow-mo and quit
    if slowmo and tick >= slowmo_end:
        running = False
        print(f"You got {score} score!")
        print(f"You survived for {tick // 60} seconds!")
        time.sleep(2)

    # Spawn zombies
    if tick % max(2, (50 - tick // 80)) == 0:
        zombie = Zombie()
        all_sprites.add(zombie)
        zombies.add(zombie)

    # Screen shake decay
    if shake_timer > 0:
        shake_timer -= 1
        if shake_timer == 0:
            shake_amount = 0


def main():
    global running
    tick = 0

    while running:
        tick += 1
        draw()
        pygame.display.flip()

        if slowmo:
            clock.tick(FPS // 4)
        else:
            clock.tick(FPS)

        get_input()
        update(tick)


# =====================
# Globals / Setup
# =====================

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
FPS = 60

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Outbreak")
clock = pygame.time.Clock()

slowmo = False
slowmo_end = 0
SLOWMO_DURATION = FPS * 1

floating_texts = pygame.sprite.Group()
shake_amount = 0
shake_timer = 0

# Font
font = pygame.font.Font(None, 128)

# Assets
BACKGROUND_IMG = pygame.transform.scale(
    pygame.image.load("imgs/background.jpg"),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

PLAYER_IMG1 = pygame.image.load("imgs/player1.png")
PLAYER_IMG2 = pygame.image.load("imgs/player2.png")
ZOMBIE_IMG1 = pygame.image.load("imgs/zombie1.png")
ZOMBIE_IMG2 = pygame.image.load("imgs/zombie2.png")
BULLET_IMG = pygame.image.load("imgs/bullet.png")
FIRE_BULLET_IMG = pygame.image.load("imgs/fire_bullet.png")

# Sounds
SHOOT_SOUND = pygame.mixer.Sound("audio/shoot.wav")
HEADSHOT_SOUND = pygame.mixer.Sound("audio/headshot.wav")
MUSIC_SOUND = pygame.mixer.Sound("audio/music.wav")

MUSIC_SOUND.play(-1)

# Game state
running = True
score = 0
fire_mode = False
fire_mode_end = 0

all_sprites = pygame.sprite.Group()
zombies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

main()
pygame.quit()

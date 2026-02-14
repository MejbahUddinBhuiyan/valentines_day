import pygame
import random
import math
import sys

# ---------- CONFIG ----------
WIDTH, HEIGHT = 900, 600
FPS = 60
HEART_COUNT = 30

# ---------- INIT ----------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("💖 Happy Valentine's Day 💖")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Segoe Script", 48, bold=True)
small_font = pygame.font.SysFont("Arial", 22)

# ---------- COLORS ----------
BG_COLOR = (15, 8, 25)
PINKS = [
    (255, 105, 180),
    (255, 20, 147),
    (255, 182, 193),
    (255, 0, 102)
]

# ---------- HEART CLASS ----------
class Heart:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(HEIGHT, HEIGHT + 500)
        self.size = random.randint(12, 25)
        self.speed = random.uniform(0.8, 2)
        self.color = random.choice(PINKS)
        self.phase = random.uniform(0, 2 * math.pi)
        self.sway = random.uniform(0.5, 1.5)  # horizontal sway

    def update(self):
        self.y -= self.speed
        self.x += math.sin(self.phase) * self.sway
        self.phase += 0.05
        if self.y < -50:
            self.y = HEIGHT + random.randint(50, 300)
            self.x = random.randint(50, WIDTH - 50)

    def draw(self, surface):
        # Real heart shape using parametric equations
        scale = self.size / 10
        points = []
        for t in range(0, 360, 2):
            rad = math.radians(t)
            x = 16 * math.sin(rad) ** 3
            y = 13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad)
            points.append((self.x + x * scale, self.y - y * scale))
        pygame.draw.polygon(surface, self.color, points)

# ---------- CREATE HEARTS ----------
hearts = [Heart() for _ in range(HEART_COUNT)]

# ---------- FADE-IN TEXT ----------
alpha = 0
text_surface = font.render("Happy Valentine's Day 💕", True, (255, 182, 193))
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

sub_text = small_font.render(
    "Love is in the air 💌", True, (255, 182, 193)
)
sub_rect = sub_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))

# ---------- MAIN LOOP ----------
running = True
while running:
    clock.tick(FPS)
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw hearts
    for heart in hearts:
        heart.update()
        heart.draw(screen)

    # Fade-in effect for text
    if alpha < 255:
        alpha += 2
    text_surface.set_alpha(alpha)
    sub_text.set_alpha(alpha)

    screen.blit(text_surface, text_rect)
    screen.blit(sub_text, sub_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()

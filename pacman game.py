import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Pac-Man properties
PACMAN_RADIUS = 15
PACMAN_SPEED = 5

# Ghost properties
GHOST_RADIUS = 15
GHOST_SPEED = 2

# Food properties
FOOD_RADIUS = 5
NUM_FOOD = 20

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Pac-Man starting position
pacman_x = SCREEN_WIDTH // 2
pacman_y = SCREEN_HEIGHT // 2

# Ghost starting position
ghost_x = random.randint(0, SCREEN_WIDTH)
ghost_y = random.randint(0, SCREEN_HEIGHT)

# Generate random food positions
foods = [
    (random.randint(20, SCREEN_WIDTH - 20), random.randint(20, SCREEN_HEIGHT - 20))
    for _ in range(NUM_FOOD)
]

# Score
score = 0

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pacman_y -= PACMAN_SPEED
    if keys[pygame.K_DOWN]:
        pacman_y += PACMAN_SPEED
    if keys[pygame.K_LEFT]:
        pacman_x -= PACMAN_SPEED
    if keys[pygame.K_RIGHT]:
        pacman_x += PACMAN_SPEED

    # Prevent Pac-Man from going off-screen
    pacman_x = max(PACMAN_RADIUS, min(SCREEN_WIDTH - PACMAN_RADIUS, pacman_x))
    pacman_y = max(PACMAN_RADIUS, min(SCREEN_HEIGHT - PACMAN_RADIUS, pacman_y))

    # Ghost movement (random direction)
    ghost_x += random.choice([-GHOST_SPEED, GHOST_SPEED])
    ghost_y += random.choice([-GHOST_SPEED, GHOST_SPEED])

    # Prevent ghost from going off-screen
    ghost_x = max(GHOST_RADIUS, min(SCREEN_WIDTH - GHOST_RADIUS, ghost_x))
    ghost_y = max(GHOST_RADIUS, min(SCREEN_HEIGHT - GHOST_RADIUS, ghost_y))

    # Check for collision with food
    foods = [
        food for food in foods
        if not (pacman_x - FOOD_RADIUS < food[0] < pacman_x + FOOD_RADIUS and
                pacman_y - FOOD_RADIUS < food[1] < pacman_y + FOOD_RADIUS)
    ]
    score = NUM_FOOD - len(foods)

    # Check for collision with ghost
    if (
        (pacman_x - ghost_x) ** 2 + (pacman_y - ghost_y) ** 2
    ) ** 0.5 < PACMAN_RADIUS + GHOST_RADIUS:
        print("Game Over! Final Score:", score)
        pygame.quit()
        sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw Pac-Man
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), PACMAN_RADIUS)

    # Draw ghost
    pygame.draw.circle(screen, RED, (ghost_x, ghost_y), GHOST_RADIUS)

    # Draw food
    for food_x, food_y in foods:
        pygame.draw.circle(screen, WHITE, (food_x, food_y), FOOD_RADIUS)

    # Draw the score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)

# Quit the game
pygame.quit()

import pygame
import random
import sys
from user_model import get_or_create_user, save_score

pygame.init()
pygame.mixer.init()

# Звуки
eat_sound = pygame.mixer.Sound("Sounds/eat.wav")
lose_sound = pygame.mixer.Sound("Sounds/lose.wav")

# Пользователь и уровень
username = input("Enter your username: ")
user_id, saved_level = get_or_create_user(username)
print(f"Welcome, {username}! Your saved level: {saved_level}")

# Настройки экрана и сетки
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
HEADER_HEIGHT_CELLS = 4

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)
DARK_GRAY = (50, 50, 50)

# Инициализация
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (1, 0)
snake_speed = 5 + saved_level
score = 0
level = saved_level
foods_to_level_up = 5  # 🔥 теперь каждые 5 яблок — уровень

walls = []
paused = False

def generate_random_walls():
    global walls
    walls = []
    wall_count = 24
    min_spacing = 2
    attempts_per_wall = 100
    placed_walls = 0

    while placed_walls < wall_count:
        for _ in range(attempts_per_wall):
            wall_length = random.randint(2, 5)
            wall_direction = random.choice(['horizontal', 'vertical'])
            wall_start = (
                random.randint(1, GRID_WIDTH - 6),
                random.randint(HEADER_HEIGHT_CELLS + 1, GRID_HEIGHT - 6)
            )

            if wall_direction == 'horizontal':
                wall_positions = [(wall_start[0] + i, wall_start[1]) for i in range(wall_length)]
            else:
                wall_positions = [(wall_start[0], wall_start[1] + i) for i in range(wall_length)]

            if any(pos[0] < 0 or pos[0] >= GRID_WIDTH or pos[1] >= GRID_HEIGHT for pos in wall_positions):
                continue

            too_close = False
            for pos in wall_positions:
                for dx in range(-min_spacing, min_spacing + 1):
                    for dy in range(-min_spacing, min_spacing + 1):
                        neighbor = (pos[0] + dx, pos[1] + dy)
                        if neighbor in walls or neighbor in snake or neighbor[1] < HEADER_HEIGHT_CELLS:
                            too_close = True
                            break
                    if too_close:
                        break
                if too_close:
                    break

            if not too_close:
                walls.extend(wall_positions)
                placed_walls += 1
                break

def generate_food():
    while True:
        pos = (
            random.randint(0, GRID_WIDTH - 1),
            random.randint(HEADER_HEIGHT_CELLS, GRID_HEIGHT - 1)
        )
        if pos not in snake and pos not in walls:
            return pos

generate_random_walls()
food = generate_food()

def draw_snake():
    for i, segment in enumerate(snake):
        color = WHITE if i == 0 else GREEN
        pygame.draw.rect(screen, color, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_walls():
    for wall in walls:
        pygame.draw.rect(screen, GRAY, (wall[0] * GRID_SIZE, wall[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_header():
    pygame.draw.rect(screen, DARK_GRAY, (0, 0, SCREEN_WIDTH, HEADER_HEIGHT_CELLS * GRID_SIZE))
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (SCREEN_WIDTH - level_text.get_width() - 10, 10))

def check_wall_collisions():
    return snake[0] in walls

def check_collisions():
    if snake[0] in snake[1:]:
        return True
    if (snake[0][0] < 0 or snake[0][0] >= GRID_WIDTH or
        snake[0][1] < HEADER_HEIGHT_CELLS or snake[0][1] >= GRID_HEIGHT):
        return True
    if check_wall_collisions():
        return True
    return False

def handle_input():
    global snake_direction, paused
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction[1] == 0:
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction[1] == 0:
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction[0] == 0:
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction[0] == 0:
                snake_direction = (1, 0)
            elif event.key == pygame.K_p:
                paused = not paused
                if paused:
                    save_score(user_id, score, level)
                    print("⏸ Game paused & saved.")

def update():
    global food, snake, snake_speed, score, level
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)

    if check_collisions():
        save_score(user_id, score, level)
        lose_sound.play()
        return True

    if snake[0] == food:
        eat_sound.play()
        score += 1
        if score % foods_to_level_up == 0:
            level += 1
            snake_speed += 1
        food = generate_food()
    else:
        snake.pop()

    return False

def display_loss_message():
    font = pygame.font.Font(None, 60)
    text = font.render("You've lost!", True, RED)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2,
                       SCREEN_HEIGHT // 2 - text.get_height() // 2))

def wait_for_keypress():
    font = pygame.font.Font(None, 48)
    message = font.render("Press any key to start", True, WHITE)
    screen.blit(message, (SCREEN_WIDTH // 2 - message.get_width() // 2,
                          SCREEN_HEIGHT // 2 - message.get_height() // 2))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

clock = pygame.time.Clock()
game_over = False

# Начальная пауза
screen.fill(BLACK)
draw_header()
draw_snake()
draw_food()
draw_walls()
wait_for_keypress()

while not game_over:
    handle_input()
    if paused:
        continue
    game_over = update()

    screen.fill(BLACK)
    draw_header()
    draw_snake()
    draw_food()
    draw_walls()

    if game_over:
        display_loss_message()
        pygame.display.update()
        pygame.time.delay(2050)  
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(snake_speed)

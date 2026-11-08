# pip install pygame

import pygame
import random

pygame.init()

CELL = 20
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (220, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont(None, 30)


def random_food(snake):
    while True:
        food = (
            random.randrange(0, WIDTH // CELL) * CELL,
            random.randrange(0, HEIGHT // CELL) * CELL,
        )
        if food not in snake:
            return food


def draw_text(text):
    label = font.render(text, True, WHITE)
    screen.blit(label, (10, 10))


def game_over():
    screen.fill(BLACK)
    draw_text("Game Over! Press R to restart, Q to quit")
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                    return
                if event.key == pygame.K_q:
                    pygame.quit()
                    return


def main():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (CELL, 0)
    food = random_food(snake)
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, CELL):
                    direction = (0, -CELL)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL):
                    direction = (0, CELL)
                elif event.key == pygame.K_LEFT and direction != (CELL, 0):
                    direction = (-CELL, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                    direction = (CELL, 0)

        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])

        # Wall collision
        if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
            game_over()
            return

        # Self collision
        if new_head in snake:
            game_over()
            return

        snake.insert(0, new_head)

        # Eat food
        if new_head == food:
            score += 1
            food = random_food(snake)
        else:
            snake.pop()

        screen.fill(BLACK)

        for part in snake:
            pygame.draw.rect(screen, GREEN, (*part, CELL, CELL))

        pygame.draw.rect(screen, RED, (*food, CELL, CELL))
        draw_text(f"Score: {score}")

        pygame.display.update()
        clock.tick(10)

    pygame.quit()


main()

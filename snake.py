import random

import pygame

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

BLOCK_SIZE = 32
NUM_WIDTH_BLOCKS = 20
NUM_HEIGHT_BLOCKS = 20
WINDOW_WIDTH = BLOCK_SIZE * NUM_WIDTH_BLOCKS
WINDOW_HEIGHT = BLOCK_SIZE * NUM_HEIGHT_BLOCKS

snake_direction = RIGHT
snake_pixel_locations = [(0, 0)]

fruit_block_location = (random.randrange(0, NUM_WIDTH_BLOCKS),
                        random.randrange(0, NUM_HEIGHT_BLOCKS))

pygame.init()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake_direction = UP
            elif event.key == pygame.K_s:
                snake_direction = DOWN
            elif event.key == pygame.K_a:
                snake_direction = LEFT
            elif event.key == pygame.K_d:
                snake_direction = RIGHT

    screen.fill("black")

    if snake_direction == LEFT:
        snake_pixel_locations.append(
            (snake_pixel_locations[-1][0] - BLOCK_SIZE, snake_pixel_locations[-1][1]))
    elif snake_direction == RIGHT:
        snake_pixel_locations.append(
            (snake_pixel_locations[-1][0] + BLOCK_SIZE, snake_pixel_locations[-1][1]))
    elif snake_direction == UP:
        snake_pixel_locations.append(
            (snake_pixel_locations[-1][0], snake_pixel_locations[-1][1] - BLOCK_SIZE))
    elif snake_direction == DOWN:
        snake_pixel_locations.append(
            (snake_pixel_locations[-1][0], snake_pixel_locations[-1][1] + BLOCK_SIZE))

    fruit_pixel_location = (
        fruit_block_location[0] * BLOCK_SIZE, fruit_block_location[1] * BLOCK_SIZE)

    if snake_pixel_locations[-1] != fruit_pixel_location:
        snake_pixel_locations.pop(0)
    else:
        fruit_block_location = (random.randrange(0, NUM_WIDTH_BLOCKS),
                                random.randrange(0, NUM_HEIGHT_BLOCKS))

    if snake_pixel_locations[-1][0] < 0 or snake_pixel_locations[-1][1] < 0 or snake_pixel_locations[-1][0] >= WINDOW_WIDTH or snake_pixel_locations[-1][1] >= WINDOW_HEIGHT:
        snake_pixel_locations = [(0, 0)]
        snake_direction = RIGHT
        fruit_block_location = (random.randrange(0, NUM_WIDTH_BLOCKS),
                                random.randrange(0, NUM_HEIGHT_BLOCKS))

    pygame.draw.rect(
        screen, "red", (*fruit_pixel_location, BLOCK_SIZE, BLOCK_SIZE))

    for x, y in snake_pixel_locations:
        pygame.draw.rect(screen, "white", (x, y, BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.flip()

    clock.tick(5)

pygame.quit()

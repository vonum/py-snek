import pygame

import movement
from collision import collision, snake_collision, wall_collision

from snek import Snek, SNEK_COLOR, SNEK_HEIGHT, SNEK_WIDTH
from green_food import GreenFood, FOOD_COLOR, FOOD_HEIGHT, FOOD_WIDTH

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

clock = pygame.time.Clock()

snek = Snek(50, 50)
foodsiez = GreenFood()

direction = movement.NONE

while not done:

  # event logic
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

    # movement
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        done = True
      if event.key == pygame.K_DOWN and direction != movement.UP:
        direction = movement.DOWN
      if event.key == pygame.K_UP and direction != movement.DOWN:
        direction = movement.UP
      if event.key == pygame.K_LEFT and direction != movement.RIGHT:
        direction = movement.LEFT
      if event.key == pygame.K_RIGHT and direction != movement.LEFT:
        direction = movement.RIGHT

  # game logic
  if (wall_collision(snek.parts[0], SNEK_HEIGHT, SNEK_WIDTH,
                     SCREEN_HEIGHT, SCREEN_WIDTH)):
    break

  if (snake_collision(snek, SNEK_HEIGHT, SNEK_WIDTH)):
    break

  shit = movement.move(direction)
  eaten = False

  if (collision(snek.parts[0], SNEK_HEIGHT, SNEK_WIDTH,
                foodsiez, FOOD_HEIGHT, FOOD_WIDTH)):
    foodsiez = GreenFood()
    eaten = True


  snek.move(shit[0], shit[1], eaten)

  # rendering
  screen.fill((0, 0, 0))

  # snek
  for snek_part in snek.parts:
    pygame.draw.rect(
      screen,
      SNEK_COLOR,
      pygame.Rect(snek_part.x, snek_part.y, SNEK_WIDTH, SNEK_HEIGHT)
  )
  # foodsiez
  pygame.draw.rect(
    screen,
    FOOD_COLOR,
    pygame.Rect(foodsiez.x, foodsiez.y, FOOD_WIDTH, FOOD_HEIGHT)
  )

  pygame.display.flip()
  clock.tick(10)

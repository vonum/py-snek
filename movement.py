STEP_LENGTH = 15

NONE = -1
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

def move(direction):
  x = 0
  y = 0

  if direction == UP:
    y -= STEP_LENGTH
  elif direction == DOWN:
    y += STEP_LENGTH
  elif direction == LEFT:
    x -= STEP_LENGTH
  elif direction == RIGHT:
    x += STEP_LENGTH

  return (x, y)

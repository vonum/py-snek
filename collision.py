def collision(obj1, obj1_height, obj1_width,
              obj2, obj2_height, obj2_width):
  if obj1.x + obj1_width <= obj2.x:
    return False
  elif obj1.y + obj1_height <= obj2.y:
    return False
  elif obj1.y >= obj2.y + obj2_height:
    return False
  elif obj1.x >= obj2.x + obj2_width:
    return False

  return True

def snake_collision(snek, SNEK_HEIGHT, SNEK_WIDTH):
  snek_head = snek.parts[0]
  snek_length = len(snek.parts)

  for i in range(1, snek_length - 1):
    snek_part = snek.parts[i]
    collided = collision(snek_head, SNEK_HEIGHT, SNEK_WIDTH,
                         snek_part, SNEK_HEIGHT, SNEK_WIDTH)
    if collided:
      return True

  return False

def wall_collision(snek_head, SNEK_HEIGHT, SNEK_WIDTH,
                   SCREEN_HEIGHT, SCREEN_WIDTH):
  if snek_head.x < 0:
    return True
  elif snek_head.x + SNEK_WIDTH > SCREEN_WIDTH:
    return True
  elif snek_head.y < 0:
    return True
  elif snek_head.y + SNEK_HEIGHT > SCREEN_HEIGHT:
    return True

  return False

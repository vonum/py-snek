from snek_part import SnekPart

SNEK_COLOR = (128, 0, 128)
SNEK_HEIGHT = 15
SNEK_WIDTH = 15

class Snek:
  def __init__(self, x, y):
    self.parts = [ SnekPart(x, y) ]

  def move(self, x, y, eaten):
    parts = self.parts
    parts_length = len(parts)

    if eaten:
      self.grow()

    for i in range(parts_length - 1, 0, -1):
      parts[i].x = parts[i-1].x
      parts[i].y = parts[i-1].y

    parts[0].x += x
    parts[0].y += y

  def grow(self):
    parts = self.parts
    last_part = parts[-1]
    parts.append(SnekPart(last_part.x, last_part.y))

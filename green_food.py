import random

FOOD_HEIGHT = 10
FOOD_WIDTH = 10
FOOD_COLOR = (0, 255, 0)

class GreenFood:
  def __init__(self):
    self.x = random.randint(0, 800 - FOOD_WIDTH)
    self.y = random.randint(0, 600 - FOOD_HEIGHT)

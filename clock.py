import clock, sys, pygame
from random import randint

#initializing pygame display and setting size
pygame.display.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])

# define First Players time, lives, and starting position
Class Player1:
  def __init__(self, time, lives, position):
  self.t = time
  self.l = lives
  self.p = position

Player1 = P1
P1 = (60,3,defense)

Class Player2:
   def __init__(self, time, lives, position):
      self.t = time
      self.l = lives
      self.p = position
Player2 = P2
P2 = (60,3,offense)


offense, defense = defense, offense

# Event randomly selecting who goes first

for event in pygame.event.get():
  if event.type == pygame.QUIT:
    sys.exit()

# Event starting the game after Offensive player decided

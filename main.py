from board import Board
from player import Player
from game import Game
p1=Player(input("enter your name"),'o')
p2=Player(input("enter your name"),'x')
g=Game(p1,p2)
g.play()
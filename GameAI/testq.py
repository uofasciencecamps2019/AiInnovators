from tic_tac_toe.Board import Board, GameResult, CROSS, NAUGHT, EMPTY
from util import print_board, play_game, battle
from tic_tac_toe.RandomPlayer import RandomPlayer
from tic_tac_toe.MinMaxAgent import MinMaxAgent
from tic_tac_toe.RndMinMaxAgent import RndMinMaxAgent
from tic_tac_toe.TabularQPlayer import TQPlayer
from tic_tac_toe.SimpleNNQPlayer import NNQPlayer
from tic_tac_toe.TFSessionManager import TFSessionManager
import matplotlib.pyplot as plt
import tensorflow as tf
import random

board = Board()
#tf.reset_default_graph()

player1 = RandomPlayer()

player2 = RandomPlayer()

p1_wins = []
p1count = 0
p2_wins = []
p2count = 0
draws = []
drawcount = 0
count = []
num_battles = 100
games_per_battle = 10
 
TFSessionManager.set_session(tf.Session())
TFSessionManager.get_session().run(tf.global_variables_initializer())


for i in range(num_battles):
    p1win, p2win, draw = battle(player1, player2, games_per_battle, True)
    p1_wins.append(p1win)
    p1count+=p1win
    p2_wins.append(p2win)
    p2count+=p2win
    draws.append(draw)
    drawcount+=draw
    count.append(i*games_per_battle)
#TFSessionManager.set_session(None)
p = plt.plot(count, draws, 'r-', count, p1_wins, 'g-', count, p2_wins, 'b-')
print("p1 wins = " + str(p1count/(num_battles*games_per_battle)*100) +"% (green)")
print("p2 wins = " + str(p2count/(num_battles*games_per_battle)*100) +"% (blue)")
print("ties = " + str(drawcount/(num_battles*games_per_battle)*100) +"% (red)")

plt.show()

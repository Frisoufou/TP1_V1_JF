#!/usr/bin/env python3
"""
Quoridor agents.
Copyright (C) 2013, <<<<<<<<<<< YOUR NAMES HERE >>>>>>>>>>>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 2 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see <http://www.gnu.org/licenses/>.

"""

from quoridor import *
import NotAllowedError as exceptions
import heuristic_state as hs
import minimax
import log as log
import math
from minimax import heuristic

def manhattanDistance(x1, y1, x2, y2):
    "Returns the Manhattan distance between points xy1 and xy2"
    return abs( x2 - x1 ) + abs( y2 - y1 )

def possible_moves(player_curr_position, expected_move):

    if (expected_move == 'up' or expected_move == 'down' or expected_move == 'left' or expected_move == 'right'):

        move = {'up':('P', player_curr_position[0] - 1, player_curr_position[1]),
            'down':('P', player_curr_position[0] + 1, player_curr_position[1]),
            'left':('P', player_curr_position[0], player_curr_position[1] - 1),
            'right':('P', player_curr_position[0], player_curr_position[1] + 1)}

        return move[expected_move]

    else:
        raise ValueError('Expected move in possible_moves input function was wrong')

    

def wall_move_choice(board, player): ##### Wall function from greedy_player #### TO MODIFY

        # opponent position
        oppo_y, oppo_x = board.pawns[1-player]
        # opponent goal
        oppo_goal_y = board.goals[1-player]
        # set of legal wall moves
        wall_actions = board.get_legal_wall_moves(player)

        # find valid walls in front of opponent
        candidate_walls = []
        if oppo_goal_y < oppo_y:
            print("opponent moving north")
            for wall_action in wall_actions:
                wall_dir, wall_y, wall_x = wall_action
                if wall_dir == 'WH' and wall_y == oppo_y - 1 and wall_x in (oppo_x, oppo_x - 1):
                    candidate_walls.append(wall_action)
        else:
            print("opponent moving south")
            for wall_action in wall_actions:
                wall_dir, wall_y, wall_x = wall_action
                if wall_dir == 'WH' and wall_y == oppo_y and wall_x in (oppo_x, oppo_x - 1):
                    candidate_walls.append(wall_action)
        print(f"candidate walls: {candidate_walls}")

        if len(candidate_walls) > 0:
            choice = random.choice(candidate_walls)
            print(f"placing a wall: {choice}")
            return choice
        else:
            return "minimax"


class MyAgent(Agent):

    """My Quoridor agent."""
    def __init__(self):

        self._heuristic = hs.heuristic()

        self._game_state = []
        self._opponent_previous_moves = []
        self._player_previous_moves = []
        
        #### Using decorator syntax for getter/setter of each global variable ####
        @property
        def heuristic(self):
            return self._heuristic

        @heuristic.setter
        def heuristic(self, value):
            self._heuristic = value

        @property
        def game_state(self):
            return self._game_state

        @game_state.setter
        def game_state(self, value):
            self._game_state = value

        @property
        def opponent_previous_moves(self):
            return self._opponent_previous_moves

        @opponent_previous_moves.setter
        def opponent_previous_moves(self, value):
            self._opponent_previous_moves.append(value)

        @property
        def player_previous_moves(self):
            return self._player_previous_moves

        @player_previous_moves.setter
        def player_previous_moves(self, value):
            self._player_previous_moves.append(value)

    def next_actions(self, state):

        """
        Function that returns a actions to obtain a certain state.  
        Add Heuristic
        """
        board, player = state # Get board and player with regards to a certain state
        player_to_move = (player + 1) % 2
        moves = board.get_legal_pawn_moves(player) # From given function with TP2 documents
        

        for move in moves:

            test_board = board.clone() # Get shallow copy of current board
            test_board.play_action(move,player) # Changing test board with given move to a player
            result_state = (test_board, player_to_move) # Obtain resuling game state

            yield(move, result_state)

    def bool_minimax(self, step, board, depth, time_left):
        """
        Function that returns True is minimax search stopped (e.g if board is finished)
        """

        if time_left < 20 :

            return depth >= 1 or board.is_finished()

        # If begining of the game or lower than 3 minutes
        if step <= 6 or time_left < 180 :

            return depth >= 2 or board.is_finished()

        return depth >= 3 or board.is_finished()

        #board, player = state
        #if board.is_finished() or depth == 2:
        ##    return True
        #else:
        #    return False

    def player_score_heuristic_1(self, board, player, play):
        """
        Function that evaluates a current player's score according to a given game state
        """

        # TO BE IMPORTED IN HEURISTIC IN MINIMAX.PY

        #### Version plus détaillée #### TO MODIFY
        #board, player = state

        #minStepsMe = board.min_steps_before_victory(self.player)
        #minStepsHim = board.min_steps_before_victory((self.player+1)%2)
        
        #diffMinSteps =  minStepsHim - minStepsMe

        #maxPath = 30

        #score  = 1*diffMinSteps/maxPath 

        #score += 0.1 * ((board.nb_walls[self.player]/10) - (board.nb_walls[(self.player+1)%2]/10))

        #if board.nb_walls[self.player] == 0 and minStepsMe < minStepsHim:
        #    score -= 1
        #if board.nb_walls[(self.player+1)%2] == 0 and minStepsMe > minStepsHim:
        #    score += 1

        #if board.is_finished() :
#
        #    if player == self.player : score -= 9000
         #   else : score += 9000

        #return (int) (score*10000)
        

    def play(self, percepts, player, step, time_left):
        """
        This function is used to play a move according
        to the percepts, player and time left provided as input.
        It must return an action representing the move the player
        will perform.
        :param percepts: dictionary representing the current board
            in a form that can be fed to `dict_to_board()` in quoridor.py.
        :param player: the player to control in this step (0 or 1)
        :param step: the current step number, starting from 1
        :param time_left: a float giving the number of seconds left from the time
            credit. If the game is not time-limited, time_left is None.
        :return: an action
          eg: ('P', 5, 2) to move your pawn to cell (5,2)
          eg: ('WH', 5, 2) to put a horizontal wall on corridor (5,2)
          for more details, see `Board.get_actions()` in quoridor.py
        """
        print("percept:", percepts)
        print("player:", player)
        print("step:", step)
        print("time left:", time_left if time_left else '+inf')

        #log_test = log.logfile("testing_log")
        #log_test.info("Game started")

        # TODO: implement your agent and return an action for the current step.

        player_curr_position = percepts['pawns'][player]
        self.player = player
        board = dict_to_board(percepts)
        state = (board, player)

        # Printing some game informations
        print("test player 0 : " + str(board.nb_walls[0]))
        print("test player 1 : " + str(board.nb_walls[1]))
        print("Time left : " + str(time_left))
        
        # Getting information about current game state
        dict_heuristic = {}
        player1_walls = board.nb_walls[0]
        player2_walls = board.nb_walls[1]
        time_left = time_left

        # Getting manhattan distance between current my_player position and goal
        (x_init, y_init) = board.get_shortest_path(self.player)[0]
        (x_goal, y_goal) = board.get_shortest_path(self.player)[-1]
        distance_my_player = manhattanDistance(x_init, y_init, x_goal, y_goal)

        # Getting manhattan distance between current player position and goal
        (x_init, y_init) = board.get_shortest_path(1 - self.player)[0]
        (x_goal, y_goal) = board.get_shortest_path(1 - self.player)[-1]
        distance_player = manhattanDistance(x_init, y_init, x_goal, y_goal)
        
        # Creating current game state dictionnary for heuristic_state.py class input
        dict_heuristic["Player1_shortest_path"] =  distance_my_player
        dict_heuristic["Player2_shortest_path"] = distance_player
        dict_heuristic["Step"] = step
        dict_heuristic["time"] = time_left
        dict_heuristic["Player1_walls"] = player1_walls
        dict_heuristic["Player2_walls"] = player2_walls

        shortest_path_player = board.get_shortest_path(player)
        if (len(shortest_path_player) == 1):

            if player == 0:
                
                action = possible_moves(player_curr_position, 'down')
                if (board.is_action_valid(action, player)):
                    print("win possible")
                    print(action)
                    return action
                else:
                    return minimax.search(board, player, dict_heuristic, time_left,  step, heuristic)

            elif player == 1:

                action =  possible_moves(player_curr_position, 'up')
                if (board.is_action_valid(action, 1 - player)):
                    print("win possible")
                    print(action)
                    return action
                else:
                    return minimax.search(board, player, dict_heuristic, time_left,  step, heuristic)

            else:

                raise ValueError('Value error encounter when processing len(shortest_path_player) in my_player.py')


        # Calling heuristic_state.py class to determine what the next action should be, based on current game information thru dict_heuristic
        action = hs.heuristic.switch_heuristic(dict_heuristic)

        # Switch depending on prescribed action fro switch_heuristic
        if (action == "EarlyMove"):

            (x, y) = board.get_shortest_path(self.player)[0]
            return ('P', x, y)

        elif (action == "WallMove"):
            
            choice = wall_move_choice(board, player)
            if (choice == "minimax"):

                return minimax.search(board, player, dict_heuristic, time_left,  step, heuristic)

            else:

                return choice

        elif (action == "MonteCarlo"):

            print("To be implemented")

            pass

        else:

            return minimax.search(board, player, dict_heuristic, time_left,  step, heuristic)
    
if __name__ == "__main__":
    agent_main(MyAgent())

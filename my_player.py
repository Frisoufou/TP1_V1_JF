#!/usr/bin/env python3
"""
Quoridor agent.
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
        """
        board, player = state # Get board and player with regards to a certain state
        player_to_move = (player + 1) % 2
        moves = board.get_legal_pawn_moves(player) # From given function with TP2 documents
        

        for move in moves:

            test_board = board.clone() # Get shallow copy of current board
            test_board.play_action(move,player) # Changing test board with given move to a player
            result_state = (test_board, player_to_move) # Obtain resuling game state

            yield(move, result_state)

    def bool_minimax(self, state, depth):
        """
        Function that returns True is minimax search stopped (e.g if board is finished)
        """
        board, player = state
        if board.is_finished() or depth == 2:
            return True
        else:
            return False

    def player_score(self, state):
        """
        Function that evaluates a current player's score according to a given game state
        """
        board, player = state
        return board.get_score(player) # From given function with TP2 documents

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
        
        # TODO: implement your agent and return an action for the current step.
        self.player = player
        state = (dict_to_board(percepts), player)
        return minimax.search(state, self)
        


if __name__ == "__main__":
    agent_main(MyAgent())

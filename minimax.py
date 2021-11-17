"""
First implementation of AlphaBeta search and returns the best action. Inspired from pseudo-code given in the course's notes. 

Second implementation should includes heuristic switch cases function 
"""

inf = float("inf")
from quoridor import *

def heuristic(board, player, dict_heuristic_infos):
        """
        Function that evaluates a current player's score according to a given game state
        """
        
        ##### Version 1 ####
        score = board.get_score()
        sp = board.get_shortest_path(player)

        if (len(sp) == 1):

            score += 1000
            return score

        elif (len(sp) != 1):

            return score

        else:
            raise ValueError("Problem while processing player_score_heuristic")

def search(board, player, dict_heuristic, time_left, step, h = lambda s, p: 0):
    """
    Args:
            state : Initial game state
            game : Instance of game class
            prune : If pruning is to be used or not
    """

    print("Processing minimax")
    max_depth = 5
    state = (board, player)
    prune=True



    def max_value(board, alpha, beta, depth):

        #if game.bool_minimax(step, board, depth, time_left): # If board is finished, hence, the game is done

        if board.is_finished():
            
            return board.get_score(player), None

        if depth > max_depth:

                return h(board, player, dict_heuristic), None # player_score_heuristic(board, player, "me"), None

        val = -inf # Initial value for max

        action = None # Initial action

        # Iterate in possible actions with given state

        for a in board.get_actions(player): # Where a is actions and s the score associated

            # Call for min value of current tree
            s = board.clone().play_action(a, player)
            v, _ = min_value(s, alpha, beta, depth + 1)

            # New value for min is condition respected
            if v > val:

                val = v # Assignation of the new value
                action = a # Assignation of the new corresponding action
                alpha = max(alpha, v)

                # If prune argument is true
                if prune:
                    
                      # If condition for beta is respected, return to parent knot
                    if v >= beta:

                        return v, a

                    # Get new alpha value
                    alpha = max(alpha, v)

        # Return value and corresponding action
        return val, action

    def min_value(board, alpha, beta, depth): 

        #if game.bool_minimax(step, board, depth, time_left): # If board is finished, hence, the game is done
        if board.is_finished():

            return board.get_score(1 - player), None
        
        if depth > max_depth:
            return h(board, player, dict_heuristic), None #game.player_score_heuristic(board, player, "oppo"), None

        val = inf # Initial value for min

        action = None # Initial action

        # Iterate in possible actions with given state
        for a in board.get_actions(1 - player): # Where a is actions and s the score associated
            
            # Call for max value of current tree
            s = board.clone().play_action(a, 1 - player)
            v, _ = max_value(s, alpha, beta, depth + 1)

            # New value for max is condition respected
            if v < val:

                val = v # Assignation of the new value
                action = a # Assignation of the new corresponding action
                beta = min(beta, v)
                # If prune argument is true
                if prune:
                    
                    # If condition for alpha is respected, return to parent knot
                    if v <= alpha:

                        return v, a

                    # Get new beta value
                    beta = min(beta, v)

         # Return value and corresponding action
        return val, action

    # Get max value for current state within interval borders
    _, action = max_value(board, -inf, inf, max_depth)

    # Return corresponding action
    return action


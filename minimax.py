"""
First implementation of AlphaBeta search and returns the best action. Inspired from pseudo-code given in the course's notes. 

Second implementation should includes heuristic switch cases function (heuristic_state.py)
"""

inf = float("inf")

def search(state, game, prune=True):
    """
    Args:
            state : Initial game state
            game : Instance of game class
            prune : If pruning is to be used or not
    """

    def max_value(state, alpha, beta, depth):

        if game.bool_minimax(state, depth): # If board is finished, hence, the game is done

            return game.player_score(state), None

        val = -inf # Initial value for max

        action = None # Initial action

        # Iterate in possible actions with given state
        for a, s in game.next_actions(state):

            # Call for min value of current tree
            v, _ = min_value(s, alpha, beta, depth + 1)

            # New value for min is condition respected
            if v > val:

                val = v # Assignation of the new value
                action = a # Assignation of the new corresponding action

                # If prune argument is true
                if prune:
                    
                      # If condition for beta is respected, return to parent knot
                    if v >= beta:

                        return v, a

                    # Get new alpha value
                    alpha = max(alpha, v)

        # Return value and corresponding action
        return val, action

    def min_value(state, alpha, beta, depth): 

        if game.bool_minimax(state, depth): # If board is finished, hence, the game is done

            return game.player_score(state), None

        val = inf # Initial value for min

        action = None # Initial action

        # Iterate in possible actions with given state
        for a, s in game.next_actions(state):
            
            # Call for max value of current tree
            v, _ = max_value(s, alpha, beta, depth + 1)

            # New value for max is condition respected
            if v < val:

                val = v # Assignation of the new value
                action = a # Assignation of the new corresponding action

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
    _, action = max_value(state, -inf, inf, 0)

    # Return corresponding action
    return action

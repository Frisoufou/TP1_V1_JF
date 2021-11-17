import minimax
from quoridor import *

def manhattanDistance(xy1, xy2):
    "Returns the Manhattan distance between points xy1 and xy2"
    return abs( xy1[0] - xy2[0] ) + abs( xy1[1] - xy2[1] )

class heuristic:

    def __init__(self):

        self._current_state = {}
        self._game_state = ""


    def switch_heuristic(dict_heuristic):

        condition = False # For structure to implement
        
        if (dict_heuristic["Step"] < 3 and dict_heuristic["Player1_walls"] + dict_heuristic["Player2_walls"] == 20): # Early game heuristic
            
            _game_state = "EarlyGame"
            print("Early move")
            return "EarlyMove"

        elif (condition):
             
             _game_state = "MonteCarlo"
             print("MonteCarlo move")
             return "MonteCarlo"
        
        elif (condition):
             
             _game_state = "DifferentState"
             print("AnotherTypeOfDecision")
             return "SomethingToBeImplemented"

        else: # Minimax algo 

            _game_state = "MiniMax"
            print("Minimax move")
            return "MiniMax"

        
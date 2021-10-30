class heuristic:

    def __init__(self):

        self._current_state = []
        pass
    
    def switch_heuristic(self, game_state):
        
        if game_state == "Early Game":

            early_heuristic = ""

            return early_heuristic

        elif game_state == "Mid Game":

            Mid_heuristic = ""

            return Mid_heuristic
        
        elif game_state == "Late Game":

            Late_heuristic = ""

            return Late_heuristic

        # Implement other heuristics such as a state with an inferiority or superiority of walls for either of the opponents...
        # Implement heuristic that considers the best path between each player and their respective goal position...
        
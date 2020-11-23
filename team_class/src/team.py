# Create a class called Team

class Team:

    def __init__(self, input_team_name, input_players, input_coach):
        self.name = input_team_name
        self.players = input_players
        self.coach = input_coach


    # Define function to add new player
    def add_player(self, new_player):
        self.players.append(new_player)
        

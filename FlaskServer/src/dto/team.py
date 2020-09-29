class Team:

    def __init__(self, team_name, first_member):
        self.team_name = team_name

    @property
    def name(self):
        return self.team_name
class Team:

    def __init__(self, team_name, first_member):
        self.team_name = team_name
        self.current_balance = 100000
        self.arch_level = 1

    @property
    def name(self):
        return self.team_name

    @property
    def balance(self):
        return self.current_balance

    @property
    def architecture_level(self):
        return self.arch_level


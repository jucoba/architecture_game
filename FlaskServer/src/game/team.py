import random


def create_team_id() -> int:
    return random.randint(1000, 9999)


class Team:
    _current_clients: int
    _capacity: int
    _current_balance: int

    def __init__(self, team_name, first_member, f=create_team_id):
        self.team_name = team_name
        self._current_balance = 100000
        self.architecture_level = 1
        self._can_receive_new_clients = False
        self._id = f()
        self._current_clients = 0

    @property
    def team_name(self):
        return self._team_name

    @team_name.setter
    def team_name(self, value):
        self._team_name = value

    @property
    def balance(self):
        return self._current_balance

    @property
    def architecture_level(self):
        return self._architecture_level

    @architecture_level.setter
    def architecture_level(self, value):
        self._architecture_level = value

    @property
    def can_receive_new_clients(self):
        return self._can_receive_new_clients

    @property
    def capacity(self):
        if self.architecture_level == 1:
            return 100
        if self.architecture_level == 2:
            return 600
        if self.architecture_level == 3:
            return 2000

    @property
    def id(self):
        return self._id

    @property
    def current_clients(self):
        return self._current_clients

    @property
    def cicle_cost(self):
        if self.architecture_level == 1:
            return 5000
        if self.architecture_level == 2:
            return 15000
        if self.architecture_level == 3:
            return 30000






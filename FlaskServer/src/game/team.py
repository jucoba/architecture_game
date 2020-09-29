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
        self._architecure_level = 1
        self._can_receive_new_clients = False
        self._capacity = 0
        self._id = f()
        self._current_clients = 0

    @property
    def name(self):
        return self.team_name

    @property
    def balance(self):
        return self._current_balance

    @property
    def architecture_level(self):
        return self._architecure_level

    @property
    def can_receive_new_clients(self):
        return self._can_receive_new_clients

    @property
    def capacity(self):
        return self._capacity

    @property
    def id(self):
        return self._id

    @property
    def current_clients(self):
        return self._current_clients




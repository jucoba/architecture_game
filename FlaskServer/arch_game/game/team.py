import random


def create_team_id() -> int:
    return random.randint(1000, 9999)


capacity_switch = {
    1: 100,
    2: 600,
    3: 10000
}

cost_switch = {
    1: 5000,
    2: 15000,
    3: 30000

}


class Team:
    current_clients: int
    _capacity: int
    _current_balance: int

    def __init__(self, team_name, first_member, f=create_team_id):
        self.team_name = team_name
        self._current_balance = 100000
        self.architecture_level = 1
        self._can_receive_new_clients = False
        self._id = f()
        self.current_clients = 0

    @property
    def team_name(self):
        return self._team_name

    @team_name.setter
    def team_name(self, value):
        self._team_name = value

    @property
    def income(self):
        return self.current_clients * 50

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
        return capacity_switch[self._architecture_level]

    @property
    def id(self):
        return self._id

    @property
    def current_clients(self):
        return self._current_clients

    @property
    def cicle_cost(self):
        return cost_switch[self._architecture_level]

    @property
    def pyg(self):
        return self.income - self.cicle_cost

    @current_clients.setter
    def current_clients(self, value):
        self._current_clients = value

    def add_clients(self, value):
        total_clients = self._current_clients + value
        if total_clients <= self.capacity:
            self._current_clients = total_clients
        else:
            self._current_clients = int(self._current_clients / 2)

import unittest
from src.dto.team import Team



class TestTeams(unittest.TestCase):

    def test_create_team_name_should_be_right(self):
        a_team = Team('A Team', 'Anibal')
        self.assertEqual(a_team.name, 'A Team', 'The name is not A Team')




import unittest, picker

def make_people(skills):
  return [picker.make_person("joe", p) for p in skills]

def get_teams(teams):
    return teams["A"], teams["B"]

class TestPicker(unittest.TestCase):

  def test_empty(self):
      result = picker.pick_teams([])
      team_a, team_b = get_teams(result)
      self.assertEqual(team_a, [])
      self.assertEqual(team_b, [])

  def test_one(self):
      result = picker.pick_teams(make_people([4]))
      team_a, team_b = get_teams(result)
      lengths = sorted([len(team_a), len(team_b)])
      self.assertEqual(lengths, [0, 1])

  def test_two(self):
      result = picker.pick_teams(make_people([4, 4]))
      team_a, team_b = get_teams(result)
      lengths = sorted([len(team_a), len(team_b)])
      self.assertEqual(lengths, [1, 1])

  def test_odd(self):
      result = picker.pick_teams(make_people([4, 3, 3, 2, 2]))
      team_a, team_b = get_teams(result)
      lengths = sorted([len(team_a), len(team_b)])
      self.assertEqual(lengths, [2, 3])

  def test_imbalance(self):
      result = picker.pick_teams(make_people([4, 1, 1, 1]))
      team_a, team_b = get_teams(result)
      lengths = sorted([len(team_a), len(team_b)])
      self.assertEqual(lengths, [2, 2])

  def test_eveness(self):
    players = range(1, 5) + range(1, 5)
    result = picker.pick_teams(make_people(players))
    team_a, team_b = get_teams(result)
    lengths = sorted([len(team_a), len(team_b)])
    self.assertEqual(lengths, [4, 4])
    skill_a = sum([p["skill"] for p in team_a])
    skill_b = sum([p["skill"] for p in team_b])
    self.assertEqual(skill_a, skill_b)

if __name__ == '__main__':
    unittest.main()
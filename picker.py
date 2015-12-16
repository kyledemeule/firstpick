import random

MAX_ITER = 1000

def make_person(name, skill=None):
    return {
        "name": name,
        "skill": skill
    }

def pick_teams(people):
    random.shuffle(people)
    people = sorted(people, key=lambda p: -p["skill"])

    team_a = {
        "num": 0,
        "sum": 0,
        "players": []
    }
    team_b = {
        "num": 0,
        "sum": 0,
        "players": []
    }

    distribute_players(team_a, team_b, people)
    fix_balance(team_a, team_b)
    return {"A": team_a["players"], "B": team_b["players"]}

def add_player(team, player):
    team["players"].append(player)
    team["num"] += 1
    team["sum"] += player["skill"]

def remove_player(team):
    # players were added in 
    player = team["players"].pop()
    team["num"] -= 1
    team["sum"] -= player["skill"]
    return player

def distribute_players(team_a, team_b, players):
    for player in players:
        if team_a["sum"] == team_b["sum"]:
            if random.randint(0, 1) == 0:
                add_player(team_a, player)
            else:
                add_player(team_b, player)
        elif team_a["sum"] < team_b["sum"]:
            add_player(team_a, player)
        else:
            add_player(team_b, player)

def fix_balance(team_a, team_b):
    while team_a["num"] - team_b["num"] >= 2:
        add_player(team_b, remove_player(team_a))
    while team_b["num"] - team_a["num"] >= 2:
        add_player(team_a, remove_player(team_b))

def team_difference(teams):
    team_a_skill = sum([p["skill"] for p in teams["A"]])
    team_b_skill = sum([p["skill"] for p in teams["B"]])
    return team_a_skill - team_b_skill

def team_imbalance(teams):
    return abs(team_difference(teams))

def print_teams(teams):
    for team in teams:
        print("Team %s:" % (team))
        for player in teams[team]:
            print("\t%s, %i" % (player["name"], player["skill"]))

def main():
    people = [
        make_person("John Doe1", 4),
        make_person("John Doe2", 4),
        make_person("John Doe3", 3),
        make_person("John Doe4", 3),
        make_person("John Doe5", 2),
        make_person("John Doe6", 2),
        make_person("John Doe7", 2),
        make_person("John Doe8", 4),
        make_person("John Doe9", 1),
        make_person("John Doe10", 1),
    ]
    people = [
        make_person("John Doe1", 4),
        make_person("John Doe1", 3),
        make_person("John Doe2", 3),
        make_person("John Doe2", 2),
        make_person("John Doe4", 3),
    ]
    teams = pick_teams(people)
    print_teams(teams)
    error = team_imbalance(teams)
    print "Error: %i" % (error)


if __name__ == "__main__":
    main()
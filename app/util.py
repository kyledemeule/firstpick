from lib.picker import make_person

def parse_params(params):
    player_names = []
    for p in params.getlist('player_name[]'):
        player_names.append(p)
    player_skills = []
    for p in params.getlist('player_skill[]'):
        player_skills.append(int(p))

    players = []
    for name, skill in zip(player_names, player_skills):
        players.append(make_person(name, skill))
    return players
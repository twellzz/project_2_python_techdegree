import random
players_placed = {
            'Sharks experienced':0,
            'Sharks unexperienced':0,
            'Raptors experienced':0,
            'Raptors unexperienced':0,
            'Dragons experienced':0,
            'Dragons unexperienced':0
}

TEAM_NAMES = ['Sharks', 'Raptors', 'Dragons']
chosen_team = random.choice(TEAM_NAMES)
print(chosen_team)
my_key = chosen_team + ' experienced'
print(my_key)
my_return = players_placed[my_key]
print(my_return)
TEAM_NAMES.remove(chosen_team)
print(TEAM_NAMES)

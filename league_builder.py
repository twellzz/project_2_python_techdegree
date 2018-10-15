import csv
import random

TEAM_NAMES = ['Sharks', 'Raptors', 'Dragons']
SOURCE_FILE = 'soccer_players.csv'

shark_list = ['Sharks']
raptor_list = ['Raptors']
dragon_list = ['Dragons']

# number of players in each team, both experienced and not
players_placed = {
            'Sharks experienced': 0,
            'Sharks unexperienced': 0,
            'Raptors experienced': 0,
            'Raptors unexperienced': 0,
            'Dragons experienced': 0,
            'Dragons unexperienced': 0
}


def count_experienced(players_list, TEAM_NAMES):
    experienced_players = 0

    for individual in players_list:
        if individual['Soccer Experience'].lower() == 'yes':
            experienced_players += 1
    # how many experienced players per team
    return experienced_players / len(TEAM_NAMES)


def assign_team(experience, TEAM_NAMES, players_placed,
                experienced_players, unexperienced_players):
    team_copy = TEAM_NAMES.copy()

    while True:
        chosen_team = random.choice(team_copy)
        if experience.lower() == 'yes':
            team_key = chosen_team + ' experienced'
            if players_placed[team_key] >= experienced_players:
                # this team already has enough experienced players
                # remove the team and go again
                team_copy.remove(chosen_team)
            else:
                return [chosen_team, team_key]
        else:
            team_key = chosen_team + ' unexperienced'
            if players_placed[team_key] >= unexperienced_players:
                # this team already has enough experienced players
                # remove the team and go again
                team_copy.remove(chosen_team)
            else:
                return [chosen_team, team_key]


def guardian_letter(child, guardian, team):
    # write the letter to the guardian
    letter_content = (
        "Dear {},\n\nMy name is Tyler and I'm reaching out to "
        "inform you that {} was selected to play for the {} "
        "this soccer season.\nThe first practice is October 22 at "
        "6 PM. Have a great season!\n\n"
        "Sincerly,\nTyler".format(guardian, child, team)
        )

    txt_name = child.split()[0] + "_" + child.split()[1] + ".txt"
    with open(txt_name, "w") as letter_file:
        letter_file.write(letter_content)


def transform_csv(source_file):
    # open the csv and handle it to understandable information
    with open(source_file, newline='') as players_file:
        players_reader = csv.DictReader(players_file, delimiter=',')
        players_list = list(players_reader)

        return players_list


if __name__ == '__main__':
    # take the CSV and transform it into a readable format (dict)
    players_list = transform_csv(SOURCE_FILE)
    # how many players are in the league? lets us be flexible
    league_size = len(players_list)
    # how many experienced players permitted per team
    experienced_players_limit = count_experienced(players_list, TEAM_NAMES)
    # how many total players permitted per team?
    total_players_limit = league_size / len(TEAM_NAMES)
    # how many unexperienced players allowed per team
    un_players_limit = total_players_limit - experienced_players_limit

    # loop through all of the players
    for individual in players_list:
        # relevant player information
        player_name = individual['Name']
        experience = individual['Soccer Experience']
        guardians = individual['Guardian Name(s)']
        # return a random team (running the proper checks)
        # also to make it easy return the key of the dictionary to change value
        choose_team = assign_team(
            experience, TEAM_NAMES, players_placed,
            experienced_players_limit, un_players_limit
            )

        assigned_team = choose_team[0]
        returned_key = choose_team[1]
        # add player info to the proper team
        if assigned_team == 'Sharks':
            shark_list.append(
                '{}, {}, {}'.format(player_name, experience, guardians)
            )
        elif assigned_team == 'Raptors':
            raptor_list.append(
                '{}, {}, {}'.format(player_name, experience, guardians)
            )
        else:
            dragon_list.append(
                '{}, {}, {}'.format(player_name, experience, guardians)
            )
        # change the players_placed dictionary
        number_placed_already = players_placed[returned_key] + 1
        players_placed[returned_key] = number_placed_already
        # create letter to guardians
        guardian_letter(player_name, guardians, assigned_team)

# create txt file that contains all the teams information
total_list = shark_list + raptor_list + dragon_list
with open("teams.txt", "w") as final_file:
    for line in total_list:
        final_file.write(line + '\n')

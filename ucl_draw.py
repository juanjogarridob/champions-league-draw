import random

ucl_teams = {
    "ENG" : {"Arsenal", "Manchester City", "Aston Villa", "Liverpool"},
    "GER" : {"Bayern München", "Dortmund", "Leipzig", "Stuttgart", "Leverkusen"},
    "ESP" : {"Barcelona", "Real Madrid", "Atlético de Madrid", "Girona"},
    "ITA" : {"Juventus", "Inter", "AC Milan", "Bologna", "Atalanta"},
    "FRA" : {"Paris Saint-Germain", "Brest", "Mónaco", "Lille"},
    "POR" : {"Sporting CP", "Benfica"},
    "NED" : {"PSV Eindhoven", "Feyenoord"},
    "AUT" : {"SK Sturm Graz", "Salzburg"},
    "BEL" : {"Club Brugge"},
    "SCO" : {"Celtic"},
    "CZE" : {"Sparta Praha"},
    "UKR" : {"Shaktar Donetsk"},
    "SUI" : {"Young Boys"},
    "SVK" : {"Slovan Bratislava"},
    "SRB" : {"Crvena Zvezda"},
    "CRO" : {"GNK Dinamo"}
}

# team_num = 0
# for teams in ucl_teams.values():
#     for team in teams:
#         team_num += 1
# print(team_num)

pot_1 = ["Real Madrid", "Manchester City", "Bayern München", "Paris Saint-Germain", "Liverpool", "Inter", "Dortmund", "Leipzig", "Barcelona"]
pot_2 = ["Leverkusen", "Atlético de Madrid", "Atalanta", "Juventus", "Benfica", "Arsenal", "Club Brugge", "Shaktar Donetsk", "AC Milan"]
pot_3 = ["Feyenoord", "Sporting CP", "PSV Eindhoven", "GNK Dinamo", "Salzburg", "Lille", "Crvena Zvezda", "Young Boys", "Celtic"]
pot_4 = ["Slovan Bratislava", "Monaco", "Sparta Praha", "Aston Villa", "Bologna", "Girona", "Girona", "Stuttgart", "Sturm Graz", "Brest"]
pots = [pot_1, pot_2, pot_3, pot_4]

# print(len(pot_1), len(pot_2), len(pot_3), len(pot_4))
# team = pot_1[random.randint(0, 8)]
# print(team)

def draw_team():
    pot = int(input("Select one pot to start the draw (1-4): "))
    if pot == 1:
        team = pot_1[random.randint(0, 8)]
    elif pot == 2:
        team = pot_2[random.randint(0, 8)]
    elif pot == 3:
        team = pot_3[random.randint(0, 8)]
    elif pot == 4:
        team = pot_4[random.randint(0, 8)]
    else:
        return 'Select one pot from 1 to 4.'

    return team

my_team = draw_team()
print(my_team)

def check_team_country(team):
    for key, value in ucl_teams.items():
        if team in value:
            return key
    else:
        return 'Associated country not found.'

print(check_team_country(my_team))

def draw_rivals(team):
    
    rivals = []

    for pot in pots:
        random.shuffle(pot)
        count = 0

        for t in pot:
            if t != team and check_team_country(t) != check_team_country(team):
                count += 1
                rivals.append(t)
                
            
            if count >=2:
                break

    return rivals

print(draw_rivals(my_team))
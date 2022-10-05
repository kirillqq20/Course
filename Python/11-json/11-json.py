import json
file = 'users_json.txt'
myfile = open(file, mode = 'w', encoding = 'utf-8')

hero1 = {
    'name'  : 'Andrey',
    'years' : '24',
    'games' : [ 'gta', 'withes', 'formula']
}

hero2 = {
    'name'  : 'Egor',
    'years' : '24',
    'games' : [ 'heartstone', 'dota2', 'civilization']
}

all_players = []
all_players.append(hero1)
all_players.append(hero2)

json.dump(all_players, myfile)
myfile.close()

myfile = open (file, mode = 'r', encoding= 'utf-8')
json_data = json.load(myfile)

for user in json_data:
    print ('Player name is --- ' + str(user['name']) + ' years = ' + str(user['years']) + ' games = ' + str(user['games'][0]) + ' , ' + str(user['games'][1]) + ' , ' + str(user['games'][2]))
enemy = {
    'loc_x': 100,
    'loc_y': 200,
    'color': 'yellow',
    'health': 100,
    'name': 'monstr'
}
print(enemy)
print('------------------------')

all_enemies = []
for x in range(0, 5):
    all_enemies.append(enemy.copy())

for y in all_enemies:
    print(y)
all_enemies[3]['health'] = 20

for t in all_enemies:
    if t['health'] < 50:
        print(t)
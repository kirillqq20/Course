from module import *


solider1 = Hero('Vanya',20,'green')
solider2 = Hero('Petya', 30,'green')


solider1.show_hero()
solider2.show_hero()

solider2.edit_in_monstr()
solider2.level_up()
solider1.set_health()
solider2.show_hero()
solider1.show_hero()


#########################################################

print('===================================================')

solider3 = SuperHero('MONSTR',33,'RED')
solider4 = SuperHero('Ivan', 25, 'black')

solider3.set_health()
solider4.set_health()

solider3.add_skills()
solider3.count_mana()

solider4.add_skills()
solider4.count_mana()

solider3.show_superhero()
solider4.show_superhero()


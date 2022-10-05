class Hero():
    ### Class to create hero for game ###
    def __init__(self, name, level, color):
    ### init our hero ###
        self.name = name
        self.level = level
        self.color = color
        self.health = 100
    
    def show_hero(self):
        print(self.name + ' Level = ' + str(self.level) + ' color = ' + self.color + ' health = ' + str(self.health))

    def level_up(self):
        self.level += 1

    def edit_in_monstr(self):
        self.color = 'RED'
        self.name = 'MONSTR'
        self.level = 50

    def set_health(self):
        if self.name == 'MONSTR':
            self.health = 500
        else:
            self.health = 350

###########################################################################

class SuperHero(Hero):
    def __init__(self, name, level, color):
        super().__init__(name, level, color)
        self.skills = 'no skills'
        self.mana = 0

    def add_skills(self):
        if self.name == 'MONSTR':
            self.skills = 'punch'
        else:
            self.skills = 'fireball'

    def count_mana(self):
        if self.skills == 'fireball':
            self.mana = 80
        elif self.skills == 'punch':
            self.mana = 45
        else:
            self.mana = 20

    def show_superhero(self):
        print(self.name + ' Level = ' + str(self.level) + ' color = ' + self.color + ' health = ' + str(self.health) + ' skills = ' + self.skills + ' mana = ' + str(self.mana))

###########################################################################
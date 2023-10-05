import random
from rules import Rules
from armor import Armor

class Character:
    def __init__(self, name):
        #weapon = Weapon(Weapon("Wood Sword", 2))
        self.rules = Rules()
        self.characteristics = {
            "name":name,
            "defense": random.randrange(0,10),
            "attack": random.randrange(0,10),
            "pv": random.randrange(50,100),
            "level": 1,
            "experience": 0,
            "gold": 0,
            "equipment": {
                "right_arm": Armor("Wood Sword", 2,0),
                "left_arm": Armor('',0,0),
                "head": Armor('',0,0)
            }
        }
        
    def show_stats(self):
        print('-----------STATS----------')
        print('- NAME:    '+ self.characteristics['name'])
        print('- Defense: '+ str(self.characteristics['defense']))
        print('- Attack: '+ str(self.characteristics['attack']))
        print('- PV: '+ str(self.characteristics['pv']))
        print('- LEVEL: '+str(self.characteristics['level']))
        print('- Exp: '+ str(self.characteristics['experience']))
        print('-$'+str(self.characteristics['gold']))

    def attack(self, personaje):
        result = Rules.attack(self.calculate_attack(), personaje.calculate_defense())
        if result['result'] >0:
            personaje.characteristics['pv'] = personaje.characteristics['pv'] - result['result']
        return {'result': result['result'], 'pv': personaje.characteristics['pv']}

    def calculate_attack(self):
        return self.characteristics['attack'] 
        +self.characteristics['equipment']['right_arm'].characteristics['attack']
        +self.characteristics['equipment']['left_arm'].characteristics['attack']
        +self.characteristics['equipment']['head'].characteristics['attack']
    
    def calculate_defense(self):
        return self.characteristics['defense'] 
        +self.characteristics['equipment']['right_arm'].characteristics['defense']
        +self.characteristics['equipment']['left_arm'].characteristics['defense']
        +self.characteristics['equipment']['head'].characteristics['defense']
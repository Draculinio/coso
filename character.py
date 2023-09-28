import random
from rules import Rules
from weapons import Weapon

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
                "weapon": Weapon("Wood Sword", 2)
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

    def attack(self, attack):
        result = Rules.attack(attack, self.characteristics['defense'])
        if result['result'] >0:
            self.characteristics['pv'] = self.characteristics['pv'] - result['result']
        return {'result': result['result'], 'pv': self.characteristics['pv']}

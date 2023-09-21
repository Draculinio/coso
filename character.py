import random

class Character:
    def __init__(self, name):
        self.name = name
        self.defense = random.randrange(0,10)
        self.attack = random.randrange(0,10)
        self.pv = random.randrange(50,100)
        self.level = 1
        self.experience = 0
        self.gold = 0
    
    def show_stats(self):
        print('-----------STATS----------')
        print('- NAME:    '+self.name)
        print('- Defense: '+ str(self.defense))
        print('- Attack: '+ str(self.attack))
        print('- PV: '+ str(self.pv))
        print('- LEVEL: '+str(self.level))
        print('- Exp: '+ str(self.experience))
        print('-$'+str(self.gold))

    

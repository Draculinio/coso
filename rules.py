import random 
class Rules:

    def attack(a,d):
        attack = a + random.randrange(1,7)
        defense = d + random.randrange(1,7)
        return {'attack': attack, 'defense':defense, 'result': attack - defense}
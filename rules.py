from character import Character

class Rules:

    def atacar(a,d):
        result = a.attack - d.defense
        if result > 0:
            print('ATAQUE EXITOSO')
            return result
        else:
            print('TU ATAQUE DIO ASCO')
            return 0
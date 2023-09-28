from character import Character
from os import system, name
 
if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')
mi_personaje = Character('Pepito')
mi_personaje.show_stats()
otro_personaje = Character('Juancito')
otro_personaje.show_stats()
result = otro_personaje.attack(mi_personaje.characteristics['attack']+mi_personaje.characteristics['equipment']['weapon'].characteristics['attack'])
otro_personaje.show_stats()
print(result)
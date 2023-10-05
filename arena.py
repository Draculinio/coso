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
result = mi_personaje.attack(otro_personaje)
otro_personaje.show_stats()
print(result)
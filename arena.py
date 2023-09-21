from character import Character
from rules import Rules
mi_personaje = Character('Pepito')
mi_personaje.show_stats()
otro_personaje = Character('Juancito')
otro_personaje.show_stats()
otro_personaje.pv = otro_personaje.pv - Rules.atacar(mi_personaje,otro_personaje)
otro_personaje.show_stats() 
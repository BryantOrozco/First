
vida_pikachu = 100
vida_enemigo = 0

contrincante = input("Contra quien te quieres enfrentar? \nBulbasaur\nCharmander\nsquirtle\nContrincante:").upper()

if contrincante == "BULBASAUR":
    vida_enemigo = 100
    name_enemigo = "BULBASAUR"
    atak_enemigo = 10
elif contrincante == "SQUIRTLE":
    vida_enemigo = 90
    name_enemigo = "SQUIRTLE"
    atak_enemigo = 8
elif contrincante == "Charmander":
    name_enemigo = "Charmander"
    vida_enemigo = 80
    atak_enemigo = 7

while vida_pikachu > 0 and vida_enemigo > 0:
   ataque_input = input("Escoje tu ataque: (Chispazo) (Bola voltio): ").upper()
   if ataque_input == "CHISPAZO":
       vida_enemigo -= 10
   elif ataque_input == "BOLA VOLTIO":
        vida_enemigo -= 12

   print("La vida del {} es de {}" .format(name_enemigo ,vida_enemigo))

   print("{} te hace un ataque de {} puntos de dano".format(name_enemigo , atak_enemigo))
   vida_pikachu -= atak_enemigo
   print("La vida de tu pikachu es de {}".format(vida_pikachu))

print("Elcombate termino")

if vida_enemigo <= 0:
    print("Has Ganado el combate")
if vida_pikachu <= 0:
    print("Has perdido el combate")

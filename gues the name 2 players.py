
second_player_guess = 0
number_to_guess = int(input("Jugador 1 introduce el numero a advinar (Sin que el juegador 2 VEA!!): "))

while second_player_guess != number_to_guess:
    second_player_guess = int(input("Jugador 2 ingresa el numero que creas correcto: "))

    if second_player_guess != number_to_guess:
        print("No es le numero correcto intenta de nuevo")

print("HAS Adivinado el numero!!")
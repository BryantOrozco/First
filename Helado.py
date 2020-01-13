


quiere_helado = input("Quieres comprar un helado ? (Si / No ): ").upper()
dinero = int(input("El helado cuesta 20 pesos cuanto dinero tiene en su tarjeta? "))
costo_helado = 20

if quiere_helado == "SI" and dinero >= costo_helado :
    print("Usted a comprado un helado")
    print("Saldo restante en su tarjeta es: {}".format(dinero - costo_helado))
elif dinero < costo_helado :
    print("No tiene dinero sufuciente")
elif quiere_helado != "SI" and quiere_helado != "NO":
    print("Has introducido una opcion incorreecta, recuerda que solo es si o no ")
else:
    print("No has comprado el helado")




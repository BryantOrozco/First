

print("CLACULADORA")
operation = input("Que Operacion quiere hacer? (Multiplicar / Dividir / Sumar / Restar): ").upper()
number_one = float(input("Primer numero que quieras {}: ".format(operation)))
number_two = float(input("Segundo numero que quieras {}: ".format(operation)))

if operation == "MULTIPLICAR":
    result = number_one * number_two
    print("El resultado de tu multiplicacion es igual a: {}".format(result))
elif operation == "DIVIDIR":
    result = number_one / number_two
    print("El resulatado de tu division es: {}".format(result))
elif operation == "SUMAR":
    result = number_one + number_two
    print("El resultado de tu suma es: {} ".format(result))
elif operation == "RESTAR":
    result = number_one - number_two
    print("El Reslutado de tu division es: {}".format(result))
else:
    print("La operacion es incorrecta intenta de nuevo")

print("HASTA LUEGO!")




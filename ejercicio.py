resultado = 0.00
tiempo = int(input("Introduzca las horas que mantuvo estacionado: "))
tiempo2 = int(input("Introduzca los minutos que mantuvo estacionado: "))
dia = int(input("1. Lunes, martes o miércoles, 2. Jueves, viernes, 3. Sábado, domingo: "))

tarifas = {
    1: {"hora": 2.00, "minuto_extra": 0.00},
    2: {"hora": 2.50, "minuto_extra": 0.00},
    3: {"hora": 3.00, "minuto_extra": 0.00}
}

if dia in tarifas:
    tarifa = tarifas[dia]
    if tiempo2 >= 5:
        resultado = (tiempo + 1) * tarifa["hora"]
    else:
        resultado = tiempo * tarifa["hora"]
else:
    print("Selección incorrecta")

print(f"El total a pagar es de: {resultado} dólares")

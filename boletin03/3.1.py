precioinicial=float(input("Precio inicial: "))
preciofinal=float(input("Precio final: "))
porcentaje=(100-(preciofinal/precioinicial)*100)
print("El porcentaje es "+ str(porcentaje) + "%")
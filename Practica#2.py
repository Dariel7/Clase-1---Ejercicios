nota = int(input("Digite su nota: "))
carrera = input("Carrera: ")

if nota >= 90 and carrera.upper() == "ISC":
    print("Aplica para que la beca en el MIT")

else: 
    print("Lo sentimos no tenemos becas disponibles")
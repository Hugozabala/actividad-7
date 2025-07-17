

estudiantes = {}

def menu():
    print("\n menu principal")
    print("1. Ingreso de estudiante")
    print("2. mostrar todo los estudiantes ingresados ")
    print("3. buscar estudiante por carnet")
    print("4. salir")
op=0
while op!=4:
    menu()
    op=int(input("ingrese que opcion desea ejecutar"))


    if op==1:
        cantidad = int(input("¿Cuántos estudiantes desea ingresar? "))

        for i in range(cantidad):
            print(f"\nEstudiante #{i + 1}")
            carnet = input("Ingrese el número de carnet: ")
            nombre = input("Ingrese el nombre completo: ")
            edad = int(input("Ingrese la edad: "))
            carrera = input("Ingrese la carrera: ")
            op2 = int(input("Ingrese cuantos cursos desea ingresar : "))
            for a in range(op2):
                curso = input("  ingrese código curso: ")
                nota =int(input(" ingreso nota de tareas: "))
                nota1 = int(input(" ingreso nota de parcial: "))
                nota2 = int(input(" ingreso nota de proyecto: "))

                suma =nota+nota1+nota2

                estudiantes[carnet] = {
                "nombre": nombre,
                "edad": edad,
                "carrera": carrera,
                "codigo": {
                    "curso": curso,
                     "notas_tareas": nota,
                     "nota_parcial": nota1,
                     "nota_proyecto":nota2
                }
                }
                print("estudiante ingresado con éxito")

    elif op==2:
       print(f"estudiantes ingresados" )
       for carnet,datos in estudiantes.items():
           print(f"\n carnet:{carnet}")
           print(f"\n nombre:{datos['nombre']}")
           print(f"\n edad:{datos['edad']}")
           print(f"\n carrera:{datos['carrera']}")
           for datos,codigo ,date in estudiantes.items():
               print(f"Correo: {date['codigo']['curso']}")
               print(f"Correo: {date['codigo']['nota_tareas']}")
               print(f"Correo: {date['codigo']['nota_parcial']}")
               print(f"Correo: {date['codigo']['nota_proyecto']}")

           print("se mostró todo los datos de estudiante ")



    elif op==3:
        buscado = input("Ingrese el número de carnet que desea buscar: ")

        if buscado in estudiantes:
            estudiante = estudiantes[buscado]
            print("\nEstudiante encontrado:")
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Edad: {estudiante['edad']}")
            print(f"Carrera: {estudiante['carrera']}")

        else:
            print("Estudiante no encontrado.")

    elif op==4:
        print("\nsalir de programa...")





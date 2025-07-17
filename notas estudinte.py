

estudiantes = {}

def menu():
    print("\n menu principal")
    print("1. Ingreso de estudiante")
    print("2. mostrar todo los estudiantes ingresados ")
    print("3. buscar estudiante por carnet")
    print("4. salir")
op=0
menu()
op=int(input("ingrese que opcion desea ejecutar"))
while op!=4:
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
                curso = input("  curso: ")
                nota =int(input(" ingreso nota de tareas: "))
                nota1 = int(input(" ingreso nota de parcial: "))
                nota2 = int(input(" ingreso nota de proyecto: "))

                suma =nota+nota1+nota2

                estudiantes[carnet] = {
                "nombre": nombre,
                "edad": edad,
                "carrera": carrera,
                "curso": {
                    "codigo": curso,
                     "notas_tareas": nota,
                     "nota_parcial": nota1,
                     "nota_notaproyecto":nota2

                }
            }
    elif op==2:
       print(f"estudiantes ingresados" )
    elif op==3:
        buscado = input("Ingrese el número de carnet que desea buscar: ")

        if buscado in estudiantes:
            estudiante = estudiantes[buscado]
            print("\nEstudiante encontrado:")
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Edad: {estudiante['edad']}")
            print(f"Carrera: {estudiante['carrera']}")
            print(f"Correo: {estudiante['contacto']['correo']}")
            print(f"Teléfono: {estudiante['contacto']['telefono']}")
        else:
            print("Estudiante no encontrado.")

    elif op==4:
        print("\nsalir de programa...")





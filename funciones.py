#funciones_Katherinnacandia_FPY1101_013v

libros = []
nombres_usuarios = []
listas_de_usuarios = [] #me falta una lista de usuarios, no estoy segura donde ponerlo
def registrar_libro(): #fijate bien y termina

    titulo = input("Ingrese el nombre del libro que desea registar: ") 
    autor = input("ingrese el nombre del autor del libro: ") 
    #cómo hago el sku? algo que cuente las letras y las "corte"
    try:
        año = int(input("ingrese el año de públicación del libro: "))
        
    except ValueError: 
        print ("ingrese solo el año en números")
        return
    #de verdad no sé como hacerlo
    sku1 = input("Ingrese las primeras 6 letras del título: ")
    sku2= input("Ingrese las 3 primeras letras del nombre del autor: ")
    sku3= input("Ingrese el año: ")
    sku = sku1, sku2, sku3
    print(sku)
    
    #validación
    if titulo and autor and año and sku1 and sku2:
        libro = {
            ['titulo'] : titulo,
            ['autor'] : autor,
            ['año'] : año,
            ['sku1'] : sku1,
            ['sku2'] : sku2,
            ['sku'] : sku
        }
        libros.append(libro)
    else:
        print("Por favor, rellene todo")

   

registrar_libro()
def prestar_libro(libros): 
    n_usuario = input("por favor, escriba su nombre: ")
    nombres_usuarios.append(n_usuario) 
    sol_sku = input("Escriba el SKU del libro que desea: ")
    sku_encontrados = [libro for libro in libros if libros['sku'] == sol_sku] 
    if sku_encontrados:
        print("el libro existe")
        #con un if? 
        if sku_encontrados in libros: 
            print("El libro está prestado UnU, pero le invitamos a seguir buscando") 
        else:
            print("libro disponible")
            fecha = input("ingrese la fecha de cuándo lo arrendó: ") 
            print(n_usuario, fecha, sku_encontrados) 
    else:
        print("No existen registros, por favor, vuelva a intentarlo") 
        return 

    
        
def listar_libros(libros): 
    for libro in libros:
        print("libros uwu")
        for key, value in libros.items(): 
            print(f"{key} : {value}")

def imprimir_prestamo(libros): 
    with open('reporte_préstamos.txt', 'w') as prestamos:
        prestamos.write("USUARIO            TÍTULO          FECHA PRESTAMO     \n")
        prestamos.write("\n")
        prestamos.write(f"{libros['titulo']}") #me falta el nombre del usuario y la fecha de prestamooooo, lloro

    with open('reporte_préstamos.txt', 'r') as prestamos: 
        leer = prestamos.read()
        print(leer)

def menu(): 
    
    while True:
        try:
            print("Bienvenido, ¿Qué desea hacer?")
            print("\4" * 30)
            op = int(input("1.- Registrar libro\n2.- Prestar libro\n3.- Listar todos los libros\n Imprimir reporte de préstamos\n5.- Salir del programa:\n >>>>  "))
            if op == 1:
                registrar_libro
            elif op == 2:
                prestar_libro(libros)
            elif op == 3:
                listar_libros(libros)
            elif op == 4:
                imprimir_prestamo(libros)
            elif op == 5:
                print ("¡Adioos!")
                print("Desarrollado por Katherinna Candia\nRun: 22020337-9")
            else:
                print("Ingrese un número válido")
        except ValueError:
            print("Por favor seleccione una opción válida")
            break

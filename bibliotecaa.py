import random 

Datos_generales = []


cantidad = int(input("Cantidad de libros a registrar: "))
print("\nRellene los siguientes datos.")


for i in range (cantidad):
    print(f"\nLibro {i + 1}:")
    
   
    while True:
        Nombre = input("Nombre del libro: ").strip()
        if Nombre:
            break
        else:
            print("El nombre del libro no puede quedar vacio. Ingrese el nombre")
            
    
    while True:
        Autor = input("Nombre del autor: ").strip().lower()
        if Autor:
            break
        else:
            print("El nombre del autor no puede quedar vacio. Ingrese el autor")
            
    
    while True:
        try:
            AP = int(input("Año de publicación: "))
            if AP > 0:
                break
            else:
                print ("El año de publicacion debe ser positivo. Intenta nuevamente")       
        except ValueError:
            print("Entrada invalida. Ingrese un número entero")
            
   
    while True:
        Genero = input ("Genero del libro: ").strip().lower()
        if Genero:
            break
        else:
            print("El genero no puede quedar vacio. Ingrese genero")

    
    while True:
        try:
            NP = int(input("cantidad de paginas del libro: "))
            if NP > 0:
                break
            else:
                print("La cantidad de paginas debe ser positivo. Intenta nuevamente")
        except ValueError:
            print("Entrada invalida. Ingrese cantidad entera")
            
   
    Libros = {
      "Nombre": Nombre,
      "Autor": Autor,
      "Año_publicado": AP, 
      "Genero": Genero,
      "Numero_paginas": NP 
      }
    
    Datos_generales.append(Libros)


def mostrar_libro(libro):
    print(f"   Nombre: {libro['Nombre']}")
    print(f"   Autor: {libro['Autor'].capitalize()}") 
    print(f"   Año de Publicación: {libro['Año_publicado']}") 
    print(f"   Genero: {libro['Genero'].capitalize()}") 
    print(f"   Paginas: {libro['Numero_paginas']}") 


while True:
    print("\n--- Opciones de Búsqueda ---")
    print("1. Buscar por Genero")
    print("2. Encontrar el Libro más Largo")
    print("3. Encontrar el Libro más Largo por Genero")
    print("4. Obtener Recomendación de Libro")
    print("5. Salir de la Búsqueda")
    
    try:
        opciones = int(input("Elige una opción del 1 al 5: "))
        
        if opciones == 1:
            genero_buscar = input("Ingresa el genero a buscar: ").strip().lower()
            
            libros_encontrados = [
                libro for libro in Datos_generales
                
                if genero_buscar in libro['Genero'].lower() 
            ]
            
            if libros_encontrados:
                print(f"\n--- Libros encontrados en el género '{genero_buscar.capitalize()}' ---")
                for libro in libros_encontrados: 
                    mostrar_libro(libro)
            else:
                print(f"No se encontraron libros que contengan '{genero_buscar.capitalize()}' en su género.")
                
        elif opciones == 2:
            if not Datos_generales:
                print("No hay libros registrados para encontrar el más largo.")
            else:
                
                libro_mas_largo = None
                max_paginas = -1
                for libro in Datos_generales:
                    if libro['Numero_paginas'] > max_paginas:
                        max_paginas = libro['Numero_paginas']
                        libro_mas_largo = libro
                
                print("\n--- El Libro más Largo ---")
                mostrar_libro(libro_mas_largo)
                
        elif opciones == 3:
            if not Datos_generales:
                print("No hay libros registrados para encontrar el más largo por género.")
            else:
                genero_buscar = input("Ingresa el genero para buscar el libro más largo: ").strip().lower()
                libros_por_genero = [
                    libro for libro in Datos_generales
                    if genero_buscar in libro['Genero'].lower() 
                ]
                
                if libros_por_genero:
                    libro_mas_largo_genero = None
                    max_paginas_genero = -1
                    for libro in libros_por_genero:
                        if libro['Numero_paginas'] > max_paginas_genero:
                            max_paginas_genero = libro['Numero_paginas']
                            libro_mas_largo_genero = libro
                    
                    print(f"\n--- El Libro más Largo en el género '{genero_buscar.capitalize()}' ---")
                    mostrar_libro(libro_mas_largo_genero)
                else:
                    print(f"No se encontraron libros que contengan '{genero_buscar.capitalize()}' en su género para determinar el más largo.")
                    
        elif opciones == 4:
            if not Datos_generales:
                print("No hay libros registrados para ofrecer una recomendación.")
            else:
                
                libro_recomendado = random.choice(Datos_generales)
                print("\n--- Recomendación de Libro ---")
                print("¡Podrías disfrutar de este libro!")
                mostrar_libro(libro_recomendado)
                
        elif opciones == 5:
            print("Saliendo de la búsqueda. ¡Hasta luego!")
            break 
            
        else:
            print("Opción no válida. Ingrese un número del 1 al 5.")
            
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero para la opción.")
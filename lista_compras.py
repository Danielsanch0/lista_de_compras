
lista_compras = []


while True:
   
    print("\nMenú de opciones:")
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Mostrar lista")
    print("4. Salir")

   
    opcion = input("Por favor, selecciona una opción (1-4): ")

   
    if opcion == "1":
       
        articulo = input("Ingresa el nombre del artículo: ")
        lista_compras.append(articulo)
        print(f"Artículo '{articulo}' agregado a la lista.")
    elif opcion == "2":
        
        if lista_compras:
            print("\nLista de compras actual:")
            for i, articulo in enumerate(lista_compras):
                print(f"{i}. {articulo}")
            try:
                indice = int(input("Ingresa el índice del artículo a eliminar: "))
                if 0 <= indice < len(lista_compras):
                    eliminado = lista_compras.pop(indice)
                    print(f"Artículo '{eliminado}' eliminado de la lista.")
                else:
                    print("Índice inválido. Intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor ingresa un número.")
        else:
            print("La lista de compras está vacía.")
    elif opcion == "3":
       
        if lista_compras:
            print("\nLista de compras actual:")
            for i, articulo in enumerate(lista_compras):
                print(f"{i}. {articulo}")
        else:
            print("La lista de compras está vacía.")
    elif opcion == "4":
        
        print("Gracias por usar la lista de compras. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")

from statistics import mean
# ------- CARGAR CONTENIDO -------
# Cargamos el contenido del archivo `dataset_paises.csv` en una lista llamada `paises_lista`
def cargar_contenido():
    paises_lista = []
    with open('dataset_paises.csv', 'r', encoding='utf-8') as archivo:

        for lineas in archivo:
            nombre, poblacion, superficie, continente = lineas.strip().split(',') 
            paises_lista.append({
                'Nombre': nombre,
                'Población': int(poblacion),
                'Superficie': int(superficie),
                'Continente': continente
            })
        return paises_lista

# -------- BUSCAR --------
def buscar_pais(nombre, paises_lista):
    for p in paises_lista:
        if nombre in p['Nombre'].lower(): #Nos aseguramos de normalizar el nombre
            return p
    return None # En caso de no encontrar el país, devolvemos None

# ------- FILTRAR  -------
def filtrar_continente(paises_lista):
    print('\n----- Lista de países (por continente) -----\n')
    for paises in paises_lista:
        print(f'País: {paises['Nombre']}\nContinente: {paises['Continente']}')
        print('--------------------------')

def filtrar_rango_poblacion(paises_lista):
    print('\n----- Lista de países (por rango de población) -----\n')
    for paises in paises_lista:
        print(f'País: {paises['Nombre']}\nPoblación: {paises['Población']:,} habitantes'.replace(",", ".")) #Colocamos el número de habitantes separado por puntos
        print('--------------------------')                                                                 #Ej: 100.000.000 en lugar de 100000000

def filtrar_rango_superficie(paises_lista):
    print('\n----- Lista de países (por rango de superficie) -----\n')
    for paises in paises_lista:
        print(f'País: {paises['Nombre']}\nSuperficie: {paises['Superficie']:,} km²'.replace(",", "."))
        print('--------------------------')


# ------- ORDENAR -------
def ordenar_nombre(paises_lista):
    lista_ordenar_nombre = []
    for paises in paises_lista: #Recorremos la lista con un bucle for
        lista_ordenar_nombre.append(paises['Nombre'])
        lista_ordenar_nombre.sort() #Ordenamos los países de forma ascendente
    print(f'\n-------- Lista de países ordenada: --------\n')
    for p in lista_ordenar_nombre:
        print(f'★ {p}') # Listamos los países con saltos de línea para mayor legibilidad

def ordenar_poblacion(paises_lista):
    lista_poblaciones = [] #Creamos una nueva lista
    for pais in paises_lista: #Recorremos la lista original
        lista_poblaciones.append(pais["Población"]) #Agregamos los valores de 'Población' a la nueva lista
    lista_poblaciones.sort()   #Ordenamiento ascendente

    print('\n-------- Lista de poblaciones ordenada de menor a mayor: --------\n')

    for poblacion in lista_poblaciones:
        for pais in paises_lista:
            if pais["Población"] == poblacion:
                print(f'✶ {pais["Nombre"]}: {poblacion:,} habitantes'.replace(',', '.')) #Mostramos la lista
                break 

def ordenar_superficie(paises_lista):
    lista_superficies = []
    for pais in paises_lista:
        lista_superficies.append(pais["Superficie"]) #Repetimos lo mismo que hicimos en la función `ordenar_poblacion()`
    lista_superficies.sort()  

    print('\n-------- Lista de superficies ordenada de menor a mayor: --------\n')

    for superficie in lista_superficies:
        for pais in paises_lista:
            if pais["Superficie"] == superficie:
                print(f'✶ {pais["Nombre"]}: {superficie:,} km²'.replace(',', '.'))
                break

# ------- ESTADÍSTICAS -------
def menor_y_mayor_poblacion(paises_lista):
    pais_menor_poblacion = paises_lista[0] #Inicializamos variables
    pais_mayor_poblacion = paises_lista[0]

    for paises in paises_lista: #Recorremos la lista
        if paises['Población'] > pais_mayor_poblacion['Población']:
            pais_mayor_poblacion = paises #Realizamos comparaciones para encontrar el país de menor y mayor población
        elif paises['Población'] < pais_menor_poblacion['Población']:
            pais_menor_poblacion = paises
        else:
            continue #Si hay algún país con población igual al anterior, saltamos a la siguiente iteración
    print('\n---- País con menor población ----\n') #Mostramos ambos países de forma ordenada
    print(f'{pais_menor_poblacion['Nombre']}: {pais_menor_poblacion['Población']:,} habitantes.'.replace(',', '.'))
    print('\n---- País con mayor población ----\n')
    print(f'{pais_mayor_poblacion['Nombre']}: {pais_mayor_poblacion['Población']:,} habitantes.'.replace(',', '.'))

def promedio_poblaciones(paises_lista):
    poblaciones = [pais['Población']  for pais in paises_lista] #Cargamos los valores de `población` en una nueva lista `poblaciones`
    promedio = mean(poblaciones) #Sacamos su promedio 
    promedio = int(promedio) #Lo truncamos

    print('\n---- Promedio de poblaciones ----\n')
    print(f'{promedio:,} habitantes.'.replace(',', '.')) 


def promedio_superficies(paises_lista):
    superficies = [pais['Superficie'] for pais in paises_lista] #Realizamos lo mismo que en la función `promedio_poblaciones()`
    promedio = mean(superficies)
    promedio = int(promedio)

    print('\n---- Promedio de superficies ----\n')
    print(f'{promedio:,} km²'.replace(',', '.'))

def cantidad_por_continente(paises_lista):
    contador = {} #Nuevo diccionario

    for pais in paises_lista: #Recorremos la lista
        continente = pais['Continente'] 

        if continente not in contador: # Si el continente no está en el diccionario, lo agregamos
            contador[continente] = 0

        contador[continente] += 1 # Si está, sumamos 1
    print('\n---- Cantidad de países por continente ----\n')
    for continente, cantidad in contador.items():
        print(f'✶ {continente}: {cantidad}') #Mostramos la cantidad de países en cada continente, en forma ordenada


lista_de_paises = cargar_contenido() #<- Cargamos el valor del CSV en la variable

# ------- MENÚ PRINCIPAL -------
while True: 
    print('\n------ MENÚ DE OPCIONES ------')
    print('1. Filtrar países\n2. Ordenar países\n3. Mostrar estadísticas\n4. Buscar país por nombre\n5. Salir')

# Controlamos errores al momento de ingresar la opción
    opcion = input('Opción: ')

    while not opcion.isdigit(): #Si la opción no es un dígito, se muestra por pantalla
        print('\nEntrada inválida.\nIntente nuevamente.\n')
        opcion = input('Opción: ') #Ingreso nuevamente de la opción

    opcion = int(opcion) #Pasamos a entero

# ------ MENÚ MATCH/CASE ------
    match opcion:
        case 1:
            # FILTRAR PAÍSES (MENÚ)
            print('\nFiltrar países por...')
            print('a. Continente\nb. Rango de población\nc. Rango de superficie')
            
            filtrar_opcion = input('Opción elegida: ').lower() #Pasamos a minúsculas para comparar
            if filtrar_opcion == 'a':
                filtrar_continente(lista_de_paises) #Llamada a funciones, pasamos `lista_de_paises` como parámetro
            elif filtrar_opcion == 'b':
                filtrar_rango_poblacion(lista_de_paises)
            elif filtrar_opcion == 'c':
                filtrar_rango_superficie(lista_de_paises)
            else:
                print('Opción inválida') #Si se ingresa una opción inválida, se muestra por pantalla
                continue #Saltamos a la siguiente iteración

        case 2:
            # ORDENAR PAÍSES (MENÚ)
            print('\nOrdenar países por...')
            print('a. Nombre\nb. Población\nc. Superficie')

            ordenar_opcion = input('Opción elegida: ').lower() #Repetimos lo mismo que hicimos con el menú anterior
            if ordenar_opcion == 'a':
                ordenar_nombre(lista_de_paises)
            elif ordenar_opcion == 'b':
                ordenar_poblacion(lista_de_paises)
            elif ordenar_opcion == 'c':
                ordenar_superficie(lista_de_paises)
            else: 
                print('Opción inválida')
                continue

        case 3:
            # MOSTRAR ESTADÍSTICAS (MENÚ)
            print('\nMostrar estadísticas...')
            print("""
            a. País con mayor y menor población
            b. Promedio de población
            c. Promedio de superficie
            d. Cantidad de países por continente\n""")
            
            estadisticas_opcion = input('Opción elegida: ').lower() #Repetimos lo mismo que hicimos en el menú anterior

            if estadisticas_opcion == 'a':
                menor_y_mayor_poblacion(lista_de_paises)
            elif estadisticas_opcion == 'b':
                promedio_poblaciones(lista_de_paises)
            elif estadisticas_opcion == 'c':
                promedio_superficies(lista_de_paises)
            elif estadisticas_opcion == 'd':
                cantidad_por_continente(lista_de_paises)
            else:
                print('Opción inválida')
                continue
        case 4:
            # BUSCAR PAÍS POR NOMBRE
            print('\nIngrese el nombre del país que desea buscar: ')
            nombre = input('-> ').lower() #Pasamos a minúsculas para normalizar el nombre

            encontrado = buscar_pais(nombre, lista_de_paises) #Definimos la variable `encontrado` con el resultado de la función `buscar_pais()`

            if encontrado == None: #Si la función retorna `None` (no encontró el país), se informa por pantalla
                print(f'{nombre.capitalize()} no está en la lista de países.') #Colocamos mayúsculas al principio por estética
            else: #Si se encuentra el país, mostramos sus datos en una lista
                print('----------- PAÍS ENCONTRADO ----------------')
                print(f'Nombre: {encontrado['Nombre']}')
                print(f'Población: {encontrado['Población']:,} habitantes'.replace(',', '.'))
                print(f'Superficie: {encontrado['Superficie']:,} km²'.replace(',', '.'))
                print(f'Continente: {encontrado['Continente']}')
        case 5:
            # SALIR
            # Se imprime un mensaje por pantalla indicando salida y rompe el bucle
            print('Saliendo...')
            break
        case _:
            # ENTRADA INVÁLIDA
            # Se indica por pantalla y saltamos a la siguiente iteración
            print('Opción inválida')
            continue

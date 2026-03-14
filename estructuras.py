# 1. Declara una variable de cada una de las siguientes estructuras de datos con al menos 3 elementos cada una
mi_lista=["verde","amarillo","rojo"]    #esta es una lista, se determina usando [] y es modificable
mi_diccionario={"nombre":"Pepe","edad":33,"ciudad":"Titirilquén"}   #el diccionario se difencia en que su estructura tiene {llave: valor}, y se usan {}
mi_tupla=("mono","caballo","cerdo","tigre") #la tupla es un contenedor inmutable luego de ser declarado y se usan ()
mi_set={"Nintendo","Sony","Sega","Microsoft"}   #el set o conjunto de datos no puede tener valores duplicados, al igual que el diccionario usa {}
print(mi_lista,mi_diccionario,mi_set,mi_tupla)

# 2.acceder a datos
# Imprime el segundo elemento de la lista.
print(mi_lista[1])

# Imprime una clave y su valor desde el diccionario.
# también pensé en usar: print(mi_diccionario.items()), pero al imprimir por pantalla empezaba con dict_items() y no queda tan legible
print(f"Clave: nombre , Valor: {mi_diccionario['nombre']}")

# Explica con comentarios por qué no puedes acceder por índice a un set.
#   El set es una estructura desordenada por lo cual un elemento dentro de este puede cambiar de índice

#3. Contar e iterar
# Usa len() para mostrar la cantidad de elementos en cada estructura.
# Itera sobre cada estructura usando un for y muestra cada elemento por pantalla.
def mostrar_todo():
    print(f"Cantidad de elementos en la lista: {len(mi_lista)}")
    for p in mi_lista:
        print(f"    {p}")
    print(f"Cantidad de elementos en el diccionario: {len(mi_diccionario)}")
    for clave, valor in mi_diccionario.items():
        print(f"    {clave} : {valor}")
    print(f"Cantidad de elementos en la tupla: {len(mi_tupla)}")
    for p in mi_tupla:
        print(f"    {p}")
    print(f"Cantidad de elementos en el conjunto: {len(mi_set)}")
    for p in mi_set:
        print(f"    {p}")
    print("----------------------------------")

mostrar_todo()

# 4. modificar estructuras 
# Agrega un nuevo elemento a la lista y al conjunto.
mi_lista.append("blanco")
mi_set.add("Valve")

# Borra un elemento de la lista.
mi_lista.remove("amarillo")

# Agrega una nueva clave al diccionario.
mi_diccionario.update({"tiene_gato":True})


mostrar_todo()

# Intenta modificar la tupla y comenta qué ocurre.
# intentando con los métodos .add() y .append() me dan error, responde que la tupla no tiene esos atributos (y de antemano sabíamos que era unmutable)



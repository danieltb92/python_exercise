# Abrir un archivo
# y añadir contenido al ya existente

fichero = open('ejemplo.txt', 'w')
fichero.write("Amor por el codigo\nQuieres aprender a programar y conocer a alguien,")
fichero.write("\no solo aprender a programar.\n")
fichero.close()

fichero = open('ejemplo.txt', 'a')
fichero.write("hola")
fichero = open('ejemplo.txt', 'r')
print(fichero.read())

fichero = open('ejemplo.txt')
print(fichero.readline())
fichero.close()
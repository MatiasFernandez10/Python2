def eje2():
    archivo = open("archivo.txt", "r")

    for line in archivo:
        print(line.strip())
    archivo.close()

eje2()
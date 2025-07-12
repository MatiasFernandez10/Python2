def eje2():
    m = int(input("ingrese un numero:"))
    array = []

    try: 
        arch = open("archivo.txt", "r")

        for line in arch:
            array.append(line)
        print(line[m-1])

        arch.close()
    except IOError:
            print("no se encontro el archivo")

eje2()
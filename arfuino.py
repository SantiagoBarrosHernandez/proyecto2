
x=input("introdusca una medida")
x=int(x)
i=0
while (i==0) :

    print("1 -convertir de pulgadas a centimetros")
    print("2 -convertir de centimetros a pulgadas")
    print("3 -convertir de kilometro  a metros")
    print("4 -convertir de metros a kilometros")
    print("5 -convertir de kilometros a millas")
    print("6 -convertir de millas a kilometros")
    print("7 -convertir de año luz a UA")
    print("8 -convertir de UA  año luz")
    print("9 -convertir de UA a kilometros")
    print("10 -convertir de kilometros a UA")

    d=input("introduzca una opcion")
    d=int(d)

    if d==1 :

        print("convertir de pulgadas a centimetros")
        f=(x * 2,54)
        f = str(f)
        print("el resultado es:" +f)

    if d == 2:
        print("convertir de centimetros a pulgadas"
        f = (x / 2, 54)
        f = str(f)
        print("el resultado es:" + f)

    if d == 3:
        print("convertir de kilometros a metros")
        f = (x / 1000)
        f = str(f)
        print("el resultado es:" + f)

    if d == 4:
        print("convertir de metros a kilometros")
        f = (x * 1000)
        f = str(f)
        print("el resuñtado es:" + f)

    if d == 5:
        print("convertir de kilometros a millas")
        f = (x * 2, 54)
        f = str(f)
        print("el resuñtado es:" + f)
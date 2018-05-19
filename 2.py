'''Santiago Barros'''
i=0
while (i==0) :
    m = input("digite una tecla entre w,a,s,d")

    if m=='w':
        lienzo.move(1,0,-50)
        Tk.update(ventana)
        time.sleep(1)


    if m=='s':
        lienzo.move(1,0,50)
        Tk.update(ventana)
        time.sleep(1)



    if m =='a':
        lienzo.move(1,-50,0)
        Tk.update(ventana)
        time.sleep(1)



    if m=='d':
        lienzo.move(1,50,0)
        Tk.update(ventana)
        time.sleep(1)
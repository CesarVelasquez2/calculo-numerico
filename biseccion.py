import math

def funcion(x):
    return math.atan(x)+x-1

def biseccion(a,b,funcion,minerror,maxinteraccion):

    if(not isinstance(a, (int,float)) or not isinstance(b, (int,float)) or not isinstance(minerror, (int,float)) or not isinstance(maxinteraccion, (int,float))):
    
        if(not isinstance(a, (int,float))):
            print("la variable a no contiene un valor numerico")
        if(not isinstance(b, (int,float))):
            print("la variable b no contiene un valor numerico")
        if(not isinstance(minerror, (int,float))):
            print("la variable minerror no contiene un valor numerico")
        if(not isinstance(maxinteraccion, (int,float))):
            print("la variable maxinteraccion no contiene un valor numerico")
        
        raise ValueError("")
    
    if(minerror < 0 or minerror > 1):
        raise ValueError("la variable minerror no se encuentra entre los valores 0 y 1")
    
    if(maxinteraccion < 1 or maxinteraccion > 100):
        raise ValueError("la variable maxinteraccion no se encuentra entre los valores 1 y 100")
    
    if(not callable(funcion)):
        raise TypeError("la variable funcion no cumplen con los requerimientos")

    if(a>b):
        raise ValueError("la variable a debe ser menor que la variable b")

    i = 0
    calc_error = 1.1

    while True:
        i+=1
        m = (a+b)/2

        fa = funcion(a)
        fm = funcion(m)

        # la variable band sirve para determinar entre a y b cual es la que se va a juntar con m. 0 para a y 1 para b.
        if(fa<0):
            if(fm<0):
                a = m
            else:
                b = m
        else:
            if(fm>0):
                a = m
            else:
                b = m
    
        if(i>=2):
            calc_error = abs((m - manterior)/ m)

        if(calc_error <= minerror or i == maxinteraccion):
            return m if calc_error <= minerror else None

        manterior = m


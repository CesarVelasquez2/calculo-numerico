from biseccion import biseccion
import unittest
import math

def funcion(x):
    return math.atan(x)+x-1

def funcion2(x):
    return math.exp(-x) - math.log(x)

def funcion3(x):
    return (math.exp(-x) - math.log(x))/5

class Test_biseccion(unittest.TestCase):

    def test_resultado(self):

        resultado = biseccion(0,1,funcion,0.01,100)
        resultado2 = biseccion(1,1.5,funcion2,0.01,100)
        resultado3 = biseccion(1,1.5,funcion3,0.0000001,10)

        self.assertEqual(resultado,0.51953125)
        self.assertEqual(resultado2,1.3046875)
        self.assertIsNone(resultado3)

    def test_a_menor_b(self):

        with self.assertRaises(ValueError) as exc:
            biseccion(1,0,funcion,0.01,100)

        self.assertEqual(str(exc.exception), "la variable a debe ser menor que la variable b")

    def test_es_numero(self):

        with self.assertRaises(ValueError) as exc:
            biseccion("hola",funcion,funcion,'f',"sdgd")

        self.assertEqual(str(exc.exception),"")

    def test_minerror(self):

        with self.assertRaises(ValueError) as exc:
            biseccion(0,1,funcion,2,100)

        self.assertEqual(str(exc.exception),"la variable minerror no se encuentra entre los valores 0 y 1")

        with self.assertRaises(ValueError) as exc2:
            biseccion(0,1,funcion,-2,100)

        self.assertEqual(str(exc2.exception),"la variable minerror no se encuentra entre los valores 0 y 1")

    def test_maxinteraccion(self):

        with self.assertRaises(ValueError) as exc:
            biseccion(0,1,funcion,0.01,-2)

        self.assertEqual(str(exc.exception),"la variable maxinteraccion no se encuentra entre los valores 1 y 100")

        with self.assertRaises(ValueError) as exc2:
            biseccion(0,1,funcion,0.01,101)

        self.assertEqual(str(exc2.exception),"la variable maxinteraccion no se encuentra entre los valores 1 y 100")

    def test_funcion(self):

        with self.assertRaises(TypeError) as exc:
            biseccion(0,1,"gsgs",0.1,100)
        
        self.assertEqual(str(exc.exception),"la variable funcion no cumplen con los requerimientos")

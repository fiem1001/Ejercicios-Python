#define la función "leer número" 
#define la función "imprime suma"

#lee y guarda primer número
#lee y guarda segundo número
#imprime la suma de ambos números

def lee_numero():
    x = int(input("Ingresa el número: "))
    return x

def imprime_resultado(x, y):
    resultado = x + y
    print("La suma de los números es" , resultado)

def main():
    x = lee_numero()
    y = lee_numero() 
    imprime_resultado(x, y) 
main()  
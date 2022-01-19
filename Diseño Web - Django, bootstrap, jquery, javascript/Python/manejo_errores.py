def run():
    try:
        num1 = int(input('Escribe aqui un numero entero: '))
        num2 = int(input('Escribe el segundo numero aqui: '))
        print(f"la suma de los dos numeros es: {num1+num2}")
    except Exception as e:
        print(f'Hubo un error,  {e}')
    else:
        print('ningun error.')
    finally:
        print('FINALLY -> Es algo que siempre se ejecute este bien o mal.')
        run()

if __name__ == "__main__":
    run()
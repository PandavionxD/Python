def run():
    contador=0
    a=2**contador
    LIMITE= 1000000
    while a<LIMITE:
       print('2 eleveado a la potencia de  ',contador,' es igual a ',a)
       contador+=1
       a=2**contador

if __name__ == '__main__':
    run()
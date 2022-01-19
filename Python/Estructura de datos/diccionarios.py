#Un diccionario tendra los siguientes valores Llave y valor
def run():
    mi_diccionario = {
        'llave_1':1,
        'llave_2':2,
        'llave_3':3
    }
    #Imprimira todo el diccionario
    # print(mi_diccionario)
    #Imprimiendo el valor especificando la llave
    # print(mi_diccionario['llave_1'])
    paises ={
        'Argentina':1234567,
        'Peru':2345678,
        'Brasil':80976543
    }
    #Usaremos el ciclo for para ver la llave imprimira los paises
    for pais in paises.keys():
        print(pais)
    #Usaremos el ciclo for para recorrer los valores o sea los habitantes
    for habitantes in paises.values():
        print(habitantes)
    #Usaremos el ciclo for para recorrer tanto la llave como el valor
    for i,j in paises.items():
        print(i,' -->',j)


if __name__ =="__main__":
    run()
#Numeros impares
def run():
    for i in range(101):
        if i%2==0:
            continue
        print(i,end=", --> ")
    

if __name__ =='__main__':
    run()
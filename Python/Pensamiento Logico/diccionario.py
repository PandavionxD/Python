#Diccionarios
dic_1 ={
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5
}
print(dic_1)

for i in dic_1:
    print(i)

print(dic_1['two'])

for a in dic_1.keys():
    print(a)

for e in dic_1.values():
    print(e)

for b,c in dic_1.items():
    print(f'La llave del diccionario es {b} y su valor es \t {c}')
persona_1=input('Escribe el nombre de la primera persona: ')
edad_1=int(input('Escribe la edad de la primera persona: '))
persona_2=input('Escribe el nombre de la segunda persona: ')
edad_2=int(input('Escribe la edad de la segunda persona: '))
if edad_1>edad_2:
    print(f'{persona_1} es mayor que {persona_2}')
elif edad_2>edad_1:
    print(f'{persona_2} es mayor que {persona_1}')
else:
    print(f'{persona_1} y {persona_2} tienen la misma edad')
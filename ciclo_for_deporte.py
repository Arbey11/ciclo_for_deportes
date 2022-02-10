'''Elaborar un algoritmo que lea para un grupo de 10 personas el nombre, la edad y el deporte 
(1= fútbol, 2=baloncesto, 3= otro deporte) 

-imprima cuantos de fútbol son mayores de edad
-cuantos de baloncesto son menores de edad 
-cuantas personas prefieren otro deporte.'''

may_edad = 0
men_edad = 0
otro_dep = 0

for i in range(10):

    nombre = input('ingrese nombre: ')
    edad = int(input('ingrese edad: '))
    deporte = int(input('ingrese deporte, 1 = futbol, 2 = baloncesto, 3 = otro deporte, : '))


    if edad >=18 and deporte == 1:
        may_edad = may_edad + 1
        

    elif edad <= 17 and deporte == 2:
        men_edad = men_edad + 1
        
    
    elif edad >= 0 and deporte == 3:
        otro_dep = otro_dep + 1
        

print('mayores de edad que juegan futbol = ', may_edad)
print('menores de edad que juegan baloncesto = ', men_edad)
print('Personas que prefieren otro deporte: ', otro_dep)    

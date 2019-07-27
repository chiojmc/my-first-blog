print("Welcome to DjangoGirls")

hacer_tarea = False
barrer_casa = True

if 5 > 3:
    print("5 es mayor")
else:
    print("5 es menor")
if hacer_tarea:
    print("Sal a jugar")
else:
    print("estás castigado")

# conditional multiple
nombre = "Chío"

if nombre == "Chío":
    print("Trabaja en MVS")
elif nombre == "Alma":
    print("Trabaja en Edenred")
elif nombre == "Vic":
    print("Es mi instructor equipo 3")
else:
    print("No sé dónde está")

volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

def hi(nombre):
    if nombre == "Victor":
        print("Cuanto llevas en Nearsoft?")
    elif nombre == "Chio":
        print(nombre+", ¿usas excel?")
    elif nombre == "Alma":
        print("Que te parece python?")
    else:
        print("No se que preguntarte!!!!")
hi("Chio")

# loops

lucky_numbers = [10,4,6,3,298,45,45]
# para cada num en lucky_numbers
for num in lucky_numbers:
    print(num * 2) 


personas = [
    {"name": "Victor"},
    {"name": "Alma"},
    {"name": "Chio"}
]
# para cada num en lucky_numbers has lo siguiente
for persona in personas:
    print(persona["name"]) 

for idx in range(10):
    print(idx)
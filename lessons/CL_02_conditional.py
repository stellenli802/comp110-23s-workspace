"""CL02"""

__author__ = "730476572"

2 + 4 / 2 * 2
print(type(2 + 4 / 2 * 2)) #float bcuz standard division converts everything to float first

print(220 >= int(("1" + "1" + "0") * 2)) #false bcuz 220 !>= 110110

#To make the above statement true:
print(220 >= int("1" + "1" + "0") * 2)

#traffic light conditional:
light: str = input("What color is the light? ").lower() #.lower() makes it not case sensitive

if (light == "green"):
    print("GO")
    print("Drive safe! Love, mom.")
elif (light == "yellow"):
    print("vroom")
elif (light == "red"):
    print("STOP")
else:
    print("Go report this to the authorities.")
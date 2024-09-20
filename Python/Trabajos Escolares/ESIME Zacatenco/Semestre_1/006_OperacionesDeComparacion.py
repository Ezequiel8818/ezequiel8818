cal1=float(input("Escriba la calificación del primer parcial: "))
cal2=float(input("Escriba la calificación del segundo parcial: "))
cal3=float(input("Escriba la calificación del tercer parcial: "))

promedio=(cal1+cal2+cal3)/3

if(promedio==10):
    print(f'\nHas aprobado la materia con un promedio de {promedio:.2f}')
    print("Asiste a control escolar por la beca de excelencia")
elif(promedio>=6):
    print(f'\nHas aprobado la materia con un promedio de {promedio:.2f}')
else:
    print(f'\nHas reprobado la materia con un promedio de {promedio:.2f}')
    asesorias=input("\nAsistirás a asesorias?: ")
    asesorias=asesorias.rstrip()
    if(asesorias == "si" or asesorias == "SI" or asesorias == "Si" or asesorias =="Sí" or asesorias == "sí" or asesorias == "SÍ"):
        boleta=int(input("\nAnota tu numero de boleta para inscribirte a Asesorias: "))
        print("\nSe te contactará en un futuro, gracias.")
    elif(asesorias == "no" or asesorias =="NO" or asesorias =="No"):
        print("\nHasta Luego")
    else:
        print("\nPrograma terminado debido a error en el sistema")
    
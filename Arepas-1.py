print("Ingredientes y cantidades para hacer arepas")

#el usuario indica las cantidad de ingredientes a agregar
harina = int(input("Introduce las tazas de harina que tienes: "))
aceite = float(input("Introduce las cucharadas de aceite que tienes: "))
sal = float(input("Introduce las cucharaditas de sal que tienes: "))
#se convierten las unidades a tazas
aceite = aceite/16
sal = sal/16/3

agua = int(input("Introduce la tazas de agua que tienes: "))



#se especifican las variables y su equivalencia para llegar a un valor preciso

bol = harina + agua + sal
budare = bol + aceite*0.75

print (budare)
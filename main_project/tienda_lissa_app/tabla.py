
a = 1
mult = 2
tabla = []

while True:

    if a<=10:
        tabla.append({f"{mult} x {a}":mult*a})
        a += 1
    else:
        a = 1
        mult +=1

        print(tabla,"\n")
        tabla.clear()
    
    if mult == 10:
        break
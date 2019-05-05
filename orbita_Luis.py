#Taller 2

G=6.67e-11 #Constante de gravitacional
Ms=1.989e30 #Masa del sol
pi=3.1416

Rp=float(input("Ingrese  el radio del perihelio:"))
Vp=float(input("Ingrese la velocidad del perihelio:"))

Va=(((2*G*Ms)/(Vp*Rp))+(((2*G*Ms)/(Vp*Rp))**2+4*((Vp**2-2*G*Ms)/Rp))**1/2)/2

Ra=(Rp*Vp)/Va
a=(Rp+Ra)/2
b=(Rp*Ra)**(1/2)
T=(2*pi*a*b)/(Rp*Vp)
E=(Ra-Rp)/(Ra+Rp)

print("La velocidad del afelio es:" ,Va)
print("El radio del afelio:" ,Ra)
print("El semieje mayor es:" ,a)
print("El semieje menor es:" ,b)
print("El periodo orbital es:", T)
print("La excentricidad orbital es:" ,E)


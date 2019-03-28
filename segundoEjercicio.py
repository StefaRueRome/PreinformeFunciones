a=int(input("Ingrese un número: "))
b=int(input("Ingrese el número que desea que sea elevado: "))

def cuadrado(a,b):
	oper=a**b
	print(oper)
	return oper

oper1=cuadrado(a,b)

c=int(input("Ingrese otro número: "))
d=int(input("Ingrese el número que desea que sea elevado: "))

oper2=cuadrado(c,d)

if oper1>oper2:
	print("La primera es mayor que la segunda")
else:
	print("La segunda es mayor que la primera")
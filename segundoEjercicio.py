def cuadrado(a,b):
	oper=a**b
	print(oper)
	return oper

for i in range(0,2):
	a=int(input("Ingrese la base: "))
	b=int(input("Ingrese el exponente: "))
	if i==0:
		oper1=cuadrado(a,b)
	else:
		oper2=cuadrado(a,b)

if oper1>oper2:
	print("El primer resultado es mayor que el segundo")
else:
	print("El segundo resultado es mayor que el primero")
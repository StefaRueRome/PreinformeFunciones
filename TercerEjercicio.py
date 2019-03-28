
n=int(input("Ingrese un número: "))

def primo(cont):
	cont=0
	if n%1==0:
		cont=cont+1
		if n%n==0:
			cont=cont+1
			return cont

if cont>2:
	print("El número no es primo")
else:
	if cont<=2:
		print("El número es primo")

primo(cont)


n=int(input("Introduzca un número: "))
def primo_hermano():
	cont=0
	if n%6==0:
		print("No es primo hermano ")
	else:
		for i in range(n,n+1):
			if i%1==0:
				cont+=1
				if i%i==0:
					cont+=1
					if cont<=2:
						print("Es primo hermano")
					else:
						print("No es primo hermano")

primo_hermano()
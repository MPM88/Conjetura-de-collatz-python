#Prueba de la conjetura de collatz en Python
def IsEven(Number):
	if (Number % 2 == 1):
		return False
	else:
		return True

def CalculateCollatz(Number):
	while Number > 1:
		if (IsEven(Number) == False):
			Number  = Number * 3 + 1
			print(Number)
		else:
			Number = Number / 2
			print(Number)

CalculateCollatz(int(input('Ingresa un numero\n')))
input()
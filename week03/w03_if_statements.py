# Comparando números
n1 = int (input("What is the first number? "))
n2 = int (input ("What is the second number? "))

if n1 > n2:
    print ("The first number is greater")
else:
    
    print("The first number is not greater")

if n1 == n2:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if n2 > n1:
    print("The second number is greater")
else:
    print("The second number is not greater")

print() # Espacio en blanco

# --- COMPARANDO TEXTO ---
mi_animal = "bear"
usuario_animal = input("What is your favorite animal? ")

# .lower() hace que "BEAR" o "Bear" coincidan con "bear"
if usuario_animal.lower() == mi_animal.lower():
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
import os
from operations_on_numbers import*

os.system("cls") 

print("Choose what do you what to do: ")
print(" 1. Add ")
print(" 2. Subtract ")
print(" 3. Divide ")
print(" 4. Multiply ")
print(" 5. Exponentiate ")
print(" 6. Root ")

choice = input(" Enter your choice ( 1/2/3/4/5/6):")

if choice == "1":
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))
    
    print(a ,"+", b ,"=" , Add(a,b))
    
elif choice == "2":
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))
    
    print(a ,"-", b ,"=" , Subtract(a,b))
    
elif choice == "3":
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))
    
    print(a ,"/", b ,"=" , Divide(a,b))
    
elif choice == "4":
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))
    
    print(a ,"*", b ,"=" , Multiply(a,b))
    
elif choice == "5":
    a = float(input("Enter base: "))
    b = float(input("Enter power (exponent): "))
    
    print(a ,"^", b ,"=" , Exponentiate(a,b))
    
elif choice == "6":
    a = float(input("Enter radiocant: "))
    b = float(input("Enter index (degree) : "))
    
    print(" The", b, "root of", a , "=" , Root(a,b))
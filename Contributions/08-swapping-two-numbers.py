# getting input
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("\nValues before swapping\n","a =",a,"\n b =",b)

# swap using tuple assignment
a,b = b,a

print("\nValues After swapping\n","a =",a,"\n b =",b)

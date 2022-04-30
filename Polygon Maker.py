import turtle
print("\n<<< Welcome to polygon maker >>>")
n = int(input("\nEnter the number of sides of the polygon: "))
i = int(((n-2)*180)/n)
s = turtle.getscreen()
t = turtle.Turtle()
while n != 0:
    t.forward(50)
    t.left(180 - i)
    n = n - 1
turtle.done()
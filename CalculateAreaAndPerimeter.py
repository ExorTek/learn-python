def CalculateArea():
    shortEdge = int(input("Kısakenar: "))
    longEdge = int(input("Uzunkenar: "))
    area = shortEdge * longEdge
    print(f"Short Edge = {shortEdge} Long Edge = {longEdge} area of a rectangle = {area}")


def CalculatePerimeter():
    shortEdge = int(input("Kısakenar: "))
    longEdge = int(input("Uzunkenar: "))
    perimeter = 2 * (shortEdge + longEdge)
    print(f"Short Edge = {shortEdge} Long Edge = {longEdge} perimeter of a rectangle = {perimeter}")


CalculateArea()
CalculatePerimeter()

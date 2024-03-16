def calculate_area(x1, y1, x2, y2, x3, y3):
    side1 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
    side2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    side3 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    list = [side1,side2,side3]
    list.sort()
    newside1= list[0]
    newside2= list[1]

    return newside1 * newside2

n = int(input())
for _ in range(n):
    vertices = list(map(float, input().split()))
    x1, y1, x2, y2, x3, y3 = vertices
    area = calculate_area(x1, y1, x2, y2, x3, y3)
    print(f"Area of rectangle with vertices ({x1}, {y1}), ({x2}, {y2}), ({x3}, {y3}) is {area}")
